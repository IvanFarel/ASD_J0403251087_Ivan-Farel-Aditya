#================================================================================
#Nama   : 
#NIM    :
#Kelas  :
#================================================================================

#================================================================================
#Implementasi Dasar : Stack
#================================================================================

class Node :
    #Kostruktor adlah fungsi yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note brikutnya (awal=None)

#Stack ada operasi push(memasukkan head baru) dan pop (menghapus head)

class stack :
    def __init__(self):
        self.top = None #Stop menunjuk ke node paling atas (awalnya kosong)

    def push(self,data):
        #! Mmebuat noode baru
        nodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class Node

        #2 node baru menunjuk ke tp yang lama (head lama)
        nodeBaru.next = self.top

        #3 geser too pindah ke node baru
        self.top = nodeBaru

    def is_empty(self):
        return self.top is None #stack kosong jika top = None

    def pop(self): #mengambil / menghapus node paling atas (top/head)

        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel (peek)
        self.top = self.top.next #geser top ke node beikutnya
        return data_terhapus

    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data

    def tampilkan(self):
        #Top -> A -> B
        current = self.top
        print ("Top ->" , end=" ")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

#Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
s.pop()
s.tampilkan()
print("Peek {Lihat Top}: ", s.peek())
s.pop()
s.tampilkan()
print("Peek {Lihat Top}: ", s.peek())