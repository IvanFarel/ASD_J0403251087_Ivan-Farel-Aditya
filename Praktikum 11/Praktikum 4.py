# ----------------------------------------
# Nama    : Ivan Farel Aditya
# NIM     : J0403251087
# Kelas   : TPL A2
# ----------------------------------------

# Daftar node
nodes = ["Bogor", "Jakarta", "Bandung", "Sukabumi", "Cianjur"]

# Daftar edge
edges = [
    ("Bogor", "Jakarta"),
    ("Bogor", "Sukabumi"),
    ("Bogor", "Cianjur"),
    ("Jakarta", "Bandung"),
    ("Sukabumi", "Cianjur"),
    ("Cianjur", "Bandung")
]

# Membuat Adjacency List
graph = {}

# Membuat key untuk setiap node
for node in nodes:
    graph[node] = []

# Menambahkan hubungan antar node
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)


# Membuat Adjacency Matrix
# Jumlah vertex
V = len(nodes)

# Membuat index node
index = {}

for i in range(V):
    index[nodes[i]] = i

# Membuat matrix berisi 0
matrix = [[0 for column in range(V)]
          for row in range(V)]

# Mengisi matrix berdasarkan edge
for u, v in edges:
    i = index[u]
    j = index[v]
    matrix[i][j] = 1
    matrix[j][i] = 1


print("Node (Kota):")
for node in nodes:
    print("-", node)
print()


print("Edge (Jalan):")
for u, v in edges:
    print(u, "--", v)
print()


print("Adjacency List:")
for node in graph:
    print(node, "->", graph[node])
print()


print("Adjacency Matrix:")
for row in matrix:
    print(row)