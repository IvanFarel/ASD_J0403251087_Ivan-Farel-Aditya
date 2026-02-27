# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================
def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang: # Base case: jika panjang hasil sudah sesuai dengan panjang yang diinginkan, cetak hasil
        print("PIN:", hasil) # jika panjangnya sudah sesuai (3 digit), maka program akan mencetaknya (000, 001, dst...)
        return
    for angka in ["0", "1", "2"]:
        if angka not in hasil:
        # fungsi memanggil dirinya sendiri dan menambahkan 'angka' saat ini ke dalam string 'hasil', 
        # karena berada di dalam perulangan, pemanggilan ini akan menciptakan banyak cabang sekaligus
            buat_pin(panjang, hasil + angka)

buat_pin(3)
    
# Bagaimana cara mencegah angka yang sama muncul berulang?
# kita bisa menambahkan kode "if angka not in hasil:" setelah "for angka in ["0", "1", "2"]:"
# maka outputnya akan menjadi 012, 021, 102, 120, 201, 210