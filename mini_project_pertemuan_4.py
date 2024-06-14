# Pewarna
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"

class Node_Scooter: #node yang dipake
    def __init__(self, id_scooter, nama_scooter):
        self.id_scooter = id_scooter
        self.nama_scooter = nama_scooter
        self.next = None

    def __str__(self): #buat output node biar ada keterangannya
        return f"ID: {self.id_scooter}, Nama Part Scooter: {self.nama_scooter}"
    
class Queue: #kelas buat antrian
    def __init__(self): #buat inisialisasi kelas queue
        self.items = []

    def enqueue(self, item): #penambahan antrian dari belakang
        self.items.append(item) #append buat menambahkan item

    def dequeue(self): #penghapusan antrian dari depan
        if not self.is_empty():
            return self.items.pop(0)

    def front(self): #buat penghapusan
        if not self.is_empty():
            return self.items[0]

    def is_empty(self): #kalo size nya 0
        return len(self.items) == 0 #buat hitung jumlah karakter

    def size(self): #buat melihat ukuran antrian
        return len(self.items)

class Stack: #kelas buat tumpukan
    def __init__(self): #buat inisialisasi kelas stack
        self.items = [] #buat naro data nya

    def push(self, item): #buat nambah item untuk stack
        self.items.append(item)

    def pop(self): #buat penghapusan item
        if not self.is_empty():
            return self.items.pop()

    def peek(self): #buat melihat data item terbaru stack
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self): #ukurean stack
        return len(self.items)

