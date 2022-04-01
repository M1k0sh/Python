import pygame
import random
import sys

def run():

    musics = [
        r"C:\Users\PK\python1\Python\Lab7\musics\irina-kajratovna-shiza-kok-tu_(muzzonas.ru).mp3",
        r"C:\Users\PK\python1\Python\Lab7\musics\pre_kai_ro_-_1_slowed_73488250.mp3",
        r"C:\Users\PK\python1\Python\Lab7\musics\ᴍᴇʀᴄʏ _ʀᴍx.mp3",
        r"C:\Users\PK\python1\Python\Lab7\musics\аппарат президента.mp3",
        r"C:\Users\PK\python1\Python\Lab7\musics\ночной рейс.mp3",
        r"C:\Users\PK\python1\Python\Lab7\musics\Без тебя догорел мой рай.mp3",
        r"C:\Users\PK\python1\Python\Lab7\musics\кино.mp3",
        r"C:\Users\PK\python1\Python\Lab7\musics\Особенная slow.mp3",
        r"C:\Users\PK\python1\Python\Lab7\musics\Патрон.mp3",
        r"C:\Users\PK\python1\Python\Lab7\musics\чародей rmx.mp3",
        r"C:\Users\PK\python1\Python\Lab7\musics\Эти будни _slow.mp3",
        r"C:\Users\PK\python1\Python\Lab7\musics\Baby mama _ sʟᴏᴡ.mp3",
        r"C:\Users\PK\python1\Python\Lab7\musics\ʙɪsᴍᴀʀᴋ _ sʟᴏᴡ.mp3",
        r"C:\Users\PK\python1\Python\Lab7\musics\Low rmx  .mp3",
        r"C:\Users\PK\python1\Python\Lab7\musics\s.o remix.mp3",
        r"C:\Users\PK\python1\Python\Lab7\musics\𐌑᧐ᥙ_ⲙыᥴ᧘ᥙ_нᥲ_днᥱ_᧐нᥙ_s᧐ᥣ᧐ᥕ.mp3"
    ]

    pygame.init()
    screen = pygame.display.set_mode((700, 700)) 

    clock = pygame.time.Clock()
    pygame.display.set_caption("Музыка")
    image = pygame.image.load(r"C:\Users\PK\python1\Python\Lab7\images\123.jpg")

    pos = 0
    pygame.mixer.music.load(musics[pos])
    pygame.mixer.music.play()
    pygame.mixer.music.queue(musics[random.randrange(0, 16)])
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.pause()
                elif event.key == pygame.K_KP_ENTER:
                    pygame.mixer.music.unpause()
                
                elif event.key == pygame.K_RIGHT:
                    if pos <= 16:
                        pos+=1
                    else:
                        pos = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(musics[pos])
                    pygame.mixer.music.play()
                elif event.key == pygame.K_LEFT:
                    if pos >= 1:
                        pos-=1
                    else:
                        pos = 15
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(musics[pos])
                    pygame.mixer.music.play()
    
        pygame.display.flip()    
        clock.tick(60)    
        screen.blit(image, (0, 0))
run()