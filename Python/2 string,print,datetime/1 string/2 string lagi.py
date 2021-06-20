# # oke mari kita berlatih lagi tentang string
# '''
# instruksi:
# jawab semua variabel di samping menggunakan strings.
# '''
# negara = 'Indonesia'
# ibukota = 'Jakarta'
# motto = 'Bhineka Tunggal Ika'
# tanggal_kemerdekaan = '17 agustus 1945'
# print('negara {}, ibukota {}, motto {}, tanggal kemerdekaan {}'.format(negara,ibukota,motto,tanggal_kemerdekaan))
import pygame
pygame.init()

width = 800
height = int(width * 0.8)

screen = pygame.display.set_mode((width, height))

bg = (255,255,255)

# def back_gr():
#     screen.fill(bg)

run = True

while run:
    # back_gr()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                exit()
    pygame.display.update()
pygame.quit()