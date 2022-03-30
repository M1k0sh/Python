import pygame

pygame.init()

size = width, height = (700, 800)

screen = pygame.display.set_mode(size)

x = 0
y = 0
speed = 20
clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    press = pygame.key.get_pressed()
    if press[pygame.K_UP]:
        if y >= 20:
                y += (-1) * speed
    if press[pygame.K_DOWN]:
        if y <= height - 70:
                y += speed
    if press[pygame.K_LEFT]:
        if x >= 20:
                x += (-1) * speed
    if press[pygame.K_RIGHT]:
        if x <= width - 70:
                x += speed 

    screen.fill((255, 255, 255))
    clock.tick(30)
    pygame.draw.ellipse(screen, ((255, 0, 0)), (x, y, 50, 50))
    pygame.display.flip()
pygame.quit()