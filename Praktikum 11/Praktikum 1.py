# ----------------------------------------
# Nama    : Ivan Farel Aditya
# NIM     : J0403251087
# Kelas   : TPL A2
# ----------------------------------------

def createGraph(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]

    # Memasukkan edge ke dalam adjacency matrix
    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1

        # Karena graf tidak berarah, kita juga perlu menandai v ke u
        mat[v][u] = 1
    return mat

if __name__ == "__main__":
    V = 4

    # Daftar edge dalam bentuk [u, v]
    edges =[[0,1], [0, 2], [1, 2], [2, 3]]

    # Membuat adjacency matrix
    mat = createGraph(V, edges)

    print("Adjacency Matrix:")
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        print()

