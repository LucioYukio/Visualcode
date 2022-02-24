import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("LOL_Zelda")
clock = pygame.time.Clock()
text_font = pygame.font.Font('C:/Users/Lucio/Documents/Visualcode/Pixeltype.ttf',40)

sky_surface = pygame.image.load('C:/Users/Lucio/Documents/Visualcode/Sky.png').convert()
ground_surface = pygame.image.load('C:/Users/Lucio/Documents/Visualcode/ground.png').convert()

text_surface = text_font.render("Score", False, (64,64,64))
text_rect = text_surface.get_rect(center = (400, 50))



snail_surface = pygame.image.load('C:/Users/Lucio/Documents/Visualcode/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (800,300))

player_surf = pygame.image.load('C:/Users/Lucio/Documents/Visualcode/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
#player midbottom = 48


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if event.type == pygame.KEYDOWN:
        print('Key down')

    if event.type == pygame.KEYUP:
        print('Key up')

    snail_rect.left -= 4   

    screen.blit(sky_surface,(0,0))  
    screen.blit(ground_surface,(0,300))

    pygame.draw.rect(screen,'#c0e8ec', text_rect,6,10)
    screen.blit(text_surface, text_rect)

    screen.blit(snail_surface, snail_rect)

    if snail_rect.right == 0: snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)

    screen.blit(player_surf, player_rect)
  



    pygame.display.update()
    clock.tick(60)