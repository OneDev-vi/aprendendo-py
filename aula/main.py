import pygame
import random

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Definir cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)

# Definir as propriedades do jogador
largura_jogador = 50
altura_jogador = 50
x_jogador = largura_tela * 0.45
y_jogador = altura_tela * 0.8
velocidade_jogador = 5

# Definir as propriedades do obstáculo
largura_obstaculo = 50
altura_obstaculo = 50
x_obstaculo = random.randrange(0, largura_tela - largura_obstaculo)
y_obstaculo = -altura_obstaculo
velocidade_obstaculo = 5

# Função para desenhar o jogador
def desenhar_jogador(x, y):
    pygame.draw.rect(tela, preto, [x, y, largura_jogador, altura_jogador])

# Função para desenhar o obstáculo
def desenhar_obstaculo(x, y):
    pygame.draw.rect(tela, vermelho, [x, y, largura_obstaculo, altura_obstaculo])

# Função principal do jogo
def jogo():
    x = x_jogador
    y = y_jogador
    x_mudanca = 0

    sair = False
    while not sair:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sair = True

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_mudanca = -velocidade_jogador
                if evento.key == pygame.K_RIGHT:
                    x_mudanca = velocidade_jogador

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    x_mudanca = 0

        x += x_mudanca
        tela.fill(branco)

        desenhar_obstaculo(x_obstaculo, y_obstaculo)
        desenhar_jogador(x, y)

        y_obstaculo += velocidade_obstaculo

        # Reiniciar o obstáculo ao sair da tela
        if y_obstaculo > altura_tela:
            y_obstaculo = -altura_obstaculo
            x_obstaculo = random.randrange(0, largura_tela - largura_obstaculo)

        # Verificar colisão
        if y_jogador < y_obstaculo + altura_obstaculo and y_jogador + altura_jogador > y_obstaculo:
            if x_jogador < x_obstaculo + largura_obstaculo and x_jogador + largura_jogador > x_obstaculo:
                sair = True

        pygame.display.update()

    pygame.quit()
    quit()

# Iniciar o jogo
jogo()