class LinkedList: #constructor buat linked list
    def __init__(self): #buat inisialisasi
        self.head = None #buat naro node nya
        self.histori_data = Stack() #buat nyimpen record data
        self.queue = Queue()  #buat data queue

    def ambil_data(self, ambil, data): #buat ambil record data
        self.histori_data.push((ambil, data))

    def tambah_di_awalan(self, id_scooter, nama_scooter):
        new_node = Node_Scooter(id_scooter, nama_scooter)
        new_node.next = self.head #Mengatur referensi next dari new_node agar menunjuk ke elemen yang saat ini menjadi head (self.head).
        self.head = new_node #Mengganti head dengan new_node, sehingga new_node menjadi elemen pertama dalam struktur data.
        self.ambil_data("menambah_di_awalan", (id_scooter, nama_scooter))
        self.queue.enqueue(new_node) #Menambahkan new_node ke dalam antrian (queue) yang mungkin ada dalam objek self.

    def tambah_di_akhiran(self, id_scooter, nama_scooter):
        new_node = Node_Scooter(id_scooter, nama_scooter)
        if not self.head:#Memeriksa apakah struktur data kosong (head belum ada).
            self.head = new_node
            self.ambil_data("menambah_di_akhiran", (id_scooter, nama_scooter))
            self.queue.enqueue(new_node)
            return
        current = self.head
        while current.next:#Melakukan perulangan selama current memiliki elemen berikutnya (tidak berada di akhir struktur data).
            current = current.next
        current.next = new_node
        self.ambil_data("menambah_di_akhiran", (id_scooter, nama_scooter))
        self.queue.enqueue(new_node)

    def tambah_di_antara_node(self, id_scooter, nama_scooter, posisi): #0 1 2 3 4 5
        if posisi < 0:
            print("Posisi penambahan di antara node tidak valid.")
            return
        new_node = Node_Scooter(id_scooter, nama_scooter)
        if posisi == 0:
            new_node.next = self.head#Jika iya, maka new_node akan menjadi head (elemen pertama) dalam struktur data.
            self.head = new_node
            self.ambil_data("menambah_di_awalan", (id_scooter, nama_scooter))
            self.queue.enqueue(new_node)
            return
        current = self.head
        for i in range(posisi - 1): #buat urutan angka
            if current:
                current = current.next#Pada setiap iterasi, pindahkan current ke elemen berikutnya (jika ada).
            else:
                print("Posisi penambahan di antara node tidak valid.")
                return
        if not current:
            print("Posisi penambahan di antara node tidak valid.")
            return
        new_node.next = current.next
        current.next = new_node
        self.ambil_data("menambah_di_antara_node", (id_scooter, nama_scooter, posisi))
        self.queue.enqueue(new_node)

    def dequeue(self): #penghapusan antrian dari depan
        if not self.queue.is_empty():
            return self.queue.dequeue()

    def tampilkan_hasil(self):
        current = self.head
        while current:
            print(BOLD + CYAN +"")
            print(current, end=" -> ")
            current = current.next
        print("takde")

    def quicksort_berdasarkan_id_ascending(self, head):
        if head is None or head.next is None:#Memeriksa apakah head adalah None atau hanya memiliki satu elemen.
            return head#Jika iya, kembalikan head tanpa melakukan pengurutan.

        pivot = head.id_scooter#Mengambil nilai atribut id_scooter dari head sebagai pivot (titik pemisah).
        left_head = left_tail = None#Variabel ini akan digunakan untuk menyimpan elemen-elemen yang lebih kecil dari pivot.
        equal_head = equal_tail = None#Variabel ini akan digunakan untuk menyimpan elemen-elemen yang sama dengan pivot.
        right_head = right_tail = None#Variabel ini akan digunakan untuk menyimpan elemen-elemen yang lebih besar dari pivot.

        current = head
        while current is not None:
            if current.id_scooter < pivot:#Jika current.id_scooter lebih kecil dari pivot, tambahkan current ke bagian kiri.
                if left_head is None:
                    left_head = left_tail = current
                else:
                    left_tail.next = current
                    left_tail = current
            elif current.id_scooter == pivot:#Jika current.id_scooter sama dengan pivot, tambahkan current ke bagian yang sama dengan pivot.
                if equal_head is None:
                    equal_head = equal_tail = current
                else:
                    equal_tail.next = current
                    equal_tail = current
            else:
                if right_head is None:#Jika current.id_scooter lebih besar dari pivot, tambahkan current ke bagian kanan.
                    right_head = right_tail = current
                else:
                    right_tail.next = current
                    right_tail = current
            current = current.next

        if left_tail:
            left_tail.next = None
        if right_tail:
            right_tail.next = None

        left_head = self.quicksort_berdasarkan_id_ascending(left_head)
        right_head = self.quicksort_berdasarkan_id_ascending(right_head)

        if left_head:
            head = left_head
            left_tail.next = equal_head
        else:
            head = equal_head

        if equal_tail:
            equal_tail.next = right_head
        else:
            head = right_head

        return head

    def quicksort_berdasarkan_id_descending(self, head):
        if head is None or head.next is None:
            return head

        pivot = head.id_scooter
        left_head = left_tail = None
        equal_head = equal_tail = None
        right_head = right_tail = None

        current = head
        while current is not None:
            if current.id_scooter > pivot:
                if left_head is None:
                    left_head = left_tail = current
                else:
                    left_tail.next = current
                    left_tail = current
            elif current.id_scooter == pivot:
                if equal_head is None:
                    equal_head = equal_tail = current
                else:
                    equal_tail.next = current
                    equal_tail = current
            else:
                if right_head is None:
                    right_head = right_tail = current
                else:
                    right_tail.next = current
                    right_tail = current
            current = current.next

        if left_tail:
            left_tail.next = None
        if right_tail:
            right_tail.next = None

        left_head = self.quicksort_berdasarkan_id_descending(left_head)
        right_head = self.quicksort_berdasarkan_id_descending(right_head)

        if left_head:
            head = left_head
            left_tail.next = equal_head
        else:
            head = equal_head

        if equal_tail:
            equal_tail.next = right_head
        else:
            head = right_head

        return head

    def quicksort_berdasarkan_nama_ascending(self, head):
        if head is None or head.next is None:
            return head

        pivot = head.nama_scooter
        left_head = left_tail = None
        equal_head = equal_tail = None
        right_head = right_tail = None

        current = head
        while current is not None:
            if current.nama_scooter < pivot:
                if left_head is None:
                    left_head = left_tail = current
                else:
                    left_tail.next = current
                    left_tail = current
            elif current.nama_scooter == pivot:
                if equal_head is None:
                    equal_head = equal_tail = current
                else:
                    equal_tail.next = current
                    equal_tail = current
            else:
                if right_head is None:
                    right_head = right_tail = current
                else:
                    right_tail.next = current
                    right_tail = current
            current = current.next

        if left_tail:
            left_tail.next = None
        if right_tail:
            right_tail.next = None

        left_head = self.quicksort_berdasarkan_nama_ascending(left_head)
        right_head = self.quicksort_berdasarkan_nama_ascending(right_head)

        if left_head:
            head = left_head
            left_tail.next = equal_head
        else:
            head = equal_head

        if equal_tail:
            equal_tail.next = right_head
        else:
            head = right_head

        return head

    def quicksort_berdasarkan_nama_descending(self, head):
        if head is None or head.next is None:
            return head

        pivot = head.nama_scooter
        left_head = left_tail = None
        equal_head = equal_tail = None
        right_head = right_tail = None

        current = head
        while current is not None:
            if current.nama_scooter > pivot:
                if left_head is None:
                    left_head = left_tail = current
                else:
                    left_tail.next = current
                    left_tail = current
            elif current.nama_scooter == pivot:
                if equal_head is None:
                    equal_head = equal_tail = current
                else:
                    equal_tail.next = current
                    equal_tail = current
            else:
                if right_head is None:
                    right_head = right_tail = current
                else:
                    right_tail.next = current
                    right_tail = current
            current = current.next

        if left_tail:
            left_tail.next = None
        if right_tail:
            right_tail.next = None

        left_head = self.quicksort_berdasarkan_nama_descending(left_head)
        right_head = self.quicksort_berdasarkan_nama_descending(right_head)

        if left_head:
            head = left_head
            left_tail.next = equal_head
        else:
            head = equal_head

        if equal_tail:
            equal_tail.next = right_head
        else:
            head = right_head

        return head

    def fibonaci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonaci(n-1) + self.fibonaci(n-2)

    def tampilkan_histori_data(linked_list):
        print(BOLD + YELLOW + "Record Data:" + RESET)
        while not linked_list.histori_data.is_empty():
            ambil, data = linked_list.histori_data.pop()
            print(BOLD + CYAN + "")
            print(f"{ambil}: {data}")


    def hapus_node(self, id_scooter):
        if not self.head:#Memeriksa apakah struktur data kosong (head belum ada).
            print("kosong cuy")
            return

        if self.head.id_scooter == id_scooter:
            self.head = self.head.next
            self.ambil_data("hapus_node", id_scooter)
            return

        prev = None
        current = self.head
        while current:
            if current.id_scooter == id_scooter:#Jika current.id_scooter sama dengan id_scooter, hubungkan prev dengan elemen berikutnya (current.next) untuk menghapus current.
                prev.next = current.next
                self.ambil_data("hapus_node", id_scooter)
                return
            prev = current
            current = current.next
        print(f"Tidak ada node dengan ID {id_scooter}.")

