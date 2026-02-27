# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================
def pangkat(a, n):
    # Base case
    if n == 0: 
        return 1 # Jika nilai n sudah sama dengan 0 maka program akan mengembalikan nilai 1
    # Recursive case
    return a * pangkat(a, n - 1) #  Mengalikan a dengan hasil fungsi pangkat(a, n-1) sampai n menjadi 0
print(pangkat(2, 4)) # Output: 16

# alur kerja
# pangkat(2, 4) mengembalikan 2 * pangkat(2, 3)
# pangkat(2, 3) mengembalikan 2 * pangkat(2, 2)
# pangkat(2, 2) mengembalikan 2 * pangkat(2, 1)
# pangkat(2, 1) mengembalikan 2 * pangkat(2, 0)
# pangkat(2, 0) mencapai base case, mengembalikan 1.

# Proses Kalkulasi Balik:
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 4 = 8
# 2 * 8 = 16 (Hasil Akhir)