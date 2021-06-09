print("NAMA: FAIZ HIDAYAT \nNIM: 201420026 \nKELAS: IF2A")
# STACK
# =======================================================================

# Import library os untuk membersihkan layar console
#import os


# Class stack
class Stack:
    def __init__(self):
        self.items = []

    # Memeriksa apakah stack kosong
    def isEmpty(self):
        return self.items == []

    # Menambah objek/data ke dalam stack
    def push(self, item):
        self.items.append(item)

    # Mengeluarkan data dari stack
    def pop(self):
        return self.items.pop()

    # Menampilkan objek terakhir dari stack
    def peek(self):
        return self.items[len(self.items) - 1]

    # Mehitung panjang stack
    def size(self):
        return len(self.items)

    # Menu dari aplikasi
    def mainmenu(self):
        # pilih = "y"
        while True:
            # os.system("clear")
            print("=========================")
            print("| Menu aplikasi stack |")
            print("=========================")
            print("1. Push objek")
            print("2. Pop objek")
            print("3. Cek Empty")
            print("4. Tampil objek terakhir")
            print("5. Panjang dari stack")
            print('0. exit')
            print("=========================")
            pilihan = int(input('input menu: '))
            if pilihan==1:
               # os.system("clear")
                obj = str(input("Masukan objek yang ingin anda tambahkan: "))
                self.push(obj)
                print("Object " + obj + " telah ditambahkan")
                x = input("")
            elif pilihan==2:
                # os.system("clear")
                print("Objek " + self.pop() + " dihapus")
                x = input("")
            elif pilihan==3:
                # os.system("clear")
                print(self.isEmpty())
                x = input("")
            elif pilihan==4:
                # os.system("clear")
                print("Objek terakhir: " + self.peek())
                x = input("")
            elif pilihan==5:
                # os.system("clear")
                print("Panjang dari stack adalah: " + str(self.size()))
                x = input("")
            elif pilihan==0:
                exit()

            else:
                pilih = "n"


if __name__ == "__main__":
    s = Stack()

