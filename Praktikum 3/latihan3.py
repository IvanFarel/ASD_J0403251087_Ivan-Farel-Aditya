class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Menyimpan node terakhir untuk traversing mundur
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    def display_forward(self):
        print("\nTraversing forward:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
    def display_backward(self):
        print("\nTraversing backward:")
        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("null")
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

elemen = input("\nMasukkan elemen ke dalam Doubly Linked List (pisahkan dengan koma): ").strip().split(",")
cari = int(input("Masukkan elemen yang ingin dicari: "))

dll = DoublyLinkedList()

#Memasukkan elemen ke dalam linked list
for i in elemen:
    dll.insert_at_end(int(i))
#Proses pencarian
if dll.search(cari):
    print(f"Elemen {cari} ditemukan dalam Doubly Linked List.")
else:
    print(f"Elemen {cari} tidak ditemukan dalam Doubly Linked List.")

