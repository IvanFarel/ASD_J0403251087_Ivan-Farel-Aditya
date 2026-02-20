##================================================================================
#Nama   : Ivan Farel Aditya
#NIM    : J0403251087
#Kelas  : TPL A2
#================================================================================

#================================================================================
#Implementasi Dasar : Noode pada Linked List
#================================================================================

class Node :
    #Konstrutor yang dijalankan secara otomatis ketika class node dipanggil / diinstalasi
    def __init__(self, data):
        self.data = data #menyimpan nilai aatu data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#1) membuat node dengan instantiasi class node
nodeA =  Node("A")
nodeB =  Node("B")
nodeC =  Node("C")

#2) Menghubungkan Node : A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3) Traversal : MENELUSURI NODE dari head sampai ke None
current = head
while current is not None :
    print(current.data) #menampilan data node saat ini
    current = current.next #pindah ke node selanjutnya




    
