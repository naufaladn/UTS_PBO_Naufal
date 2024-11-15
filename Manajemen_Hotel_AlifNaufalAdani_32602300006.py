from datetime import datetime

class Kamar:
    def __init__(self, nomorKamar, tipeKamar, hargaPerMalam):
        self.__nomorKamar = nomorKamar
        self.__tipeKamar = tipeKamar
        self.__hargaPerMalam = hargaPerMalam
        self.__status = "tersedia"
    
    def tampilkanInfoKamar(self):
        print(f"Nomor Kamar: {self.__nomorKamar}")
        print(f"Tipe Kamar: {self.__tipeKamar}")
        print(f"Harga per Malam: Rp{self.__hargaPerMalam}")
        print(f"Status: {self.__status}")
    
    def setStatus(self, status):
        self.__status = status
    
    def getStatus(self):
        return self.__status
    
    def getNomorKamar(self):
        return self.__nomorKamar

class KamarSuite(Kamar):
    def __init__(self, nomorKamar, hargaPerMalam):
        super().__init__(nomorKamar, "Suite", hargaPerMalam)
        self.__fasilitas = "Spa, Pool View, Room Service"
    
    def tampilkanInfoKamar(self):
        super().tampilkanInfoKamar()
        print(f"Fasilitas Tambahan: {self.__fasilitas}")

class Tamu:
    def __init__(self, nama, nomorIdentitas, kontak):
        self.__nama = nama
        self.__nomorIdentitas = nomorIdentitas
        self.__kontak = kontak
        self.__daftarReservasi = []
    
    def tampilkanInfoTamu(self):
        print(f"Nama: {self.__nama}")
        print(f"Nomor Identitas: {self.__nomorIdentitas}")
        print(f"Kontak: {self.__kontak}")
        print("Daftar Reservasi Aktif:")
        for reservasi in self.__daftarReservasi:
            reservasi.tampilkanInfoReservasi()

    def tambahReservasi(self, reservasi):
        self.__daftarReservasi.append(reservasi)
    
    def hapusReservasi(self, reservasi):
        self.__daftarReservasi.remove(reservasi)

class Reservasi:
    def __init__(self, tamu, kamar, tanggalCheckIn, tanggalCheckOut):
        self.__tamu = tamu
        self.__kamar = kamar
        self.__tanggalCheckIn = tanggalCheckIn
        self.__tanggalCheckOut = tanggalCheckOut
        self.__durasiMenginap = (tanggalCheckOut - tanggalCheckIn).days
        self.__status = "aktif"
    
    def tampilkanInfoReservasi(self):
        print(f"Tamu: {self.__tamu._Tamu__nama}")
        print(f"Kamar: {self.__kamar.getNomorKamar()}")
        print(f"Check-in: {self.__tanggalCheckIn}")
        print(f"Check-out: {self.__tanggalCheckOut}")
        print(f"Durasi Menginap: {self.__durasiMenginap} malam")
        print(f"Status: {self.__status}")
    
    def batalkan(self):
        self.__status = "dibatalkan"
        self.__kamar.setStatus("tersedia")

