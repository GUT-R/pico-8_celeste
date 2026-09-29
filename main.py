import pygame

pygame.init()
tela_lado = int(input("Digite o tamaho da tela : "))
display = pygame.display.set_mode((tela_lado, tela_lado))

rodando = True

player_x: int = display.width / 2 - 20
player_y: int = display.height / 2 - 20

clock = pygame.Clock()
pygame.time.get_ticks()

while rodando:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
            quit(0)
        teclas = pygame.key.get_just_pressed()
        
        if teclas[pygame.K_a]:
                player_x -= 10
                break
        if teclas[pygame.K_d]:
                player_x += 10
                break
        if teclas[pygame.K_s]:
                player_y -= 10
                break
        if teclas[pygame.K_w]:
                player_y -= 10

    display.fill((0, 0, 3))
    pygame.draw.rect(display, (255, 255, 255), (player_x, player_y, 40, 40))

    pygame.display.flip()
    

        