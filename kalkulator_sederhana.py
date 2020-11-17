import math
jawab = "y"
while (jawab=="y"):
	print("v1.0.0")
	print("==========================================================")
	print("||||||||||||||PROGRAM KALKULATOR SEDERHANA||||||||||||||||")
	print("|>______________________________________________________<|")
	print("[>>>>>>>>>>>>>>>>>>>>MENU PROGRAM<<<<<<<<<<<<<<<<<<<<<<<<]")
	print("==========================================================")
	print("|>+---+                                                 <|")
	print("|>| 1 | MENGHITUNG rumus SEGITIGA                       <|")
	print("|>+---+                                                 <|")
	print("|>| 2 | MENGHITUNG LUAS LINGKARAN                       <|")
	print("|>+---+                                                 <|")
	print("|>| 3 | MENGHITUNG DERET BUJUR SANGKAR (KALKULUS)       <|")
	print("|>+---+                                                 <|")
	print("|>| 4 | MENGHITUNG LUAS PERSEGI PANJANG                 <|")
	print("|>+---+                                                 <|")
	print("|>| 5 | LIMIT FUNGSI                                    <|")
	print("|>+---+                                                 <|")
	print("|>| 6 | FUNGSI                                          <|")
	print("|>+---+                                                 <|")
	print("|>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|")
	print("|>______________________________________________________<|")
	print("")
	print(">>>>>>>>>>>>>>>>>>")
	A = input("pilih menu: ")
	print(">>>>>>>>>>>>>>>>>>")
	a = (A)
	b = (A)
	c = (A)
	d = (A)
	e = (A)
	f = (A)
	if a==1:
		T = "y"
		while(T=="y"):
			print("|>______________________________________________________<|")
			print("|>+---+                                                 <|")
			print("|>| 1 | menghitung rumus segitiga                       <|")
			print("|>+---+                                                 <|")
			print("|>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|")
			print("ditanya:")
			print("1. luas")
			print("2. alas")
			print("3. tinggi")
			a1 = input("pilih menu: ")
			aa = (a1)
			ab = (a1)
			ac = (a1)
			if aa==1: #luas
				aa1 = input("alas: ")
				aa2 = input("tinggi: ")
				luas = (aa1 * aa2) / 2	
				print("        "+str(aa1)+"x"+str(aa2))	
				print("luas = ------- = "+str(luas))
				print("          2")
			elif ab==2: #alas
				ab1 = input("luas: ")
				ab2 = input("tinggi: ")
				alas = (ab1 * 2) / ab2
				print("        "+str(ab1)+"x"+str("2"))
				print("alas = ------- = "+str(alas))
				print("          "+str(ab2))
			elif ac==3:
				ac1 = input("luas: ")
				ac2 = input("alas: ")
				tinggi = (ac1 * 2) / ac2
				print("        "+str(ac1)+str("x2"))
				print("tinggi = ------- = "+str(tinggi))
				print("          "+str(ac2))
			print("-----------------------------------------------------")
			T = raw_input("hitung lagi|yes|no|? y/n -")
			if T=="n":
				print("No!")
				print("")
				break
			elif T!="y":
				print("tidak cocok")
			elif T=="y":
				print("yes")
				print("")
	elif b==2:
		T = "y"
		while (T=="y"):
			print("|>______________________________________________________<|")
			print("|>+---+                                                 <|")
			print("|>| 2 | menghitung luas lingkaran                       <|")
			print("|>+---+                                                 <|")
			print("|>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|")
			print("pilih diketahui")
			print("1. jari-jari")
			print("2. diameter")
			b1 = input("pilih menu: ")
			bb = (b1)
			bc = (b1)
			if bb==1: #jari-jari
				bb1 = input("jari-jari lingkaran: ")
				luas = float(22)/7 * (bb1 ** 2)#luas lingkaran
				print("luas = "+str("22/7x")+str("(")+str(bb1)+str("^2")+str(")"))#mengeluarkan penjabaran pertama
				print("     = "+str("22/7x")+str(bb1**2))#mengeluarkan penjabaran kedua
				print("     = "+str(luas))#hasil output
			elif bc==2: #diameter
				bc1 = input("ketikan diameter lingkaran: ")
				luas = (float(22)/7)*(float((bc1)/2)**2) #luas lingkaran
				print("luas  = "+str("22/7x")+str(bc1)+str("/2"))#penjabaran
				print("      = "+str("22/7x")+str(bc1/2)+str("^2"))#penjabaran
				print("      = "+str(luas)) #hasil ouput
				print("------------------------------------------------------")
			T = raw_input("hitung lagi|yes|no|? y/n -")
			if T=="n":
				print("No!")
				print("")
				break
			elif T!="y":
				print("tidak cocok")
			elif T=="y":
				print("yes!")
				print("")
	elif c==3: 
		T = "y"
		while(T=="y"):
			print("|>______________________________________________________<|")
			print("|>+---+                                                 <|")
			print("|>| 3 | menghitung luas bujur sangkar + kalkulus        <|")
			print("|>+---+                                                 <|")
			print("|>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|")
			c1 = int(input("sisi bujur sangkar pertama[1]:"))
			c2 = c1/2 #bujur sangkar ke-2 ==mencari sisi miring
			c3 = (c2**2) + (c2**2)
			c4 = math.sqrt(c3)
			c5 = c4/2 #bujur sangkar ke-3 ==mencari sisi miring
			c6 = (c5**2) + (c5**2)
			c7 = math.sqrt(c6)
			c8 = c1*c1 #luas bujur sangkar pertama
			c9 = (c4)*c4 #luas bujur sangkar kedua
			c10 = c7*c7 #luas bujur sangkar ketiga
			cr = c9/c8 #rasio
			c11 = c8/(1-cr)#total luas
			print("luas [1]= "+str(c1)+" x "+str(c1))
			print("luas [1]= "+str(c8))
			print("")
			print("sisi [2]?")
			print("sisi [2] = sisi miring segitiga siku-siku sama kaki")
			print("A^2 = "+str(c2)+"^2 + "+str(c2)+"^2")
			print("A^2 = "+str(c2**2)+" + "+str(c2**2))
			print("A   = "+str(c3)+"^1/2")
			print("A   = "+str(c4))
			print("")
			print("sisi [2], "+str(c4))
			print("luas [2] = "+str(c4)+" x "+str(c4))
			print("luas [2] = "+str(c9))
			print("")
			print("sisi [3]?")
			print("A^2 = "+str(c5)+"^2 + "+str(c5)+"^2")
			print("A^2 = "+str(c5**2)+" + "+str(c5**2))
			print("A   = "+str(c6)+"^1/2")
			print("A   = "+str(c7))
			print("")
			print("sisi [3],"+str(c7))
			print("luas [3] = "+str(c7)+" x "+str(c7))
			print("luas [3] = "+str(c10))
			print("")
			print("rasio = "+str(c9)+"/"+str(c8))
			print("      = "+str(cr))
			print("")
			print("total luas[s] = "+str(c8)+"/(1-"+str(cr)+")")
			print("total luas[s] = "+str(c8)+"/"+str(1-cr)+")")
			print("total luas[s] = "+str(c11))
			print("")
			print("luas bujur sangkar pertama:"+str(c8))
			print("luas bujur sangkar kedua  :"+str(c9))
			print("luas bujur sangkar ketiga :"+str(c10))
			print("rasio                     :"+str(cr))
			print("jumlah luas               :"+str(c11))
			print("----------------------------------------------------------")
			T = raw_input("hitung lagi|yes|no|? y/n -")
			if T=="n":
				print("No!")
				print("")
				break
			elif T!="y":
				print("tidak cocok")
			elif T=="y":
				print("yes!")
				print("")

	elif d==4:
		T = "y"
		while(T=="y"):
			print("|>______________________________________________________<|")
			print("|>+---+                                                 <|")
			print("|>| 4 | menghitung luas persegi panjang                 <|")
			print("|>+---+                                                 <|")
			print("|>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|")
			d1 = input("ketikan panjang persegi panjang: ")
			d2 = input("ketikan lebar persegi panjang:")
			luas = d1 * d2
			print("luas = "+str(d1)+str("*")+str(d2)+str("=")+str(luas))
			print("")
			print("----------------------------------------------------------")
			T = raw_input("hitung lagi|yes|no|? y/n -")
			if T=="n":
				print("No!")
				print("")
				break
			elif T!="y":
				print("tidak cocok")
			elif T=="y":
				print("yes")
				print("")
	elif e==5:
		T = "y"
		while(T=="y"):
			print("|>______________________________________________________<|")
			print("|>+---+                                                 <|")
			print("|>| 5 | limit fungsi					                   <|")
			print("|>+---+                                                 <|")
			print("|>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|")
			print("menu:")
			print("                     ==============")
			print("=====================|coming soon!|=======================")
			print("|                    ==============                      |")
			print("+________________________________________________________+")
			print("+::::::::| |::||--|  =      /  |;;|| ____   _____;;;;;;;;|")
			print("|::::;;;;| |:;||--| | =    /   |;;||;;;;;| ;-- -- --  ---|")
			print("|::::::::| |::||--| |  =__/    |;;||;;;;;| ;- -- -- -----|")
			print("|::::::::|  ];|| -|__]       [ |;;||>>>>>| ;-  -----  ---|")
			print("+________________________________________________________|")
			T = raw_input("silahkan kembali! klik[n] -")
			if T=="n":
				break
	elif f==6:
		T = "y"
		while(T=="y"):
			print("|>______________________________________________________<|")
			print("|>+---+                                                 <|")
			print("|>| 6 | fungsi                                          <|")
			print("|>+---+                                                 <|")
			print("|>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|")
			print("menu:")
			print("1. fungsi linear")
			print("2. fungsi kuadrat")	
			f1 = input("pilih menu:")
			ff = (f1)
			fg = (f1)
			if ff==1:
				print("contoh:")
				print("y = ax + b, a=2 & b=3")
				print("y = 2x + 3")
				ff1 = input("a : ") #bisa negatif positif
				ff2 = input("b : ")
				ffa = ff2+(ff1*0) #rumus x=0, y = a(0)+b
				if ff2<0:
					print("misal, x = 0")
					print("y = "+str(ff1)+"x"+"+("+str(ff2)+")")
					print("  = "+str(ff1)+"(0)"+str(ff2))
					print("  = "+str(ffa))
				elif ff2>0:
					print("misal, x = 0")
					print("y = "+str(ff1)+"x + "+str(ff2))
					print("  = "+str(ff1)+"(0) + "+str(ff2))
					print("  = "+str(ff2))
				print("misal, y = 0")
				ff11 = input("a : ")
				ff21 = input("b : ")
				ffa1 = float(ff21)/ff11 #x = b+y /2
				
				if ff11<0:
					print("x = "+str(ff21)+"/"+str(ff11))
					print("  = "+str(ff21)+"/"+str(ff11))
					print("  = "+str(ffa1))
				elif ff21>0:
					print("x = "+str(ff21)+"/"+str(ff11))
					print("  = "+str(ffa1))
			elif fg==2:
				print("                     ==============")
				print("=====================|coming soon!|=======================")
				print("|                    ==============                      |")
				print("+________________________________________________________+")

			T = raw_input("hitung lagi|yes|no|? y/n -")
			if T=="n":
				print("No!")
				print("")
				break
			elif T!="y":
				print("tidak cocok")
			elif T=="y":
				print("yes!")
				print("")
	elif jawab>4:
		print("input yang anda masukan tidak ada.")
	jawab = raw_input("lanjut kemenu utama? y/n -")
	if jawab=="n":
		print("terimakasih sudah mencoba.")
	elif jawab!="y":
		print("input yang anda masukan salah.")