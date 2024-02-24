import os 
os.system("cls")
from prettytable import PrettyTable

class penitipan:
    def __init__(self, nama, no_hp, alamat, jenis_hewan, nama_hewan, tanggal_penitipan) :
        self.nama = nama
        self.no_hp = no_hp
        self.alamat = alamat
        self.jenis_hewan = jenis_hewan
        self.nama_hewan = nama_hewan
        self.tanggal_penitipan = tanggal_penitipan

class penitipanHewan:
    def __init__(self):
        self.data_penitipan = []
    
    def create(self, nama, no_hp, alamat, jenis_hewan, nama_hewan, tanggal_penitipan):
        self.data_penitipan.append({
            'nama': nama,
            'no hp': no_hp,
            'alamat': alamat,
            'jenis hewan': jenis_hewan,
            'nama hewan': nama_hewan,
            'tanggal penitipan': tanggal_penitipan
        })
        print("===========================================================")
        print("        DATA PENITIPAN HEWAN BERHASIL DITAMBAHKAN.         ")
        print("                     (´｡• ◡ •｡`)                            ")
        print("===========================================================")
    
    def read(self):
        if self.data_penitipan:
            table = PrettyTable()
            table.field_names = ["Nama Pemilik", "Nomor HP", "Alamat", "Jenis Hewan", "Nama Hewan", "Tanggal Penitipan"]
            for data in self.data_penitipan:
                table.add_row([data['nama'], data['no hp'], data['alamat'], data['jenis hewan'], data['nama hewan'], data['tanggal penitipan']])
            print(table)
        else:
            print("===========================================================")
            print("         TIDAK ADA DATA PENITIPAN YANG TERSEDIA.           ")
            print("                      ( • ᴖ • ｡)                           ")
            print("===========================================================")
            
    def update(self, nama, no_hp_baru, alamat_baru, jenis_hewan_baru, nama_hewan_baru, tanggal_penitipan_baru):
        updated = False
        for penitipan in self.data_penitipan:
            if penitipan['nama'] == nama:
                penitipan['no hp'] = no_hp_baru
                penitipan['alamat'] = alamat_baru
                penitipan['jenis hewan'] = jenis_hewan_baru
                penitipan['nama hewan'] = nama_hewan_baru
                penitipan['tanggal penitipan'] = tanggal_penitipan_baru
                updated = True
        return updated
            
    def delete(self, nama):
        found = False
        for data in self.data_penitipan:
            if data['nama'] == nama:
                self.data_penitipan.remove(data)
                found = True
                print("===========================================================")
                print("             DATA PENITIPAN BERHASIL DIHAPUS.              ")
                print("                      (´｡• ◡ •｡`)                           ")
                print("===========================================================")
                break
        if not found:
            print("===========================================================")
            print("             DATA TIDAK BERHASIL DITEMUKAN.                ")
            print("                      ( • ᴖ • ｡)                           ")
            print("===========================================================")
            
def main():
    penitipan = penitipanHewan()
    
    while True:
        print("===========================================================")
        print("|            Sistem Pendataan Penitipan Hewan             |")
        print("===========================================================")
        print("| 1. Tambah Data Penitipan                                |")
        print("| 2. Tampilkan Data Penitipan                             |")
        print("| 3. Perbarui Data Penitipan                              |")
        print("| 4. Hapus Data Penitipan                                 |")
        print("| 5. Keluar                                               |")
        print("===========================================================")
        print("|                         ˶ᵔ ᵕ ᵔ˶                         |")
        print("===========================================================")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            nama = input("Masukkan nama pemilik: ")
            no_hp = input("Masukkan nomor HP: ")
            alamat = input("Masukkan alamat: ")
            hewan = input("Masukkan jenis hewan: ")
            nama_hewan = input("Masukkan nama hewan: ")
            tanggal_penitipan = input("Masukkan tanggal penitipan: ")
            penitipan.create(nama, no_hp, alamat, hewan, nama_hewan, tanggal_penitipan)
        elif pilihan == '2':
            penitipan.read()
        elif pilihan == '3':
            nama = input("Masukkan nama pemilik untuk diperbarui datanya: ")
            no_hp = input("Masukkan nomor HP baru: ")
            alamat = input("Masukkan alamat baru: ")
            hewan = input("Masukkan jenis hewan baru: ")
            nama_hewan = input("Masukkan nama hewan baru: ")
            tanggal_penitipan = input("Masukkan tanggal penitipan baru: ")
            if penitipan.update(nama, no_hp, alamat, hewan, nama_hewan, tanggal_penitipan):
                print("===========================================================")
                print("           DATA PENITIPAN BERHASIL DIPERBARUI.             ")
                print("                      (´｡• ◡ •｡`)                           ")
                print("===========================================================")
            else:
                print("===========================================================")
                print("                DATA TIDAK DITEMUKAN.                      ")
                print("                      ( • ᴖ • ｡)                           ")
                print("===========================================================")
        elif pilihan == '4':
            nama = input("Masukkan nama pemilik untuk menghapus data: ")
            penitipan.delete(nama)
        elif pilihan == '5':
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()