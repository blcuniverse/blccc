import random
import pygame
import sys
from pygame.surface import Surface, SurfaceType

WIDTH = 1024
HEIGHT = 800

FONT_WIDTH = 15
pygame.init()
pygame.font.init()
pygame.display.set_caption('                                                                                                                  来下一场loveinfinity的梦幻雨')
winSur: Surface | SurfaceType = pygame.display.set_mode((WIDTH,HEIGHT))
font = pygame.font.Font('C:\Windows\Fonts\simfang.ttf',15)
bg_surface = pygame.Surface((WIDTH,HEIGHT),flags=pygame.SRCALPHA)

pygame.Surface.convert(bg_surface)

bg_surface.fill(pygame.Color(0,0,0,30))
winSur.fill((0,0,0))
#letter = ['I','L','O','V','E','i','n','f','i','n','i','t','y']
letter = ['I','L','O','V','E','w','q',]
texts = [font.render(str(letter[i]),
                     True,
                     (random.randint(0,255),random.randint(0,255),random.randint(0,255)))for i in range(7)]
                     #(random.randint(0,255),random.randint(0,255),random.randint(0,255)))for i in range(14)]

column = int(WIDTH/FONT_WIDTH)

drops = [0 for i in range(column)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.time.delay(30)
    winSur.blit(bg_surface,(0,0))
    for i in range(len(drops)):
        text = random.choice(texts)
        winSur.blit(text,(i * FONT_WIDTH,drops[i]*FONT_WIDTH))
        drops[i] +=1
        if drops[i] * 10>HEIGHT or random.random() >0.95:
            drops[i] = 0
    pygame.display.flip()
