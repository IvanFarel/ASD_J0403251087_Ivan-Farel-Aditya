# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================
def countdown(n):
    # Base Case
    if n == 0:
        print("Selesai") # Program akan mencetak 'selesai' saat n sudah 0
        return
    print("Masuk:", n) # Mencetak "Masuk:" diikuti nilai n.
    countdown(n - 1) # Pemanggilan rekursif fungsi countdown dengan n - 1, menurunkan nilai hingga mencapai Base Case.
    print("Keluar:", n) # Setelah pemanggilan rekursif selesai (kembali dari level lebih dalam), mencetak "Keluar:" dan nilai n.
countdown(3)
