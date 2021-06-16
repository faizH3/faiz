'''
sekarang kita menghitung bunganya! ooh ya,
apakah anda tahu bahwa kita bisa merantai perhitungan
seperti ini

jawaban = 2000 * /100
kita buat hal serupa di sini
'''
'''
ciptakan variabel suku_bunga dan berikan nilai
antara 5 hingga 30
-ciptakan juga varibel jumlah_bunga yang merupakan
hasil perkalian sisa_cicilan dan suku_bunga 
dan di bagi 100
kenapa dibagi 100?
>>>karena suku bunga satuannya adalah persen
'''
harga_laptop = 5000000
uang_muka = 1000000

sisa_cicilan = harga_laptop - uang_muka
suku_bunga = 20
jumlah_bunga = sisa_cicilan * suku_bunga /100
print(jumlah_bunga)