try:
    def tambah_di_awalan(linked_list):
        id_scooter = int(input(BOLD + PURPLE + "Masukkan ID Part Scooter: "))
        nama_scooter = input("Masukkan Nama Part Scooter: ")
        linked_list.tambah_di_awalan(id_scooter, nama_scooter)
        print("Part Scooter berhasil ditambah di awalan.")

    def tambah_di_akhiran(linked_list):
        id_scooter = int(input( BOLD + PURPLE + "Masukkan ID Part Scooter: "))
        nama_scooter = input("Masukkan Nama Part Scooter: ")
        linked_list.tambah_di_akhiran(id_scooter, nama_scooter)
        print("Part Scooter berhasil ditambah di akhiran.")

    def tambah_di_antara(linked_list):
        id_scooter = int(input( BOLD + PURPLE + "Masukkan ID Part Scooter yang ingin ditambahkan: "))
        nama_scooter = input("Masukkan Nama Part Scooter yang ingin ditambahkan: ")
        posisi = int(input("Masukkan posisi penambahan (indeks nya) di antara node: "))
        linked_list.tambah_di_antara_node(id_scooter, nama_scooter, posisi)
        print("Part Scooter berhasil ditambah di antara node.")

    def hapus_part(linked_list):
        id_scooter = int(input(BOLD + PURPLE + "Masukkan ID Part Scooter yang ingin dihapus: "))
        linked_list.hapus_node(id_scooter)
        print("Part Scooter berhasil dihapus.")

    def urutkan_asc_id(linked_list):
        linked_list.head = linked_list.quicksort_berdasarkan_id_ascending(linked_list.head)
        print("Part Scooter berhasil diurutkan berdasarkan ID.")

    def urutkan_desc_id(linked_list):
        linked_list.head = linked_list.quicksort_berdasarkan_id_descending(linked_list.head)
        print("Part Scooter berhasil diurutkan berdasarkan ID.")

    def urutkan_asc_nama(linked_list):
        linked_list.head = linked_list.quicksort_berdasarkan_nama_ascending(linked_list.head)
        print("Part Scooter berhasil diurutkan berdasarkan nama.")

    def urutkan_desc_nama(linked_list):
        linked_list.head = linked_list.quicksort_berdasarkan_nama_descending(linked_list.head)
        print("Part Scooter berhasil diurutkan berdasarkan nama.")

    def search_fibonaci_id(linked_list):
        target = int(input(BOLD + PURPLE + "Masukkan ID part scooter yang ingin dicari menggunakan metode fibonaci: "))
        current = linked_list.head
        count = 0 #untuk menghitung posisi elemen yang ditemukan.
        while current:
            if current.id_scooter == target:
                found = True
                break
            elif current.id_scooter < target: #Jika current.id_scooter lebih kecil dari target, tambahkan 1 ke count dan pindahkan current ke elemen berikutnya.
                count += 1
                current = current.next
            else:
                break
        if found:
            print(f"ID part scooter {target} ditemukan pada posisi {count} menggunakan fibonaci.")
        else:
            print(f"ID part scooter {target} tidak ditemukan.")

    def search_fibonaci_nama(linked_list):
        target = (input(BOLD + PURPLE + "Masukkan nama part Scooter yang ingin dicari menggunakan fibonaci: "))
        found = False
        current = linked_list.head
        count = 0
        while current:
            if current.nama_scooter == target:
                found = True
                break
            elif current.nama_scooter < target:
                count += 1
                current = current.next
            else:
                break
        if found:
            print(f"Nama part scooter {target} ditemukan pada posisi {count} menggunakan fibonaci.")
        else:
            print(f"Nama part scooter {target} tidak ditemukan.")
