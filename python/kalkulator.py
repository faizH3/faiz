import math
while True:
        print("v1.0.1")
        print("=================================================================")
        print("|||||||||||||||||PROGRAM KALKULATOR SEDERHANA||||||||||||||||||||")
        print("|>_____________________________________________________________<|")
        print("[>>>>>>>>>>>>>>>>>>>>>>> MENU PROGRAM <<<<<<<<<<<<<<<<<<<<<<<<<<]")
        print("=================================================================")
        print("|>+---+                                                        <|")
        print("|>| 1 | LUAS BANGUN DATAR                                      <|")
        print("|>+---+                                                        <|")
        print("|>| 2 | VOLUME                                                 <|")
        print("|>+---+                                                        <|")
        print("|>| 3 | MENGHITUNG DERET LUAS BUJUR SANGKAR(KALKULUS)          <|")
        print("|>+---+                                                        <|")
        print("|>| 4 | KALKULUS                                               <|")
        print("|>+---+                                                        <|")
        print("|>| 5 | ?????                                                  <|")
        print("|>+---+                                                        <|")
        print("|>| 6 | ?????                                                  <|")
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
                        print("pilih diketahui")
                        print("1. jari-jari")
                        print("2. diameter")
                        b1 = input("pilih menu: ")
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
                print("|>| 4 | KALKULUS                                               <|")
                print("|>+---+                                                        <|")
                print("|>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|")
                print('MENU: 1.  PART 1(FUNGSI LINEAR)                                <|')
                print('      2.  PART 2(SISTEM BILANGAN REAL)                         <|')
                print('      3.  PART 3(PERSAMAAN DAN PERTIDAKSAMAAN)                 <|')
                print('      4.  PART 4(PERTIDAKSAMAAN IRASIONAL)                     <|')
                print('      5.  PART 5(QUIS)                                         <|')
                print('      6.  PART 6(LIMIT FUNGSI)                                 <|')
                print('      7.  PART 7(LIMIT FUNGSI)                                 <|')
                print('      8.  PART 8(TURUNAN FUNGSI)                               <|')
                print('      9.  PART 9(MID)                                          <|')
                print('      10. PART 10(SISTEM BILANGAN REAL DAN FUNGSI)             <|')
                print('      11. PART 11(INTEGRAL TENTU & TAK TENTU)                  <|')
                print('      12. PART 12(INTEGRAL)                                    <|')
                print('      13. PART 13(INTEGRAL GANDA)                              <|')
                print('      0.  BACK                                                 <|')
                print("---------------------------------------------------------------<|")
                a = input('pilih menu: ')
                if a=='1':
                        print('\n[[1. Fungsi linear ]]')
                        print('[[2. Fungsi kuadrat]]')
                        a=input('pilih menu: ')
                        if a=='1':
                                print('\n[fungsi linear]')
                                while True:
                                    print('1. lihat materi')
                                    print('2. mengerjakan')
                                    a = input('pilih no 1/2: ')
                                    if a=='1':
                                        print('''
bentuk persmaan: y = ax+b
dimana:
y = variabel tidak bebas
x = variabel bebas
a dan b = konstanta

ciri-ciri persamaan linear:
1. apabila a > 0 maka garis a akan bergerak dari bawah ke kanan atas.
2. apabila a < 0 maka garis akan bergerak dari kiri atas ke kanan bawah.
3. apabila a1 != a2 maka garis akan berpotongan
4. apabila a1 = a2 maka garis akan sejajar
5. titik b merupakan perpotongan pada sumbu y
6. a disebut juga tan a, a juga berarti menunjukan arah.

rumus umum tan a:
a = y2 - y1
    x2 - x1

1. contoh soal persamaan linear
+---------------+
| x | 1 | 2 | 3 |
+---+---+---+---+
| y | 9 |11 |13 |
+---+---+---+---+
a. tentukan persamaannya!
b. gambarkan grafiknya!

jawab
sebelum mengerjakan kita lihat apakah sudah ada bentuk persamaan nya. contoh bentuk persamaan yaitu, bisa y = x + 2, bisa y = 2x + 4 dan sebagainya.
nah mungkin kawan-kawan ada yang bingung apa bedanya linear dan kuadrat, untuk ciri linear pada variabelnya tidak berpangkat,
contoh: y = x + 2
        lihat x dan y disebut dengan variabel sedang 2 disebut dengan konstanta
        y = x^2 + 2
        disebut dengan persamaan kuadrat
        
kembali contoh soal diatas, contoh tersebut belum ada bentuk persamaannya. maka kita tentukan dulu bentuk persamaannya.
kita lihat bentuk umum persamaan
y = ax + b
kemudian kita sumbstitusikan nilai x dan y kedalam bentuk umum tersebut
nilai pada kolom pertama x = 1 dan y = 9 maka kita tuliskan sebagai berikut sesuai dengan bentuk umum
9 = a + b
11 = 2a + b
13 = 3a + b

setelah itu kita tentukan nilai a dan b dengan cara metode eliminasi

kita ambil dua bentuk persamaan yang termudah
9 = a + b
11=2a + b
--------- -
-2= -a
a = 2 ->(substitusi a ke 9 = a + b)

9 = 2 + b
b = 9 - 2
b = 7
jadi persamaannya adalah y = 2x + 7
''')
                                    print('\n[yes|no|exit]')
                                    a = input("ulangi lagi[y/n/x]: ")
                                    if a=="n" or a=="N":
                                        break
                                    elif a=="y" or a=="Y":
                                        print()
                                    elif a=='x' or a=='X':
                                        exit()
                        elif a=='2':
                            print('\nfungsi kudrat')
                            
                            print('\n[yes|no|exit]')
                            a = input("ulangi lagi[y/n/x]: ")
                            if a=="n" or a=="N":
                                break
                            elif a=="y" or a=="Y":
                                print()
                            elif a=='x' or a=='X':
                                exit()
                            
                                
                elif a=='2':
                    print('\n[[2. sistem bilangan real]]')
                    
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
                        print('\n[[1. persamaan]]')
                        print('[[2. pertidaksamaan]]')
                        print('[[0. back')
                        a = input('pilih no.1/2>')
                        if a=='1':
                            while True:
                                print('[persamaan]')
                                print('''\nbentuk umum persamaan kuadrat ax^2+bx+c=0
contoh:
x^2+x-2=0
a=1, b=1, c=-2

input a :1
input b :1
input c :-2

    -b +- /b^2-4ac
x = --------------
           2a
    -1 +-/1^2-4(1)(-2)
  = ------------------
           2(1)
    -1 +-/1+8
  = ---------
        2
    -1 +-/9
  = -------
       2
    -1 +- 3
  = -------
       2
    -1 + 3 |     -1 - 3
x1= ------ | x2= ------
      2    |       2
    2      |     -4
  = -      |   = --
    2      |      2
x1= 1      | x2= -2''')
                                print('_________________________')
                                print('menentukan akar persamaan')
                                print('      ax^2+bx+c=0')
                                a = int(input('\ninput a: '))
                                b = int(input('input b: '))
                                c = int(input('input c: '))
                                
                                bb = -1*b
                                b_2 = b**2
                                ac = 4*a*c
                                d = (b**2)-(4*a*c)
                                penyebut = 2*a
                                akar = math.sqrt(d)
                                xa = bb + akar
                                xb = bb - akar
                                x1 = (bb + akar)/(2*a)
                                x2 = (bb - akar)/(2*a)
                                #print(b_2, ac, d, penyebut, akar)
                                print('''
menggunakan rumus persamaan kuadrat:
    -b +- /b^2-4ac
x = --------------
           2a

    -(%s) +- /%s^2-4(%s)(%s)
x = ------------------
            2(%s)
            
    %s +- /%s-(%s)
  = -------------
          %s
          
    %s +- /%s
  = --------
        %s
    
    %s +- %i
  = -------
       %s
     %s + %i 
x1 = ------  
       %s
     %i
   = -
     %s
x1 = %s

     %s - %i
x2 = ------
       %s
     %i
   = --
     %s
x2 = %s
'''%(b,b,a,c,a,bb,b_2,ac,penyebut,bb,d,penyebut,bb,akar,penyebut,bb,akar,penyebut,xa,penyebut,x1,bb,akar,penyebut,xb,penyebut,x2))
                                print('jadi akar-akar persamaannya adalah, x1 = %s dan dan x2 = %s'%(x1,x2))
                                print('\n[yes|no|exit]')
                                a = input("ulangi lagi[y/n/x]: ")
                                if a=="n" or a=="N":
                                    break
                                elif a=="y" or a=="Y":
                                    print()
                                elif a=='x' or a=='X':
                                    exit()
                                
                        elif a=='2':
                            while True:
                                print('[pertidaksamaan]')

                                print('\n[yes|no|exit]')
                                a = input('ulangi lagi[y/n/x]: ')
                                if a=='n' or a=='N':
                                    break
                                elif a=='y' or a=='Y':
                                    print()
                                elif a=='x' or a=='X':
                                    exit()
                        elif a=='0':
                            break
                elif a=='0':
                    break    
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
        elif menu=="6":
                while True:
                    print("|>_____________________________________________________________<|")
                    print("|>+---+                                                        <|")
                    print("|>| 6 | persamaan kuadrat                                      <|")
                    print("|>+---+                                                        <|")
                    print("|>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|")
                    print('''\nbentuk umum persamaan kuadrat ax^2+bx+c=0
contoh:
x^2+x-2=0
a=1, b=1, c=-2

input a :1
input b :1
input c :-2

    -b +- /b^2-4ac
x = --------------
           2a
    -1 +-/1^2-4(1)(-2)
  = ------------------
           2(1)
    -1 +-/1+8
  = ---------
        2
    -1 +-/9
  = -------
       2
    -1 +- 3
  = -------
       2
    -1 + 3 |     -1 - 3
x1= ------ | x2= ------
      2    |       2
    2      |     -4
  = -      |   = --
    2      |      2
x1= 1      | x2= -2''')
                    print('_________________________')
                    print('menentukan akar persamaan')
                    print('      ax^2+bx+c=0')
                    a = int(input('\ninput a: '))
                    b = int(input('input b: '))
                    c = int(input('input c: '))
                    
                    bb = -1*b
                    b_2 = b**2
                    ac = 4*a*c
                    d = (b**2)-(4*a*c)
                    penyebut = 2*a
                    akar = math.sqrt(d)
                    xa = bb + akar
                    xb = bb - akar
                    x1 = (bb + akar)/(2*a)
                    x2 = (bb - akar)/(2*a)
                    #print(b_2, ac, d, penyebut, akar)
                    print('''
menggunakan rumus persamaan kuadrat:
    -b +- /b^2-4ac
x = --------------
           2a

    -(%s) +- /%s^2-4(%s)(%s)
x = ------------------
            2(%s)
            
    %s +- /%s-(%s)
  = -------------
          %s
          
    %s +- /%s
  = --------
        %s
    
    %s +- %i
  = -------
       %s
     %s + %i 
x1 = ------  
       %s
     %i
   = -
     %s
x1 = %s

     %s - %i
x2 = ------
       %s
     %i
   = --
     %s
x2 = %s
'''%(b,b,a,c,a,bb,b_2,ac,penyebut,bb,d,penyebut,bb,akar,penyebut,bb,akar,penyebut,xa,penyebut,x1,bb,akar,penyebut,xb,penyebut,x2))
                    print('jadi akar-akar persamaannya adalah, x1 = %s dan dan x2 = %s'%(x1,x2))
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
                
