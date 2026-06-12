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


def invers_matriks_2x2(A):
    det = determinan_2x2(A)

    if det == 0:
        print("Matriks tidak memiliki invers")
        return None

    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]

    hasil = [
        [d / det, -b / det],
        [-c / det, a / det]
    ]

    return hasil


def determinan_3x3(A):
    diagonal1 = A[0][0] * A[1][1] * A[2][2]
    diagonal2 = A[0][1] * A[1][2] * A[2][0]
    diagonal3 = A[0][2] * A[1][0] * A[2][1]

    diagonal4 = A[0][2] * A[1][1] * A[2][0]
    diagonal5 = A[0][0] * A[1][2] * A[2][1]
    diagonal6 = A[0][1] * A[1][0] * A[2][2]

    return (diagonal1 + diagonal2 + diagonal3) - (diagonal4 + diagonal5 + diagonal6)


def invers_matriks_3x3(A):
    det = determinan_3x3(A)

    if det == 0:
        print("Matriks tidak memiliki invers")
        return None

    k11 = A[1][1] * A[2][2] - A[1][2] * A[2][1]
    k12 = -(A[1][0] * A[2][2] - A[1][2] * A[2][0])
    k13 = A[1][0] * A[2][1] - A[1][1] * A[2][0]

    k21 = -(A[0][1] * A[2][2] - A[0][2] * A[2][1])
    k22 = A[0][0] * A[2][2] - A[0][2] * A[2][0]
    k23 = -(A[0][0] * A[2][1] - A[0][1] * A[2][0])

    k31 = A[0][1] * A[1][2] - A[0][2] * A[1][1]
    k32 = -(A[0][0] * A[1][2] - A[0][2] * A[1][0])
    k33 = A[0][0] * A[1][1] - A[0][1] * A[1][0]

    kofaktor = [
        [k11, k12, k13],
        [k21, k22, k23],
        [k31, k32, k33]
    ]

    adjoin = []

    for i in range(3):
        baris = []

        for j in range(3):
            baris.append(kofaktor[j][i])

        adjoin.append(baris)

    invers = []

    for i in range(3):
        baris = []

        for j in range(3):
            baris.append(adjoin[i][j] / det)

        invers.append(baris)

    return invers