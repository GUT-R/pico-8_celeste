import ctypes
import pygame

pygame.init()

display = pygame.display.set_mode((800, 600))

view = display.get_view("0") # Extrai o buffer como uma Array C
ptr = ctypes.addressof(ctypes.c_ubyte.from_buffer(view)) # Converte a array para bytes e obtem o ponteiro

c_power = ctypes.CDLL("./test.o").c_power

c_power.argtypes = [ctypes.c_void_p, ctypes.c_int] # tipo de cada parâmetro
c_power.restype = None # Tipo de resposta (void)

rodando = True
def is_running():
    global rodando
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            rodando = False
            pygame.quit()
    return rodando


clock = pygame.Clock()
while is_running():
    clock.tick(30)

    c_power(ctypes.c_void_p(ptr), ctypes.c_int(display.width))
    pygame.display.flip()