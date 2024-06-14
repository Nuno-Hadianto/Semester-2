class Node_Scooter:
    def __init__(self, nama_scooter):
        self.nama_scooter = nama_scooter
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def menambah_di_awalan(self, nama_scooter):
        new_node = Node_Scooter(nama_scooter)
        new_node.next = self.head
        self.head = new_node

    def menambah_di_akhiran(self, nama_scooter):
        new_node = Node_Scooter(nama_scooter)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def menambah_di_antara_node(self, nama_scooter, position):
        if position == 0:
            self.menambah_di_awalan(nama_scooter)
            return
        new_node = Node_Scooter(nama_scooter)
        current = self.head
        for _ in range(position - 1):
            if current:
                current = current.next
            else:
                print("posisi pemilihan diantara node tidak valdi.")
                return
        if not current:
            print("posisi pemilihan diantara node tidak valdi.")
            return
        new_node.next = current.next
        current.next = new_node

    def menghapus_node(self, nama_scooter):
        current = self.head
        if current and current.nama_scooter == nama_scooter:
            self.head = current.next
            return
        while current:
            if current.next and current.next.nama_scooter == nama_scooter:
                current.next = current.next.next
                return
            current = current.next
        print(f"Node dengan nama scooter {nama_scooter} tidak ada.")

    def display(self):
        current = self.head
        while current:
            print(current.nama_scooter, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()

#untuk menambahkan node di awal, di akhir sama sesuai posisi yang diinginkan diantara node tersebut
linked_list.menambah_di_awalan("Vario")
linked_list.menambah_di_akhiran("Aerox")
linked_list.menambah_di_akhiran("Mio Gear")
linked_list.menambah_di_antara_node("Beat", 10)#sesuai posisi 0 1 2 3 4 seterusnya
linked_list.display()

# Untuk menghapus node
linked_list.menghapus_node("mberr")#buat hapus yang diinginkan
linked_list.display()
