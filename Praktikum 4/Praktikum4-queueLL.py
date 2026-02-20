#================================================================================
#Nama   : Ivan Farel Aditya
#NIM    : J0403251087
#Kelas  : TPL A2
#================================================================================


#================================================================================
#Implementasi Dasar : Stack
#================================================================================

class Node :
    #Kostruktor adlah fungsi yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note brikutnya (awal=None)

class queue:
    #buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node palng belakang
    
    def is_empty(self):
        return self.front is None

    #membuat fungsi untuk menambahkan data baru
    def enqueue(self,data):
        nodeBaru = Node(data)

        #jika queue kosong, front adn rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        #jika queue tidak kosong, maka letakkan data baru ke setelah rear, dan jadikan data baru sebagai rear
        self.rear.next = nodeBaru #Letakkan data baru pada setelahnya rear
        self.rear = nodeBaru #Jadikan data baru sebagai rear

    def dequeue(self):
        #menghapus data dari depan/front
        data_terhapus = self.front.data #Lihat data paliing depan
        
        #geser front ke node berikutnya
        self.front = self.front.next
        
        #Jika setelah geser front menjadi none maka queue kosong
        #rear juga harus jadi None
        if self.front is None:
            self.rear = None

        return data_terhapus

    def tampilkan(self):
        current = self.front
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end="->")
            current =current.next
        print ("Rear")

#Instantiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()


