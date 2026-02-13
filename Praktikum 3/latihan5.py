class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Tambahkan pointer 
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            self.tail = new_node # Tail juga menunjuk ke node pertama
        else:
            self.tail.next = new_node # Sambungkan tail ke node baru
            self.tail = new_node # Update tail ke node baru
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head  # Head lama akan menjadi tail baru
        
        while current:
            next_node = current.next  # Simpan node berikutnya
            current.next = prev      # Balik arah pointer
            prev = current           # Geser prev
            current = next_node      # Geser current
        self.head = prev  # Update head ke node terakhir

elemen = input("\nMasukkan elemen untuk Linked List (pisahkan dengan koma): ").strip().split(",")

ll = LinkedList()

# Memasukkan elemen ke dalam linked list
for i in elemen:
    ll.insert_at_end(int(i))

print("\nLinked List sebelum dibalik : ", end="")
ll.display()

ll.reverse()

print("Linked List setelah dibalik : ", end="")
ll.display()