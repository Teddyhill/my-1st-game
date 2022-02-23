import pygame
#import pygame.freetype
# screen size 
WINDOW_W = 837
WINDOW_H = 478 
WINDOW_SIZE = (WINDOW_W, WINDOW_H)
pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
square = pygame.image.load("pngaaa.com-472793.png")
square = pygame.transform.scale(square,(50,90))
screen.fill(screen(0,0,0))

#clock = pygame.time.Clock()

circle_x = 10
circle_y = WINDOW_H /2
ship_x = WINDOW_W /2
ship_y = WINDOW_H - 80
circle_x_step = 10
x_step = 10
laser_list = []
play = True


# laser_list = [[121,780],[171,780]]
# i=1
# l=[171,10]
# l[0] = 171
while play:
  screen.blit(square,(0,0))

  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

  pygame.display.flip()
 # clock.tick(10)
pygame.quit()