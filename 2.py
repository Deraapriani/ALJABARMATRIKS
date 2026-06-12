import dera051

A = dera051.buat_matriks([
    [5, 2],
    [3, 1]
])

B = dera051.buat_matriks([
    [4, 6],
    [2, 5]
])

print("Matriks A")
dera051.tampilkan_matriks(A)

print("\nMatriks B")
dera051.tampilkan_matriks(B)

print("\nHasil Perkalian A x B")
hasil = dera051.perkalian_matriks(A, B)
dera051.tampilkan_matriks(hasil)

print("\nTranspose Matriks A")
hasil_transpose = dera051.transpose_matriks(A)
dera051.tampilkan_matriks(hasil_transpose)

print("\nDeterminan Matriks A")
print(dera051.determinan_2x2(A))