class Hotel:
    def __init__(self):
        self.__daftarKamar = []
        self.__daftarTamu = []
        self.__daftarReservasi = []
    
    def tambahKamar(self, kamar):
        if any(k.getNomorKamar() == kamar.getNomorKamar() for k in self.__daftarKamar):
            print("Kamar dengan nomor ini sudah ada.")
        else:
            self.__daftarKamar.append(kamar)
            print("Kamar berhasil ditambahkan.")
    
    def tambahTamu(self, tamu):
        if any(t._Tamu__nomorIdentitas == tamu._Tamu__nomorIdentitas for t in self.__daftarTamu):
            print("Tamu dengan nomor identitas ini sudah ada.")
        else:
            self.__daftarTamu.append(tamu)
            print("Tamu berhasil didaftarkan.")
    
    def buatReservasi(self, tamu, kamar, tanggalCheckIn, tanggalCheckOut):
        if kamar.getStatus() == "tersedia":
            reservasi = Reservasi(tamu, kamar, tanggalCheckIn, tanggalCheckOut)
            self.__daftarReservasi.append(reservasi)
            tamu.tambahReservasi(reservasi)
            kamar.setStatus("dipesan")
            print("Reservasi berhasil dibuat.")
        else:
            print("Kamar tidak tersedia.")
    
    def batalkanReservasi(self, reservasi):
        reservasi.batalkan()
        self.__daftarReservasi.remove(reservasi)
        reservasi._Reservasi__tamu.hapusReservasi(reservasi)
        print("Reservasi berhasil dibatalkan.")
    
    def daftarKamarTersedia(self):
        print("Daftar Kamar Tersedia:")
        for kamar in self.__daftarKamar:
            if kamar.getStatus() == "tersedia":
                kamar.tampilkanInfoKamar()

def main():
    hotel = Hotel()
    
    # Menu interaktif
    while True:
        print("\nNama: Alif Naufal Adani")
        print("NIM: 32602300006\n")
        print("Menu:")
        print("1. Tambah Kamar")
        print("2. Tambah Tamu")
        print("3. Buat Reservasi")
        print("4. Batalkan Reservasi")
        print("5. Daftar Kamar Tersedia")
        print("6. Tampilkan Info Tamu")
        print("7. Keluar")
        
        pilihan = input("Pilih opsi: ")
        
        if pilihan == "1":
            nomorKamar = int(input("Nomor kamar: "))
            tipeKamar = input("Tipe kamar (Single/Double/Suite): ")
            hargaPerMalam = int(input("Harga per malam: "))
            if tipeKamar == "Suite":
                kamar = KamarSuite(nomorKamar, hargaPerMalam)
            else:
                kamar = Kamar(nomorKamar, tipeKamar, hargaPerMalam)
            hotel.tambahKamar(kamar)
        
        elif pilihan == "2":
            nama = input("Nama tamu: ")
            nomorIdentitas = input("Nomor identitas: ")
            kontak = input("Kontak: ")
            tamu = Tamu(nama, nomorIdentitas, kontak)
            hotel.tambahTamu(tamu)
        
        elif pilihan == "3":
            nama = input("Nama tamu: ")
            nomorKamar = int(input("Nomor kamar: "))
            tanggalCheckIn = datetime.strptime(input("Tanggal Check-in (YYYY-MM-DD): "), "%Y-%m-%d")
            tanggalCheckOut = datetime.strptime(input("Tanggal Check-out (YYYY-MM-DD): "), "%Y-%m-%d")
            tamu = next((t for t in hotel._Hotel__daftarTamu if t._Tamu__nama == nama), None)
            kamar = next((k for k in hotel._Hotel__daftarKamar if k.getNomorKamar() == nomorKamar), None)
            if tamu and kamar:
                hotel.buatReservasi(tamu, kamar, tanggalCheckIn, tanggalCheckOut)
            else:
                print("Tamu atau kamar tidak ditemukan.")
        
        elif pilihan == "4":
            nama = input("Nama tamu: ")
            nomorKamar = int(input("Nomor kamar: "))
            reservasi = next((r for r in hotel._Hotel__daftarReservasi if r._Reservasi__tamu._Tamu__nama == nama and r._Reservasi__kamar.getNomorKamar() == nomorKamar), None)
            if reservasi:
                hotel.batalkanReservasi(reservasi)
            else:
                print("Reservasi tidak ditemukan.")
        
        elif pilihan == "5":
            hotel.daftarKamarTersedia()
        
        elif pilihan == "6":
            nama = input("Nama tamu: ")
            tamu = next((t for t in hotel._Hotel__daftarTamu if t._Tamu__nama == nama), None)
            if tamu:
                tamu.tampilkanInfoTamu()
            else:
                print("Tamu tidak ditemukan.")
        
        elif pilihan == "7":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()