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
	A = input("pilih menu : ")
	a = (A)
	b = (A)
	c = (A)
	if a==1:
		a1 = input("    ketikan alas segitiga:    ")
		a2 = input("  ketikan tinggi segitiga:    ")
		print("-------------------------------------  ")
		luas = (a1 * a2) / 2
		print("                   luas: ",luas)
	elif b==2:
		b1 = input("ketikan jari-jari lingkaran:    ")
		print("-------------------------------------  ")
		luas = 22 / 7 * (b1**2)
		print("                     luas: ",luas)
	elif c==3:
		c1 = input("ketikan sisi bujur sangkar:    ")
		luas = c1 ** 2
		print("-------------------------------------  ")
		print("                    luas: ",luas )
	elif jawab > 3:
		print("input yang anda masukan tidak ada.")

	jawab = raw_input("apakah anda ingin mencoba lagi? y/n -")
	if jawab=="n":
		print("terimakasih sudah mencoba.")
	elif jawab!="y":
		print("input yang anda masukan salah.")
