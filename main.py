import pygame

pygame.init()

display = pygame.display.set_mode((800, 600))

rodando = True

player_x: int = display.width / 2 - 20
player_y: int = display.height / 2 - 20
gravity = 2

floor_h = 40
floor_y = display.height - floor_h

clock = pygame.Clock()
pygame.time.get_ticks()

def draw_floor():
      pygame.draw.rect(display, (0, 255, 0), (0, floor_y, display.width, floor_h))

def draw_player():
      pygame.draw.rect(display, (255, 255, 255), (player_x, player_y, 40, 40))

while rodando:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
            quit(0)
        teclas = pygame.key.get_just_pressed()
        
        if teclas[pygame.K_a]:
            player_x -= 10
        if teclas[pygame.K_d]:
            player_x += 10
        if teclas[pygame.K_s]:
            player_y += 10
        if teclas[pygame.K_w]:
            player_y -= 10

    display.fill((0, 0, 3))
    draw_floor()
    draw_player()
    

    if player_y < floor_y - 40:
        player_y += gravity

    pygame.display.flip()
    

        
