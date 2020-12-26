# Origin Master
﻿import math

while True:
        print("v1.0.0")
        print("=================================================================")
        print("|||||||||||||||||PROGRAM KALKULATOR SEDERHANA||||||||||||||||||||")
        print("|>_____________________________________________________________<|")
        print("[>>>>>>>>>>>>>>>>>>>>>>> MENU PROGRAM <<<<<<<<<<<<<<<<<<<<<<<<<<]")
        print("=================================================================")
        print("|>+---+                                                        <|")
        print("|>| 1 | luas bangun datar                                      <|")
        print("|>+---+                                                        <|")
        print("|>| 2 | menghitung luas lingkaran                              <|")
        print("|>+---+                                                        <|")
        print("|>| 3 | menghitung deret luas bujur sangkar + kalkulus         <|")
        print("|>+---+                                                        <|")
        print("|>| 4 | menghitung luas persegi panjang                        <|")
        print("|>+---+                                                        <|")
        print("|>| 5 | limit fungsi                                           <|")
        print("|>+---+                                                        <|")
        print("|>| 0 | exit                                                   <|")
        print("|>+---+                                                        <|")
        print("|>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|")
        print("|>_____________________________________________________________<|")
        print("")
        print(">>>>>>>>>>>>>>>>>>")
        menu = input("pilih menu: ")
        print(">>>>>>>>>>>>>>>>>>")

        if menu=="1":
            while True:
                print("|>_____________________________________________________________<|")
                print("|>+---+                                                        <|")
                print("|>| 1 | luas bangun datar                                      <|")
                print("|>+---+                                                        <|")
                print("|>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|")
                print("menu")
                print("1. luas segitiga")
                print("2. luas persegi panjang")
                print("3. luas persegi")
                print("4. luas lingkaran")
                print("5. luas trapesium")
                print("6. luas jajar genjang")
                print("0. back")
                print('00. exit')
                a = input("pilih menu: ")
                if a=="0":
                    break
                elif a=='00':
                    exit()
                elif a=="1":
                    while True:
                        print("\nluas segitiga: \n1. luas \n2. alas \n3. tinggi")
                        a = input("ditanya: ")
                        if a=="1": #luas
                            print("\ndiketahui:")
                            aa1 = float(input("alas: "))
                            aa2 = float(input("tinggi: "))
                            print("\n       %.1fx%.1f"%(aa1,aa2))	
                            print("luas = ------- = %s"%(aa1*aa2/2))
                            print("          2")
                        elif a=="2": #alas
                            ab1 = float(input("luas: "))
                            ab2 = float(input("tinggi: "))
                            print("        %sx2"%(ab1))
                            print("alas = ------- = %s"%(ab1*2/ab2))
                            print("          %s"%(ab2))
                        elif a=="3": #tinggi
                            ac1 = float(input("luas: "))
                            ac2 = float(input("alas: "))
                            print("          %sx2"%(ac1))
                            print("tinggi = ------- = %.2f"%(ac1*2/ac2))
                            print("            %s"%(ac2))
                            print("-----------------------------------------------------------------")
                        print('\n[yes|no|exit]')
                        a = input("ulangi lagi[y/n/x]: ")
                        if a=="n" or a=="N":
                            break
                        elif a=="y" or a=="Y":
                            print()
                        elif a=='x' or a=='X':
                            exit()
                elif a=="2":
                    while True:
                        print("\npersegi panjang:")
                        print("1. luas \n2. panjang \n3.lebar \n0. exit")
                        a = input("ditanya:")
                        if a=="0":
                            break
                        elif a=="1":
                           p = input("panjang: ")
                           l = input("lebar: ")
                           luas = int(p) * int(l)
                           print("luas = P x L")
                           print("luas = %s x %s"%(p,l))
                           print("luas = %s"%(luas))
                        elif a=="2":
                            L = input("luas: ")
                            l = input("lebar: ")
                            p = int(L) / int(l)
                            print("panjang = Luas / lebar")
                            print("panjang = %s / %s"%(L,l))
                            print("panjang = %s"%(p))
                        elif a=="3":
                            L = input("luas: ")
                            p =input("panjang: ")
                            l = int(L) / int(p)
                            print("lebar = luas / panjang")
                            print("lebar = %s / %s"%(L,p))
                            print("lebar = %s"%(l))
                        print('\n[yes|no|exit]')
                        a = input("ulangi lagi[y/n/x]: ")
                        if a=="n" or a=="N":
                            break
                        elif a=="y" or a=="Y":
                            print()
                        elif a=='x' or a=='X':
                            exit()
                                    
                elif a=='3':
                    while True:
                        print('\npersegi')

                        print('\n[yes|no|exit]')
                        a = input("ulangi lagi[y/n/x]: ")
                        if a=="n" or a=="N":
                            break
                        elif a=="y" or a=="Y":
                            print()
                        elif a=='x' or a=='X':
                            exit()
                elif a=='4':
                    while True:
                        print('\nluas lingkaran')

                        print('\n[yes|no|exit]')
                        a = input("ulangi lagi[y/n/x]: ")
                        if a=="n" or a=="N":
                            break
                        elif a=="y" or a=="Y":
                            print()
                        elif a=='x' or a=='X':
                            exit()
                elif a=='5':
                    while True:
                        print('\ntrapesium')

                        print('\n[yes|no|exit]')
                        a = input("ulangi lagi[y/n/x]: ")
                        if a=="n" or a=="N":
                            break
                        elif a=="y" or a=="Y":
                            print()
                        elif a=='x' or a=='X':
                            exit()
                elif a=='6':
                    while True:
                        print('\njajar genjang')

                        print('\n[yes|no|exit]')
                        a = input("ulangi lagi[y/n/x]: ")
                        if a=="n" or a=="N":
                            break
                        elif a=="y" or a=="Y":
                            print()
                        elif a=='x' or a=='X':
                            exit()
        elif menu=="2":
            while True:
                print("|>_____________________________________________________________<|")
                print("|>+---+                                                        <|")
                print("|>| 2 | menghitung luas lingkaran                              <|")
                print("|>+---+                                                        <|")
                print("|>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|")
                print("pilih diketahui")
                print("1. jari-jari")
                print("2. diameter")
                b1 = float(input("pilih menu: "))
                if b1=="1": #jari-jari
                    bb1 = input("jari-jari lingkaran: ")
                    luas = 22/7 * (float(bb1) ** 2)#luas lingkaran
                    a = float(bb1)**2
                    print("luas = 22/7x%s^2"%(bb1))#mengeluarkan penjabaran pertama
                    print("     = 22/7x%s"%(a))#mengeluarkan penjabaran kedua
                    print("     = %.2f"%(luas))#hasil
                elif b1=="2": #diameter
                    bc1 = input("ketikan diameter lingkaran: ")
                    luas = (float(22)/7)*(float((bc1)/2)**2) #luas lingkaran
                    print("luas  = 22/7x%s"+str("22/7x")+str(bc1)+str("/2"))#penjabaran
                    print("      = "+str("22/7x")+str(bc1/2)+str("^2"))#penjabaran
                    print("      = "+str(luas)) #hasil ouput
                    print("---------------------------------------------------------")
                print('\n[yes|no|exit]')
                a = input("ulangi lagi[y/n/x]: ")
                if a=="n" or a=="N":
                    break
                elif a=="y" or a=="Y":
                    print()
                elif a=='x' or a=='X':
                    exit()
        elif menu=="3": 
            while True:
                print("|>_____________________________________________________________<|")
                print("|>+---+                                                        <|")
                print("|>| 3 | menghitung deret luas bujur sangkar + kalkulus         <|")
                print("|>+---+                                                        <|")
                print("|>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|")
                c1 = float(input("sisi bujur sangkar pertama[1]:"))
                c2 = c1/2 #bujur sangkar ke-2 ==mencari sisi miring
                c_2 = c2**2
                c3 = (c2**2) + (c2**2)
                c4 = math.sqrt(c3)
                c5 = c4/2 #bujur sangkar ke-3 ==mencari sisi miring
                c_5 = c5**2
                c6 = (c5**2) + (c5**2)
                c7 = math.sqrt(c6)
                c8 = c1*c1 #luas bujur sangkar pertama
                c9 = (c4)*c4 #luas bujur sangkar kedua
                c10 = c7*c7 #luas bujur sangkar ketiga
                cr = c9/c8 #rasio
                c_r = 1-cr
                c11 = c8/(1-cr)#total luas
                print("luas [1]= %.2f x %.2f"%(c1,c1))
                print("luas [1]= %.2f"%(c8))
                print("")
                print("sisi [2]?")
                print("sisi [2] = sisi miring segitiga siku-siku sama kaki")
                print("A^2 = %.2f^2 + %.2f^2"%(c2,c2))
                print("A^2 = %.2f + %.2f"%(c_2,c_2))
                print("A   = %.2f^1/2"%(c3))
                print("A   = %.2f"%(c4))
                print("")
                print("sisi [2], %.2f"%(c4))
                print("luas [2] = %.2f x %.2f"%(c4,c4))
                print("luas [2] = %.2f"%(c9))
                print("")
                print("sisi [3]?")
                print("A^2 = %.2f^2 + %2.f^2"%(c5,c5))
                print("A^2 = %.2f + %.2f"%(c_5,c_5))
                print("A   = %.2f^1/2"%(c6))
                print("A   = %.2f"%(c7))
                print("")
                print("sisi [3],%.2f"%(c7))
                print("luas [3] = %.2f x %.2f"%(c7,c7))
                print("luas [3] = %.2f"%(c10))
                print("")
                print("rasio = %.2f / %s"%(c9,c8))
                print("      = %.2f"%(cr))
                print("")
                print("total luas[s] = %s / (1-%.2f)"%(c8,cr))
                print("              = %s / %.2f"%(c8,c_r))
                print("              = %.2f"%(c11))
                print("")
                print("luas bujur sangkar pertama:%.2f"%(c8))
                print("luas bujur sangkar kedua  :%.2f"%(c9))
                print("luas bujur sangkar ketiga :%.2f"%(c10))
                print("rasio                     :%.2f"%(cr))
                print("jumlah luas               :%.2f"%(c11))
                print("-----------------------------------------------------------------")

                print('\n[yes|no|exit]')
                a = input("ulangi lagi[y/n/x]: ")
                if a=="n" or a=="N":
                    break
                elif a=="y" or a=="Y":
                    print()
                elif a=='x' or a=='X':
                    exit()

        elif menu=="4":
            while True:
                print("|>_____________________________________________________________<|")
                print("|>+---+                                                        <|")
                print("|>| 4 | menghitung luas persegi panjang                        <|")
                print("|>+---+                                                        <|")
                print("|>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|")
                d1 = input("ketikan panjang persegi panjang: ")
                d2 = input("ketikan lebar persegi panjang:")
                luas = d1 * d2
                print("luas = "+str(d1)+str("*")+str(d2)+str("=")+str(luas))
                print("")
                print("---------------------------------------------------------------")
                print('\n[yes|no|exit]')
                a = input("ulangi lagi[y/n/x]: ")
                if a=="n" or a=="N":
                    break
                elif a=="y" or a=="Y":
                    print()
                elif a=='x' or a=='X':
                    exit()
        elif menu=="5":
                while True:
                    print("|>_____________________________________________________________<|")
                    print("|>+---+                                                        <|")
                    print("|>| 5 | limit fungsi                                           <|")
                    print("|>+---+                                                        <|")
                    print("|>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|")
                    print('\n[yes|no|exit]')
                    a = input("ulangi lagi[y/n/x]: ")
                    if a=="n" or a=="N":
                        break
                    elif a=="y" or a=="Y":
                        print()
                    elif a=='x' or a=='X':
                        exit()
        elif menu=="0":
                exit()
                
