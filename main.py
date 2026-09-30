import pygame

# Você pesquisou como importart imagens em python?
# // sim, precisa de uma bibleoteca chamada pillow
# O pygame resolve sozinho
# ele lê o binário e exibe direto
# // entao a funcao que tu tinha escrevido pode pegar cadfa pixel individual?
# // ou ela le a imagem inteira?
# // por que se ela le cada pixel individual, ela teria que receber algums parametros como a posicao do pixel como uma tupla
# Ela lê o arquivo como binário
# // ou seja? ela vai retornar o que?

# 101001000101010100101010
# // ok isso era o que eu tava esperando que acontecesse
# // que bom que e assim e nao um monte de listas com inumeros valors de posicao, com, transparencia, matiz, e outras coisas
# // queria que o vs code me mostrasse a documentacao certa pra esse metodo
# Voce quer ler um arquivo de imagem, pixel por pixel?
# // sim
# // to vendo a documentacao no GitHub do projeto da comunidade
# Bro, por favor, so aprende logo como fazer o .blit no pygame
# // .split(), nao? 
# blit. É uma função/método que o Pygame usa para colocar uma imagem no buffer
# // faz sentido
# // deixa eu fazer minha magica aqui entao

from pygame.math import lerp as larp # // isso aqui? # Sim // kkkkkkkk
pygame.init()

display = pygame.display.set_mode((800, 600))

rodando = True

player_size: int    = 40
player_x: float     = display.width / 2 - player_size / 2
player_y: float     = display.height / 2 - player_size / 2
jump_force: float   = 80
jump_duration: float = 0.1
player_speed: float = 20
player_hyper_speed: float = 100

gravity = 6

floor_h = 40
floor_y = display.height - floor_h

clock = pygame.Clock()

def draw_floor():
      pygame.draw.rect(display, (0, 255, 0), (0, floor_y, display.width, floor_h))

def draw_player():
      pygame.draw.rect(display, (255, 255, 255), (player_x, player_y, player_size, player_size))

larp_atual = 0
y1 = player_y
y2 = player_y
jumping = False

while rodando:
    direction_x = 0
    direction_y = 0
    delta = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
            quit(0)

    old_player_y = player_y

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_a]:
        direction_x = -1
    if teclas[pygame.K_d]:
        direction_x = 1
    if teclas[pygame.K_s]:
        direction_y = 1
    if teclas[pygame.K_w] and player_y >= floor_y - player_size:
        jumping = True
        y1 = player_y
        y2 = player_y - jump_force
        larp_atual = 0
        direction_y = -1
    if teclas[pygame.K_SPACE]: # DASH!
        player_x *= player_hyper_speed
        player_y *= player_hyper_speed
    
    # // eu acho que meu codigo deve funcionar
    # // nao completo, mas eu acho que ele pode servir como prototipo que eu posso expandir deposi da prova de minora
    # bro, vou ter q ir já
    # // ok, eu vou dar commit entao
    if player_y < floor_y - player_size:
        player_y += gravity
    elif player_y > floor_y - player_size:
        player_y = floor_y - player_size


    
    if jumping:
        larp_atual = larp_atual + delta / jump_duration
        player_y = larp(y1, y2, larp_atual)

        if larp_atual >= 1.0:
            jumping = False

    player_y *= direction_y
    player_x *= direction_x

    display.fill((0, 0, 3))
    draw_floor()
    draw_player()

    pygame.display.flip()

def algum_codigo():
    with open('filename', 'rb') as file:
        file.read()
    pixel_atual: int = 0
    # esse vai ser o numero que vai guardar a chave correspondente ao nosso pixel
    
    posit_byte      : int = 0
    posit_bits      : int = 0
    pixel_sep       : int = 1
    pixel_sep_old   : int = 0
    # Mano, interpolação linear é algo bizarro
    # // imagino
    # // e matematica, entao tinha que ser bizarro (isso e uma reference?)
    
    channel_red   : list = 0
    channel_green : list = 0
    channel_blue  : list = 0
    channel       : int = 0
    for posit_byte in range(pixel_sep_old * 8, len(file.read), pixel_sep * 8):
        
        byte_cur = [int(bit) for bit in range(pixel_sep_old * 8, pixel_sep * 8)]
        match channel:
            case 0:
                channel_red   = byte_cur
                channel += 1
            case 1:
                channel_green = byte_cur
                channel += 1
            case 2:
                channel_blue  = byte_cur
                channel = 0
                # ta faznd oq agr?
                # // to fazendo a lista dos bits que eu selecionei
                # // basicamente, eu to selecionando partes de 8 bits da imagem
                # // e ai cada uma dessas partes vai corresponder a um channel
                # // 0 nesse match e o vermelho, 1 o verde, 2 o azul
                # // quando chegar em 2 volta ao 0 e eu continuo o for para comtinuar para o proximo pixel
                # // faz sentido?
                # N, so use o blit do Pygame
                # // nao vou nao
        

    pixel_channel: list = [channel_red, channel_green, channel_blue]
    
    # lil bro, faz oq tu achar mais desotimizado
    # // esse e meu trabalho # (desotimizar)
    # // bro
    # // tu ta vendo essa merda?
    # eu NAO vou analisar esse codigo

    # Faz isso em C btw
    # // tu faz a importacao?
    # ss
    # // ok

    # Quer dizer, eu posso, mas nao devo
    # // entao eu faco em python mesmo