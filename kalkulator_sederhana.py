jawab = "y"
while (jawab=="y"):
	print("==================================================================")
	print("|||||||||||||||  PROGRAM KALKULATOR SEDERHANA  |||||||||||||||||||")
	print("==================================================================")
	print("                     >>>>MENU PROGRAM<<<<")
	print("                                   				 ")
	print("1. menghitung luas segitiga                ")
	print("2. menghitung luas lingkaran               ")
	print("3. menghitung luas bujur sangkar           ")
	print("")
	A = int(input("pilih menu : "))
	a = (A)
	b = (A)
	c = (A)
	if a==1:
		a1 = int(input("    ketikan alas segitiga:    "))
		a2 = int(input("  ketikan tinggi segitiga:    "))
		print("-------------------------------------  ")
		luas = (a1 * a2) / 2
		print("                     luas: ",luas)
	elif b==2:
		b1 = int(input("ketikan jari-jari lingkaran:    "))
		print("-------------------------------------  ")
		luas = 22 / 7 * (b1**2)
		print("                        luas: ",luas)
	elif c==3:
		c1 = int(input("ketikan sisi bujur sangkar:    "))
		luas = c1 ** 2
		print("-------------------------------------  ")
		print("                      luas: ",luas )
	
	jawab = input("apakah anda ingin mencoba lagi? y/n -")
	if jawab=="n":
		print("terimakasih sudah mencoba.")
	elif jawab!="y":
		print("input yang anda masukan salah.")
