import pygame,os

pygame.init()

color_set = {
   'black': (0,0,0),
   'white': (255,255,255),
   'red': (255,0,0),
   'green': (0,255,0),
   'blue': (0,0,255),
   'yellow': (255,255,0),
   'cyan': (0,255,255),
   'magenta': (255,0,255),
   'gray': (127, 127, 127)
}

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(color_set['white'])
clock = pygame.time.Clock()
run = True

def get_color(color_set):
   for color in color_set.values():
      yield color

font = pygame.font.SysFont('Calibri',40)
color_section = font.render('Colors',True,color_set['black'])
screen.blit(color_section,(WIDTH/2+len(color_set)*40, HEIGHT-40))

cnt = 0
for i in get_color(color_set):
   grid = cnt*40
   pygame.draw.rect(screen,i,(WIDTH/2+grid,660,40,40))
   cnt+=1

erase = pygame.transform.scale(pygame.image.load(os.path.join('images\i.png')),(40,40))
screen.blit(erase,(0,HEIGHT-40))

pen = pygame.transform.scale(pygame.image.load(os.path.join('images\pencil.png')),(40,40))
screen.blit(pen,(40+10,HEIGHT-40))

pygame.draw.rect(screen,color_set['black'],(90+10,HEIGHT-40,50,40),3)

pygame.draw.circle(screen,color_set['black'],(150+10+20,HEIGHT-40+20),20,3)

font = pygame.font.SysFont('Calibri',40)
shapes = font.render('Shapes',True,color_set['black'])
screen.blit(shapes,(180+20+10,HEIGHT-40))

plus = pygame.transform.scale(pygame.image.load(os.path.join('images\plus.png')),(40,40))
screen.blit(plus,(WIDTH/2-120,HEIGHT-40)) 

minus = pygame.transform.scale(pygame.image.load(os.path.join('images\minus.png')),(40,40))
screen.blit(minus,(WIDTH/2-80,HEIGHT-40))

draw = None

color = color_set['black']

prev = None
cur = None
line_width = 1

while run:
   clock.tick(60)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False
   
      if event.type == pygame.MOUSEBUTTONDOWN:
         pos_select = pygame.mouse.get_pos()
         if pos_select[1] > HEIGHT-40:
            if 0 < pos_select[0] < 40:
               draw = 'eraser'
            if 50 < pos_select[0] < 90:
               draw = 'pen'
            if 100 < pos_select[0] < 150:
               draw = 'rect'
            if 160 < pos_select[0] < 200:
               draw = 'circle'
            if 500 < pos_select[0] < 540:
               color = color_set['black']
            if 540 < pos_select[0] < 580:
               color = color_set['white']
            if 580 < pos_select[0] < 620:
               color = color_set['red']
            if 620 < pos_select[0] < 660:
               color = color_set['green']
            if 660 < pos_select[0] < 700:
               color = color_set['blue']
            if 700 < pos_select[0] < 740:
               color = color_set['yellow']
            if 740 < pos_select[0] < 780:
               color = color_set['cyan']
            if 780 < pos_select[0] < 820:
               color = color_set['magenta']
            if 820 < pos_select[0] < 860:
               color = color_set['gray']

            if 380 < pos_select[0] < 420:
               line_width += 1
            if 420 < pos_select[0] < 460:
               line_width -= 1

      if draw == 'pen':
         if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pos_select
         if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
            if prev:
               if prev[1]<HEIGHT-40 and cur[1]<HEIGHT-40:
                  pygame.draw.line(screen,color,prev,cur,line_width)
                  prev = cur
         if event.type == pygame.MOUSEBUTTONUP:
            prev = None

      if draw == 'rect':
         if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pos_select
         if event.type == pygame.MOUSEBUTTONUP:
            cur = pygame.mouse.get_pos()
            if prev[1] < HEIGHT-40 and cur[1] < HEIGHT-40:
               x,y = prev[0], prev[1]
               width, height = cur[0]-prev[0], cur[1]-prev[1]
               if width < 0:
                  x += width
                  width = abs(width)
               if height < 0:
                  y += height
                  height = abs(height)
               pygame.draw.rect(screen,color,(x,y,width,height),line_width)

      if draw == 'circle':
         if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pos_select
         if event.type == pygame.MOUSEBUTTONUP:
            cur = pygame.mouse.get_pos()
            if prev[1] < HEIGHT-40 and cur[1] < HEIGHT-40:
               x,y = prev[0], prev[1]
               width, height = cur[0] - prev[0], cur[1] - prev[1]
               if width < 0:
                  x += width
                  width = abs(width)
               if height < 0:
                  y += height
               pygame.draw.circle(screen,color,(x+width/2,y+width/2),width/2,line_width)            

      if draw == 'eraser':
         if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pos_select
         if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
            if prev:
              if prev[1]<HEIGHT-55 and cur[1]<HEIGHT-55:
                 pygame.draw.line(screen,color_set['white'],prev,cur,40)
                 prev = cur
         if event.type == pygame.MOUSEBUTTONUP:
            prev = None 

   pygame.display.update()