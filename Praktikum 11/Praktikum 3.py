# ----------------------------------------
# Nama    : Ivan Farel Aditya
# NIM     : J0403251087
# Kelas   : TPL A2
# ----------------------------------------

def matrixToList(matrix):
    # Menghitung jumlah vertex dari ukuran matriks
    V = len(matrix)

    # Inisialisasi adjacency list sebagai dictionary kosong
    adj_list = {}

    # Proses konversi
    for i in range(V):
        tetangga = []
        for j in range(V):
            # Jika ada edge (nilai 1) antara node i dan j, tambahkan j ke daftar tetangga i
            if matrix[i][j] == 1:
                tetangga.append(j)
        
        # Simpan daftar tetangga untuk node i dalam adjacency list
        adj_list[i] = tetangga

    return adj_list

if __name__ == "__main__":
    # Adjacency Matrix yang diberikan dari soal
    matrix = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0]
    ]

    # Melakukan konversi dari adjacency matrix ke adjacency list
    hasil_adj_list = matrixToList(matrix)

    # Menampilkan hasil konversi
    print("Hasil Konversi ke Adjacency List:")
    for node, daftar_tetangga in hasil_adj_list.items():
        print(f"{node}: {daftar_tetangga}")