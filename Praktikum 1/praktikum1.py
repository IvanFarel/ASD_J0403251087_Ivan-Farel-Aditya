#=======================================================================
#Praktikum 1 : Konsep ADT dan file handling
#Latihan Dasar 1 : Mmebaca seluruh isi file data
#=======================================================================

print("")
print("=====Membuka File Dalam Satu String=====")

with open("data_mahasiswa.txt", "r", encoding ="utf-8" ) as file:
    isi_file = file.read()
print(isi_file)
print("Tipe Data : ", type(isi_file))

#=======================================================================
#Praktikum 1 : Konsep ADT dan file handling
#Latihan Dasar 2 : Mmebaca seluruh isi file data dengan cara per baris
#=======================================================================

print("")
print("=====Membuka FIle per Baris=====")

jumlah_baris =  0 #inisialisasi variabel untuk menghitung jumlah baris
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #Gunakan .strip() untuk menghilangkan karakter baris baru
        print("Baris ke :",  jumlah_baris)
        print("isinya :", baris)

#Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom2 data
print("")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #Menghilangkan karakter baris baru
        nim, nama, nilai =baris.split(",") #Pecah menjadi data satuan dan simpan ke variabel
        print("| NIM :", nim, "| Nama :", nama,"| Nilai :",nilai)
        
#=======================================================================
#Praktikum 1 : Konsep ADT dan file handling
#Latihan Dasar 3 : Membaca data dan menyimpannya ke struktur data list
#=======================================================================

print("")
data_list = [] #inisialisasi list untuk menampung data

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #Menghilangkan karakter baris baru
        nim, nama, nilai =baris.split(",") #Pecah menjadi data satuan dan simpan ke variabel
        data_list.append([nim, nama, int(nilai)]) #Menyimpan data ke list
print("=====Menampilkan List=====")
print(data_list)
print("Contoh record ke 1", data_list[0])
print("Contoh record ke 2", data_list[1])
print("Jumlah record ;", len(data_list))

#=======================================================================
#Praktikum 1 : Konsep ADT dan file handling
#Latihan Dasar 4 : Membaca dan menyimpannya ke dalam struktur Data Dictionary
#=======================================================================

print("")
data_dict = {} #inisialisasi dictionary

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #Menghilangkan karakter baris baru
        nim, nama, nilai =baris.split(",") #Pecah menjadi data satuan dan simpan ke variabel
        #simpan data ke dalam dictionary
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
print("=====Menampilkan Data Dictionary=====")
print(data_dict)