import pygame

pygame.init()

display = pygame.display.set_mode((800, 600))

rodando = True

player_size: int = 40
player_x: float = display.width / 2 - player_size / 2
player_y: float = display.height / 2 - player_size / 2
player_speed: float = 10

gravity = 2

floor_h = 40
floor_y = display.height - floor_h

clock = pygame.Clock()
pygame.time.get_ticks()

def draw_floor():
      pygame.draw.rect(display, (0, 255, 0), (0, floor_y, display.width, floor_h))

def draw_player():
      pygame.draw.rect(display, (255, 255, 255), (player_x, player_y, player_size, player_size))

while rodando:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
            quit(0)
    
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_a]:
        player_x -= player_speed
    if teclas[pygame.K_d]:
        player_x += player_speed
    if teclas[pygame.K_s]:
        player_y += player_speed
    if teclas[pygame.K_w]:
        player_y -= player_speed

    if player_y < floor_y - player_size:
        player_y += gravity
    player_y = min(player_y, floor_y - floor_h)
    
    display.fill((0, 0, 3))
    draw_floor()
    draw_player()
    

    

    pygame.display.flip()
    

        
