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
    
    def quickSort(self, arr, key, descending=False):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = [x for x in arr[1:] if (x.data[key] < pivot.data[key]) ^ descending]
            greater = [x for x in arr[1:] if (x.data[key] >= pivot.data[key]) ^ descending]
            return self.quickSort(less, key, descending) + [pivot] + self.quickSort(greater, key, descending)
    
    def sort(self, key1, key2=None, descending1=False, descending2=False):
        if not self.head:
            print("===========================================================")
            print("                       LIST KOSONG.                        ")
            print("                        ( • ᴖ • ｡)                         ")
            print("===========================================================")
            return
        arr = []
        current = self.head
        while current:
            arr.append(current)
            current = current.next
        if key2:
            sorted_arr = self.quickSort(arr, key2, descending2)
        else:
            sorted_arr = arr
        sorted_arr = self.quickSort(sorted_arr, key1, descending1)
        self.head = sorted_arr[0]
        current = self.head
        for node in sorted_arr[1:]:
            current.next = node
            current = current.next
        current.next = None

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
    
    def hapus_awal(self):
        self.data_penitipan.hapusAwal()
    
    def hapus_akhir(self):
        self.data_penitipan.hapusAkhir()
    
    def hapus(self, nama, posisi):
        self.data_penitipan.hapus(nama, posisi)
    
    def hapus_data(penitipan):      
        print("===========================================================")
        print("|                Pilih posisi penghapusan:                |")
        print("===========================================================")
        print("| 1. Hapus di awal                                        |")
        print("| 2. Hapus di tengah                                      |")
        print("| 3. Hapus di akhir                                       |")
        print("===========================================================")
        print("|                         ˶ᵔ ᵕ ᵔ˶                         |")
        print("===========================================================")
        posisi = input("Masukkan pilihan Anda: ")
        
        if posisi == '1':
            penitipan.hapus_awal()
            print("===========================================================")
            print("        DATA PENITIPAN HEWAN BERHASIL DIHAPUS.             ")
            print("                     (´｡• ◡ •｡`)                            ")
            print("===========================================================")
        elif posisi == '2':
            nama = input("Masukkan nama pemilik untuk menghapus data: ")
            penitipan.hapus(nama, posisi='tengah')
            print("===========================================================")
            print("        DATA PENITIPAN HEWAN BERHASIL DIHAPUS.             ")
            print("                     (´｡• ◡ •｡`)                            ")
            print("===========================================================")
        elif posisi == '3':
            penitipan.hapus_akhir()
            print("===========================================================")
            print("        DATA PENITIPAN HEWAN BERHASIL DIHAPUS.             ")
            print("                     (´｡• ◡ •｡`)                            ")
            print("===========================================================")
        else:
            print("Pilihan tidak valid. Kembali ke menu utama.")
            return
    
    def sort_data_penitipan(self, key1, key2=None, descending1=False, descending2=False):
        if key2:
            self.data_penitipan.sort(key1, key2, descending1, descending2)
        else:
            self.data_penitipan.sort(key1, descending1=descending1)
            
    def pencarian_fibonacci(arr, x, key):
        n = len(arr)
        fibM_minus_2 = 0
        fibM_minus_1 = 1
        fibM = fibM_minus_1 + fibM_minus_2

        while (fibM < n):
            fibM_minus_2 = fibM_minus_1
            fibM_minus_1 = fibM
            fibM = fibM_minus_1 + fibM_minus_2

        offset = -1
        while (fibM > 1):
            i = min(offset + fibM_minus_2, n - 1)

            if arr[i].data[key] < x:
                fibM = fibM_minus_1
                fibM_minus_1 = fibM_minus_2
                fibM_minus_2 = fibM - fibM_minus_1
                offset = i

            elif arr[i].data[key] > x:
                fibM = fibM_minus_2
                fibM_minus_1 = fibM_minus_1 - fibM_minus_2
                fibM_minus_2 = fibM - fibM_minus_1

            else:
                return i

        if fibM_minus_1 and arr[offset + 1].data[key] == x:
            return offset + 1

        return -1

    def cari_pemilik(penitipan, nama):
        current = penitipan.data_penitipan.head
        while current:
            if current.data['nama'] == nama:
                return current
            current = current.next
        return None

    def cari_hewan(penitipan, jenis_hewan):
        current = penitipan.data_penitipan.head
        while current:
            if current.data['jenis hewan'] == jenis_hewan:
                return current
            current = current.next
        return None
    
