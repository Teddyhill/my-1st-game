from re import X
from turtle import Screen
import pygame


WINDOW_W = 1000
WINDOW_H = 641
WINDOW_SIZE = (WINDOW_W, WINDOW_H)
pygame.init()


screen = pygame.display.set_mode(WINDOW_SIZE)
square = pygame.image.load("pngaaa.com-472793.png")
square = pygame.transform.scale(square,(50,90))


play = True

while play:
  screen.fill((0,0,0))
  screen.blit(square,(500,300))
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
  x = 250
  for i in range(7):
     pygame.draw.line(screen, (255,0,0), (x, 0), (x, 1000),4)
     x += 100

  pygame.display.flip()

pygame.quit()
