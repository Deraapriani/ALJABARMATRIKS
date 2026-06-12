def buat_matriks(data):
    if len(data) == 0:
        raise ValueError("Matriks tidak boleh kosong")

    kolom = len(data[0])

    for baris in data:
        if len(baris) != kolom:
            raise ValueError("Jumlah kolom harus sama")

    return data


def tampilkan_matriks(m):
    for baris in m:
        print(baris)


def perkalian_matriks(A, B):
    if len(A[0]) != len(B):
        print("Perkalian tidak dapat dilakukan")
        return None

    hasil = []

    for i in range(len(A)):
        baris_hasil = []

        for j in range(len(B[0])):
            total = 0

            for k in range(len(B)):
                total += A[i][k] * B[k][j]

            baris_hasil.append(total)

        hasil.append(baris_hasil)

    return hasil


def transpose_matriks(A):
    hasil = []

    for j in range(len(A[0])):
        baris_baru = []

        for i in range(len(A)):
            baris_baru.append(A[i][j])

        hasil.append(baris_baru)

    return hasil


def determinan_2x2(A):
    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]

    return (a * d) - (b * c)