def main():
    penitipan = PenitipanHewan()
    
    penitipan_data = [
        ('Nida', '081234986654', 'Jl. Pahlawan', 'Kucing', 'Cimeng', '28 Februari 2024'),
        ('Jio', '081294321106', 'Jl. Gatot Subroto', 'Anjing', 'Bobby', '01 Maret 2024'),
        ('Kael', '081145677849', 'Jl. Perjuangan', 'Kucing', 'Millie', '12 Maret 2024')
    ]
    
    for data in penitipan_data:
        penitipan.tambah(*data)
        
    while True:
        print("===========================================================")
        print("|            Sistem Pendataan Penitipan Hewan             |")
        print("===========================================================")
        print("| 1. Tambah Data Penitipan                                |")
        print("| 2. Tampilkan Data Penitipan                             |")
        print("| 3. Perbarui Data Penitipan                              |")
        print("| 4. Hapus Data Penitipan                                 |")
        print("| 5. Sorting Data Penitipan                               |")
        print("| 6. Cari Data Penitipan                                  |")
        print("| 8. Keluar                                               |")
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
            penitipan.hapus_data()
        elif pilihan == '5':
            print("============================================================")
            print("|                 Sorting Berdasarkan                      |")
            print("============================================================")
            print("| 1. Nama Pemilik Hewan                                    |")
            print("| 2. Jenis Hewan                                           |")
            print("============================================================")
            sorting_berdasarkan = input("Masukkan pilihan Anda: ")
            if sorting_berdasarkan == '1':
                print("===========================================================")
                print("|                 Pilih Jenis Sorting                     |")
                print("===========================================================")
                print("| 1. Ascending                                            |")
                print("| 2. Descending                                           |")
                print("===========================================================")
                jenis_sorting = input("Masukkan pilihan Anda: ")
                if jenis_sorting == '1':
                    penitipan.sort_data_penitipan('nama')
                    penitipan.lihat()
                elif jenis_sorting == '2':
                    penitipan.sort_data_penitipan('nama', descending1=True)
                    penitipan.lihat()
                else:
                    print("===========================================================")
                    print("        PILIHAN TIDAK VALID. KEMBALI KE MENU UTAMA.        ")
                    print("                      ( • ᴖ • ｡)                           ")
                    print("===========================================================")
                    
            elif sorting_berdasarkan == '2':
                print("===========================================================")
                print("|                 Pilih Jenis Sorting                     |")
                print("===========================================================")
                print("| 1. Ascending                                            |")
                print("| 2. Descending                                           |")
                print("===========================================================")
                jenis_sorting = input("Masukkan pilihan Anda: ")
                if jenis_sorting == '1':
                    penitipan.sort_data_penitipan('jenis hewan')
                    penitipan.lihat()
                elif jenis_sorting == '2':
                    penitipan.sort_data_penitipan('jenis hewan', descending1=True)
                    penitipan.lihat()
                else:
                    print("===========================================================")
                    print("        PILIHAN TIDAK VALID. KEMBALI KE MENU UTAMA.        ")
                    print("                      ( • ᴖ • ｡)                           ")
                    print("===========================================================")
            else:
                print("===========================================================")
                print("        PILIHAN TIDAK VALID. KEMBALI KE MENU UTAMA.        ")
                print("                      ( • ᴖ • ｡)                           ")
                print("===========================================================")
        elif pilihan == '6':
            print("===========================================================")
            print("|                Pilih Jenis Pencarian                     |")
            print("===========================================================")
            print("| 1. Cari berdasarkan nama pemilik                        |")
            print("| 2. Cari berdasarkan jenis hewan peliharaan              |")
            print("===========================================================")
            jenis_pencarian = input("Masukkan pilihan Anda: ")
                
            if jenis_pencarian == '1':
                nama_pemilik = input("Masukkan nama pemilik yang ingin dicari: ")
                pemilik = penitipan.cari_pemilik(nama_pemilik)  # Memanggil metode cari_pemilik menggunakan objek penitipan
                if pemilik:
                    print("===========================================================")
                    print("           DATA PEMILIK DITEMUKAN:                         ")
                    print("===========================================================")
                    penitipan.lihat()
                else:
                    print("===========================================================")
                    print("           DATA PEMILIK TIDAK DITEMUKAN.                   ")
                    print("===========================================================")
            elif jenis_pencarian == '2':
                jenis_hewan = input("Masukkan jenis hewan yang ingin dicari: ")
                hewan = penitipan.cari_hewan(jenis_hewan)  # Memanggil metode cari_hewan menggunakan objek penitipan
                if hewan:
                    print("===========================================================")
                    print("           DATA HEWAN DITEMUKAN:                           ")
                    print("===========================================================")
                    penitipan.lihat()
                else:
                    print("===========================================================")
                    print("           DATA HEWAN TIDAK DITEMUKAN.                     ")
                    print("===========================================================")
            else:
                print("===========================================================")
                print("         PILIHAN TIDAK VALID. SILAKAN COBA LAGI.          ")
                print("                      ( • ᴖ • ｡)                           ")
                print("===========================================================")
        elif pilihan == '7':
            print("Keluar dari program...")
            break
        else:
            print("===========================================================")
            print("         PILIHAN TIDAK VALID. SILAKAN COBA LAGI.          ")
            print("                      ( • ᴖ • ｡)                           ")
            print("===========================================================")

if __name__ == "__main__":
    main()
