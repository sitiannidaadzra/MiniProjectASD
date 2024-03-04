import os
os.system("cls")
from prettytable import PrettyTable

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambahDepan(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def tambahTengah(self, prev_node, data):
        if not prev_node:
            print("===========================================================")
            print("               NODE TIDAK ADA DALAM DAFTAR.                ")
            print("                      ( • ᴖ • ｡)                           ")
            print("===========================================================")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def tambahBelakang(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def hapusAwal(self):
        if self.head is None:
            print("===========================================================")
            print("         LINKED LIST KOSONG. TIDAK DAPAT MENGHAPUS         ")
            print("                      ( • ᴖ • ｡)                           ")
            print("===========================================================")
            return
        self.head = self.head.next

    def hapusTengah(self, prev_node):
        if prev_node is None or prev_node.next is None:
            print("===========================================================")
            print("                  NODE TIDAK DITEMUKAN.                    ")
            print("                      ( • ᴖ • ｡)                           ")
            print("===========================================================")
            return
        prev_node.next = prev_node.next.next

    def hapusAkhir(self):
        if self.head is None:
            print("===========================================================")
            print("         LINKED LIST KOSONG. TIDAK DAPAT MENGHAPUS         ")
            print("                      ( • ᴖ • ｡)                           ")
            print("===========================================================")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def hapus(self, key, posisi):
        if self.head is None:
            print("===========================================================")
            print("         LINKED LIST KOSONG. TIDAK DAPAT MENGHAPUS         ")
            print("                      ( • ᴖ • ｡)                           ")
            print("===========================================================")
            return

        if posisi == 'awal':
            if self.head.data['nama'] == key:
                self.head = self.head.next
                print(f"Data dengan nama '{key}' telah dihapus.")
                return

        prev_node = self.cariSebelum(key)

        if prev_node:
            if prev_node.next.data['nama'] == key:
                prev_node.next = prev_node.next.next
                print(f"Data dengan nama '{key}' telah dihapus.")
                return
        else:
            current = self.head
            while current.next:
                if current.next.data['nama'] == key and current.next.next is None:
                    current.next = None
                    print(f"Data dengan nama '{key}' telah dihapus.")
                    return
                current = current.next

        print(f"Data dengan nama '{key}' tidak ditemukan.")

    def cariSebelum(self, key):
        current = self.head
        if current is None:
            return None
        if current.data['nama'] == key:
            return None
        while current.next is not None:
            if current.next.data['nama'] == key:
                return current
            current = current.next
        return None

class Penitipan:
    def __init__(self, nama, no_hp, alamat, jenis_hewan, nama_hewan, tanggal_penitipan):
        self.nama = nama
        self.no_hp = no_hp
        self.alamat = alamat
        self.jenis_hewan = jenis_hewan
        self.nama_hewan = nama_hewan
        self.tanggal_penitipan = tanggal_penitipan

class PenitipanHewan:
    def __init__(self):
        self.data_penitipan = LinkedList()

    def tambah(self, nama, no_hp, alamat, jenis_hewan, nama_hewan, tanggal_penitipan, posisi='akhir'):
        data = {
            'nama': nama,
            'no hp': no_hp,
            'alamat': alamat,
            'jenis hewan': jenis_hewan,
            'nama hewan': nama_hewan,
            'tanggal penitipan': tanggal_penitipan
        }
        if posisi == 'awal':
            self.data_penitipan.tambahDepan(data)
        elif posisi == 'akhir':
            self.data_penitipan.tambahBelakang(data)
        else:
            temp = self.data_penitipan.head
            while temp:
                if temp.data['nama'] == posisi:
                    break
                temp = temp.next
            self.data_penitipan.tambahTengah(temp, data)
        print("===========================================================")
        print("        DATA PENITIPAN HEWAN BERHASIL DITAMBAHKAN.         ")
        print("                     (´｡• ◡ •｡`)                            ")
        print("===========================================================")

    def hapus_awal(self):
        self.data_penitipan.hapusAwal()

    def hapus_akhir(self):
        self.data_penitipan.hapusAkhir()

    def hapus(self, nama, posisi):
        self.data_penitipan.hapus(nama, posisi)

    def lihat(self):
        if self.data_penitipan.head:
            table = PrettyTable()
            table.field_names = ["Nama Pemilik", "Nomor HP", "Alamat", "Jenis Hewan", "Nama Hewan", "Tanggal Penitipan"]
            temp = self.data_penitipan.head
            while temp:
                data = temp.data
                table.add_row([data['nama'], data['no hp'], data['alamat'], data['jenis hewan'], data['nama hewan'], data['tanggal penitipan']])
                temp = temp.next
            print(table)
        else:
            print("===========================================================")
            print("         TIDAK ADA DATA PENITIPAN YANG TERSEDIA.           ")
            print("                      ( • ᴖ • ｡)                           ")
            print("===========================================================")

    def perbarui(self, nama, no_hp_baru, alamat_baru, jenis_hewan_baru, nama_hewan_baru, tanggal_penitipan_baru):
        temp = self.data_penitipan.head
        while temp:
            if temp.data['nama'] == nama:
                temp.data['no hp'] = no_hp_baru
                temp.data['alamat'] = alamat_baru
                temp.data['jenis hewan'] = jenis_hewan_baru
                temp.data['nama hewan'] = nama_hewan_baru
                temp.data['tanggal penitipan'] = tanggal_penitipan_baru
                return True
            temp = temp.next
        return False

def hapus_data(penitipan):
    print("Pilih posisi penghapusan:")
    print("1. Di awal")
    print("2. Di tengah")
    print("3. Di akhir")
    posisi = input("Masukkan pilihan Anda: ")

    if posisi == '1':
        penitipan.hapus_awal()
    elif posisi == '2':
        nama = input("Masukkan nama pemilik untuk menghapus data: ")
        penitipan.hapus(nama, posisi='tengah')
    elif posisi == '3':
        penitipan.hapus_akhir()
    else:
        print("Pilihan tidak valid. Kembali ke menu utama.")
        return

def main():
    penitipan = PenitipanHewan()

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
        print("|                   (˵ •̀ ᴗ •́ ˵ ) ✧                        |")
        print("===========================================================")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            print("===========================================================")
            print("|                Pilih posisi perubahan:                  |")
            print("===========================================================")
            print("| 1. Tambahkan di awal                                    |")
            print("| 2. Tambahkan di tengah                                  |")
            print("| 3. Tambahkan di akhir                                   |")
            print("===========================================================")
            print("|                         ˶ᵔ ᵕ ᵔ˶                         |")
            print("===========================================================")
            posisi = input("Masukkan pilihan Anda: ")
            if posisi == '1':
                position = 'awal'
            elif posisi == '2':
                position = input("Masukkan nama setelah pemilik untuk menambahkan data: ")
                position = 'akhir'
            elif posisi == '3':
                position = 'akhir'
            else:
                print("Pilihan tidak valid. Kembali ke menu utama.")
                continue
            nama = input("Masukkan nama pemilik: ")
            no_hp = input("Masukkan nomor HP: ")
            alamat = input("Masukkan alamat: ")
            hewan = input("Masukkan jenis hewan: ")
            nama_hewan = input("Masukkan nama hewan: ")
            tanggal_penitipan = input("Masukkan tanggal penitipan: ")
            penitipan.tambah(nama, no_hp, alamat, hewan, nama_hewan, tanggal_penitipan, position)
        elif pilihan == '2':
            penitipan.lihat()
        elif pilihan == '3':
            nama = input("Masukkan nama pemilik untuk diperbarui datanya: ")
            no_hp = input("Masukkan nomor HP baru: ")
            alamat = input("Masukkan alamat baru: ")
            hewan = input("Masukkan jenis hewan baru: ")
            nama_hewan = input("Masukkan nama hewan baru: ")
            tanggal_penitipan = input("Masukkan tanggal penitipan baru: ")
            if penitipan.perbarui(nama, no_hp, alamat, hewan, nama_hewan, tanggal_penitipan):
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
            hapus_data(penitipan)
        elif pilihan == '5':
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()