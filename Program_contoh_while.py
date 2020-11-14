jawab="y"
while(jawab=="y"):
 print("=============================================")
 print("       PROGRAM CONTOH PENGGUNAAN WHILE")
 print("=============================================")
 print("")
 print("MENU PROGRAM")
 print("1. Menghitung luas segitiga")
 print("2. Menghitung luas lingkaran")
 A=input("pilih menu:")
 a=(A)
 b=(A)
 if a==1:
  a1=raw_input("ketikan alas segitiga:")
  a2=raw_input("ketikan tinggi segitiga:")
  Luas=(a1*a2)/2
  print("Luas=",Luas)
 elif b==2:
  b1=input("ketikan jari-jari lingkaran:")
  Luas=22/7*(b1**2)
  print("Luas=",Luas)
 jawab=raw_input("apakah anda ingin mengulangi lagi? y/n -")
 if jawab=="n":
  print("terimakasih sudah mencoba.")
  break
 elif jawab!="y":
  print("input yang anda masukan salah.")
