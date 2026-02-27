# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================
def cari_maks(data, index=0):
    # Base case 
    if index == len(data) - 1: # Jika index sudah mencapai elemen terakhir, kembalikan nilai tersebut
        return data[index]
    # Recursive case
    maks_sisa = cari_maks(data, index + 1) # Memanggil fungsi cari_maks untuk mencari nilai maksimum dari sisa list (dari index + 1 hingga akhir)
    if data[index] > maks_sisa: # jika angka saat ini lebih besar, maka angka ini menjadi nilai maksimum baru untuk digunakan ke bagian pengulangan berikutnya
        return data[index]
    else: 
        return maks_sisa # Jika angka saat ini lebih kecil atau sama, kembalikan nilai maksimum yang ditemukan di sisa list
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))