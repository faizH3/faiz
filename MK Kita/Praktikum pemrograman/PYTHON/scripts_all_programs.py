while True:
	print('''
________kumpulan tugas
        ___ ___  __  ___ ___  _ _____
        |__||__||  || __ |__||_|| |  |
        |   |  \|__||___||  \| || |  |
                             semester 1________
MENU:
	1. konversi suhu derajat celcius-fahreinheit
	2. tugas notasi if
	3. mid semester
	0. exit
		''')

	menu = input("pilih menu:")
        if menu == 4:
                exit()
	elif menu == 1:
		x = "y" or "Y"
		while x=="y" or x=="Y":
			print("1. konversi derajat celcius-fahreinheit")
			C = input("input suhu derajat celcius: ")
			F = int(C) * 9/5 + 32
			print("%sC = %.2fF"%(C,F))
			x = input("ulangi lagi(y/n): ")
			if x=="n" or x=="N":
				break
			elif x=="y" or x=="Y":
				print("")
			else:
				exit()

	elif menu == 2:
		print("2. notasi if")
		x = "y" or "Y"
		while x=="y" or x=="Y":
			t = input("input format waktu 24 jam:")
			time = float(t)

			if time>=0 and time<=12:
				print("good morning")
			elif time>=13 and time<=16:
				print("good afternoon")
			elif time>=17 and time<=20:
				print("good evening")
			elif time>=21 and time<=24:
				print("good night")
			else:
				print("wrong input")
			x = input("ulangi lagi(y/n): ")
			if x=="n" or x=="N":
				break
			elif x=="y" or x=="Y":
				print("")
			else:
				print("input salah")

	elif menu == 3:
		print("3. mid semester")
		print('''
buat pengulangan dengan perintah while untuk menampilkan
bilangan 3,5,7,9,11,13,15,17,19

jawab
________________________________________________________
var1 = 3
while var1<=19:
    print(var1)
    var1=var1+2
________________________________________________________
output''')
		var1 = 3
		while var1<=19:
			print(var1)
			var1=var1+2
			print(var1)
