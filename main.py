#Learning Print, Variable, Type Data

# Nama = "Elang"
# umur = 15
# cita_cita = "Software Developer"
# bahasa = "Python"

# print(Nama)
# print(umur)
# print(cita_cita)
# print(bahasa)

#Learning If & Else

# usia = 15
# nilai = 90.5

# if usia >= 15 and nilai >= 75:
#     print("Usia :", usia)
#     print("Nilai :", nilai)
#     print("Status : Eligible")
# else:
#     print("Usia :", usia)
#     print("Nilai :", nilai)
#     print("Status : Not Eligible")

# Learning Loop

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i, "Genap")
#     else:
#         print(i, "Ganjil")

# for i in range(1, 11):
#     print(i, "x", 5, "=", i * 5)

# for i in range(2, 8, 2):
#     print(i)

# List Structure

# siswa = ["Elang", "Budi", "Yudhistira"]

# print("Daftar Siswa :")

# siswa.append("Rizky")

# for nama in siswa:
#     print(nama)
    
# print("Jumlah Siswa :", len(siswa))

# Learning Function

# def perkenalan(nama, umur):
#     print("Nama:", nama)
#     print("Umur:", umur)

# perkenalan("Elang", 15)

def hitung_nilai(nama, nilai):
    print("Nama:", nama)
    print("Nilai:", nilai)

    if nilai >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"


status = hitung_nilai("Elang", 90)

print("status:", status)