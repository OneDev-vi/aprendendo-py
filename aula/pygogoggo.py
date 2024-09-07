import pygame
pygame.init()

largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('caranba que pintoi nenorme')

# Definindo as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)

# Posição inicial do quadrado
x = largura // 2
y = altura // 2
largura_quadrado = 40
altura_quadrado = 40
velocidade = 5

# Configurando o relógio
clock = pygame.time.Clock()

# Loop principal do jogo
rodando = True
while rodando:
    # Loop de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Movimentação com o teclado
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    # Preencher a tela com branco
    tela.fill(branco)

    # Desenhar o quadrado
    pygame.draw.rect(tela, vermelho, (x, y, largura_quadrado, altura_quadrado))

    # Atualizar a tela
    pygame.display.flip()

    # Controlando o FPS
    clock.tick(60)

# Encerrando o Pygame
pygame.quit()
