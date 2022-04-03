import pygame
import os
from datetime import date, datetime

pygame.init()

size = (WIDTH, HEIGHT) = (1440, 1050)
screen = pygame.display.set_mode(size)
running = True
clock = pygame.time.Clock()
white = (255,255,255)

bg = pygame.transform.scale(pygame.image.load(os.path.join('images','main.jpeg')),(WIDTH, HEIGHT))

sec_img = pygame.image.load(os.path.join('images','SecondHand.png'))
x_sec, y_sec = WIDTH/2 + 7, HEIGHT/2 - 5

min_img = pygame.image.load(os.path.join('images','MinuteHand.png'))
x_min, y_min = WIDTH/2, HEIGHT/2

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)
    return rotated_image, new_rect

while running:

   clock.tick(60)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      
   screen.fill(white)

   screen.blit(bg, (0,0))

   now = datetime.now()

   second = now.second
   screen.blit(rot_center(sec_img, -second*6, x_sec, y_sec)[0], rot_center(sec_img, -second*6, x_sec, y_sec)[1])

   minute = now.minute
   screen.blit(rot_center(min_img, -minute*6, x_min, y_min)[0], rot_center(min_img, -minute*6, x_min, y_min)[1])

   pygame.draw.circle(screen, (53,54,55), (WIDTH/2, HEIGHT/2), 25)

   pygame.display.update()

pygame.quit()