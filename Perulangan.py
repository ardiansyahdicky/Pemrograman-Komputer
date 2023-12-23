#FUNGSI PERULANGAN (REVISI TUGAS 3)
print('Nama : Dicky Ardiansyah PP'.center(100))
print('NIU  : 483049'.center(100))
print()
print("Menghitung Indeks Massa Tubuh".center(100))
print()
def perhitungan(TB,BB):
    return BB/(a**2)

while True:
        TB=int(input("Masukkan tinggi badan(cm) :"))
        BB=int(input("Masukkan berat badan(kg) :"))
        a=TB/100
        IMT=BB/(a**2)
        print('IMT nya adalah',IMT)

        if IMT<18:
            print('Kurus')
        elif IMT<25:
            print('Normal')
        elif IMT<27:
            print('Kegemukan')
        elif IMT>27:
            print('Obesitas')
        else:
            print('Data masukan salah')

        stop=input('masukkan sembarang keyword untuk menghitung ulang atau \nketik 0 untuk menghentikan program:')
        if stop=='0':
            break
