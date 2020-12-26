#catatan:
"""c merupakan variabel yang menampung sebuah nilai atau string.
float penulisan dalam bentuk desimal
input sintax untuk memasukan sebuah nilai yang akan diproses
print() perintah untuk mencetak/menampilkan ke menu layar"""

c = float(input('input suhu derajat celcius: '))
f = c*9/5+32
print('%.2fC = %.2fF'%(c,f))
