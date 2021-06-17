# mendapatkan tagihan bulanan
# selamat satu unit lagi dan anda sudah membuat sebuah program! ketika
# kita bilang anda bisa membuat apa saja dengan python, kita bersungguh-sungguh!
# batas dari apa yang anda bisa bangun adalah di imajinasi anda
# terus belajar ke bab berikutnya dan akhirnya anda akan bisa membuat program yang
# lebih keren lagi!

'''
instruksi
-oke sekarang kita buat variabel
total_tagihan
yang merupakan jumlah dari
sisa_cicilan
dan
jumlah_bunga
-setelahnya kita buat
tagihan_bulanan
yang merupakan
total_tagihan
dibagi
12
-jalankan codenya dan lihat tagihan bulananan anda
-ubah angkanya sesuasi yang anda mau dan bermain mainlah dengan apa yang telah anda pelajari
'''
# harga_laptop = 5000000
# uang_muka = 1000000
# sisa_cicilan = harga_laptop-uang_muka
# suku_bunga = 10
# jumlah_bunga = sisa_cicilan * suku_bunga /100
# total_tagihan = sisa_cicilan + jumlah_bunga
# tagihan_bulanan = total_tagihan /12
# print(tagihan_bulanan)
while True:
    print('''
    menghitung total tagihan''')
    harga = int(input('harga barang: '))
    uang_muka = int(input('uang muka: '))
    sisa_cicilan = harga-uang_muka
    print('sisa cicilan {} - {} = {}'.format(harga,uang_muka,sisa_cicilan))
    suku_bunga = int(input('bunga: '))
    jumlah_bunga = sisa_cicilan * suku_bunga / 100
    total_tagihan = sisa_cicilan + jumlah_bunga
    tagihan_bulanan = total_tagihan / 12
    print('jumlah bunga {} x {} / 100 = {}'.format(sisa_cicilan,suku_bunga,jumlah_bunga))
    print('total tagihan: {} + {} = {}'.format(sisa_cicilan,jumlah_bunga,total_tagihan))
    print('tagihan bulanan: {} / 12 = %.2f'.format(total_tagihan)%(tagihan_bulanan))
    d = input('try again(y/n)? ')
    if d=='y' or d=='Y':
        print()
    elif d=='n' or d=='N':
        exit()

