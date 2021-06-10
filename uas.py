print("Program Kasir Sederhana Kantin Elektro USU")

pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

total1=0
jenis1=""
porsi=0
gelas=0

def fungsimakanan():
   global total1
   global porsi
   global jenis1
   print ("\n----Menu Makanan----")
   print("1. Mie goreng - Rp15000")
   print("2. Sop - Rp9000")
   print("3. Mie Ayam - Rp10000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       total1=porsi*15000
       print (porsi," porsi Mie goreng Telur = Rp", total1)
       jenis1=("Mie goreng")
   elif nomor==2:
       total1=porsi*9000
       print (porsi," porsi Sop = Rp", total1)
       jenis1=("Sop")
   elif nomor==3:
       total1=porsi*11000
       print (porsi, " porsi Mie Ayam = Rp", total1)
       jenis1=("Mie Ayam")
   else:
      print("Anda salah pesan!")
      fungsimakanan()


fungsimakanan()

total2=0
jenis2=""

def fungsiminuman():
   global total2
   global jenis2
   global gelas
   print("\n----Menu Minuman----")
   print("1. Teh Manis Dingin - Rp5000")
   print("2. Jus jeruk - Rp8000")
   print("3. Kopi panas/dingin - Rp10000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       total2=gelas*2000
       print (gelas," Teh Manis Dingin = Rp", total2)
       jenis2=(" Gelas Teh Manis Dingin")
   elif nomor==2:
       total2=gelas*3500
       print (gelas, " Gelas Jus jeruk = Rp", total2)
       jenis2=("Jus jeruk")
   elif nomor==3:
       total2=gelas*4000
       print (gelas, " Gelas Kopi panas/dingin = Rp", total2)
       jenis2=("Kopi panas/dingin")
   else:
      print("Anda salah Pesan!")
      fungsiminuman()


fungsiminuman()
    
totalsemua=0
totalsemua=total1+total2
print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp."))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n===========================")
print("====S T R U K   B E L I====")
print("===========================")
print (" Nama         :",pembeli)
print (" Beli         :",porsi,jenis1,"-", total1)
print ("               ",gelas,jenis2,"-", total2)
print (" Tagihan      : Rp.",totalsemua)
print (" Uang         : Rp.",uang)
print (" Kembalian    : Rp.",kembalian)
print("===========================")
print("===========================")