except KeyboardInterrupt:
    print("salah ketik")
except EOFError:
    print("salah ketik")
except ValueError:
    print("salah ketik")    

def fibonaci(self):
        current = self.head
        count = 0
        while current:
            current.id_scooter = self.fibonaci(count)
            count += 1
            current = current.next

def tampilkan_semua(linked_list):
    print(BOLD + YELLOW + "\nSemua Part Scooter:" + RESET)
    linked_list.tampilkan_hasil()

linked_list = LinkedList()

while True:
    try:
        print(BOLD + GREEN + """
        ======================
        = Nolimitz Maticshop =
        ======================
        """)
        print(BOLD + YELLOW + "============================================" + RESET)
        print(BOLD + CYAN + "1.  Tambah Part Scooter di awalan")
        print("2.  Tambah part scooter di akhiran")
        print("3.  Tambah part scooter di antaranya")
        print("4.  Hapus part Scooter")
        print("5.  Urutkan part Scooter berdasarkan id besar ke kecil")
        print("6.  Urutkan part scooter berdasarkan id kecil ke besar")
        print("7.  Urutkan part Scooter berdasarkan nama besar ke kecil")
        print("8.  Urutkan part scooter berdasarkan nama kecil ke besar")
        print("9.  Cari Part Scooter berdasarkan id dengan fibonacci")
        print("10. Cari Part Scooter berdasarkan nama dengan fibonacci")
        print("11. Tampilkan yang sudah terderet oleh fibonacci")
        print("12. Tampilkan semua")
        print("13. Tampilkan histori data")
        print("14. Keluar" + RESET)
        print(BOLD + YELLOW + "=============================================" + RESET)
        pilihan = input(BOLD + BLUE + "Masukkan pilihan Anda: " + RESET)

        if pilihan == '1':
            tambah_di_awalan(linked_list)
        elif pilihan == '2':
            tambah_di_akhiran(linked_list)
        elif pilihan == '3':
            tambah_di_antara(linked_list)
        elif pilihan == '4':
            hapus_part(linked_list)
        elif pilihan == '5':
            urutkan_asc_id(linked_list)
        elif pilihan == '6':
            urutkan_desc_id(linked_list)
        elif pilihan == '7':
            urutkan_asc_nama(linked_list)
        elif pilihan == '8':
            urutkan_desc_nama(linked_list)
        elif pilihan == '9':
            search_fibonaci_id(linked_list)
        elif pilihan == '10':
            search_fibonaci_nama(linked_list)
        elif pilihan == '11':
            fibonaci(linked_list)
            urutkan_asc_id(linked_list)
        elif pilihan == '12':
            tampilkan_semua(linked_list)
        elif pilihan == '13':
            linked_list.tampilkan_histori_data()
        elif pilihan == '14':
            print("uhuyy")
            break
        else:
            print("salah ketik")
    except KeyboardInterrupt:
        print("salah ketik")
    except EOFError:
        print("salah ketik")
    except ValueError:
        print("salah ketik") 

