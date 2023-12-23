Nama ="Dicky Ardiansyah PP"
NIU=483049
print("Nama:", Nama)
print("NIU:", NIU)
print()
bil1=int(input("masukkan angka pertama:"))
bil2=int(input("masukkan angka kedua:"))

#Pencarian angka terbesar dan terkecil
if bil1 > bil2:
    angka_terbesar=bil1
else:
    angka_terbesar=bil2

if bil1 < bil2:
    angka_terkecil=bil1
else:
    angka_terkecil=bil2
print("angka terbesar adalah", angka_terbesar)
print("angka terkecil adalah", angka_terkecil)

#Aritmatika
jumlah=bil1+bil2
kurang=bil1-bil2
kali=bil1*bil2
bagi=bil1/bil2
mod=bil1%bil2
pangkat=bil1**bil2
print()
print("hasil dari %d+%d=%d"%(bil1,bil2,jumlah))
print("hasil dari %d-%d=%d"%(bil1,bil2,kurang))
print("hasil dari %d*%d=%d"%(bil1,bil2,kali))
print("hasil dari %d/%d=%.1f"%(bil1,bil2,bagi))
print("hasil dari %dmod%d=%d"%(bil1,bil2,mod))
print("hasil dari %d**%d=%d"%(bil1,bil2,pangkat))
print()
print(Nama,"typenya adalah",type(Nama))
print(NIU,"typenya adalah",type(NIU))
print(bagi,"typenya adalah",type(bagi))
print()

#Fungsi perulangan
kunci_angka=int(input("masukkan angka selain 0:"))
max=0
while kunci_angka !=0:
    if kunci_angka>max:
        max=kunci_angka
    kunci_angka=int(input("masukkan angka selain 0:"))
print("angka terbesarnya yaitu",max)

#Fungsi if elif else
angka=int(input("masukkan angka ganjil dari pilihan 1,2,3,4,5,6:"))
if angka==1:
    print("data masukan benar")
elif angka==3:
    print("data masukan benar")
elif angka==5:
    print("data masukan benar")
else:
    print("data masukan salah")