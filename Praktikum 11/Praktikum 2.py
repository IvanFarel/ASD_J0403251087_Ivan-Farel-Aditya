# ----------------------------------------
# Nama    : Ivan Farel Aditya
# NIM     : J0403251087
# Kelas   : TPL A2
# ----------------------------------------

def createGraph(V, edges):
    adj = [[] for _ in range(V)]
    
    # Memasukkan edge ke dalam adjacency list
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)

        # Karena graf tidak berarah, kita juga perlu menandai v ke u
        adj[v].append(u)
    return adj

if __name__ == "__main__":
    V = 4

    data = {
        0 : "A",
        1 : "B",
        2 : "C",
        3 : "D"
    }

    # Daftar edge dalam bentuk [u, v]
    edges = [[0, 1], [0, 2], [1, 3], [2, 3]]

    # Membuat adjacency list
    adj = createGraph(V, edges)

    print("Adjacency List:")
    for i in range(V):
        
        # Menampilkan vertex dan daftar tetangganya
        print(f"{data[i]}:", end=" ")
        for j in adj[i]:

            # Menampilkan tetangga dari vertex i
            print(data[j], end=" ")
        print()