print('''
NAMA : BAGAS SATRIA RENALDI
NIM  : 201420102
KELAS: IF2A\n
''')
while True:
    		print('Descending')
    		data = tuple(input('Masukan data yang belum terurut : '))
    		data_descending = sorted(data, reverse = True)
    		print('print data yang belum terurut: ',data)
    		print("Data yang sudah terurut: ",data_descending)
    		d = input('try again(y/n)? ')
    		if d=='y' or d=='Y':
    			print()
    		elif d=='n' or d=='N':
    			break