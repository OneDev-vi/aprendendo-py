import pygame
import random

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo de Nave Espacial")

# Definir cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# Carregar imagens
imagem_nave = pygame.image.load("nave.png")
imagem_asteroide = pygame.image.load("asteroide.png")
imagem_tiro = pygame.image.load("tiro.png")

# Definir propriedades do jogador
largura_nave = 64
altura_nave = 64
x_nave = largura_tela * 0.45
y_nave = altura_tela * 0.8
velocidade_nave = 5

# Propriedades do tiro
tiros = []
velocidade_tiro = 10

# Propriedades dos asteroides
asteroides = []
velocidade_asteroide = 5
taxa_geracao_asteroides = 25

# Função para desenhar a nave
def desenhar_nave(x, y):
    tela.blit(imagem_nave, (x, y))

# Função para desenhar um tiro
def desenhar_tiro(x, y):
    tela.blit(imagem_tiro, (x, y))

# Função para desenhar um asteroide
def desenhar_asteroide(x, y):
    tela.blit(imagem_asteroide, (x, y))

# Função para verificar colisão
def verificar_colisao(x1, y1, largura1, altura1, x2, y2, largura2, altura2):
    return x1 < x2 + largura2 and x1 + largura1 > x2 and y1 < y2 + altura2 and y1 + altura1 > y2

# Função principal do jogo
def jogo():
    x = x_nave
    y = y_nave
    x_mudanca = 0
    pontuacao = 0
    vidas = 3

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_mudanca = -velocidade_nave
                if evento.key == pygame.K_RIGHT:
                    x_mudanca = velocidade_nave
                if evento.key == pygame.K_SPACE:
                    tiros.append([x + largura_nave//2 - 2, y])

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    x_mudanca = 0

        x += x_mudanca
        tela.fill(preto)

        # Desenhar nave
        desenhar_nave(x, y)

        # Gerar novos asteroides
        if random.randint(1, taxa_geracao_asteroides) == 1:
            asteroides.append([random.randint(0, largura_tela - largura_nave), -64])

        # Mover e desenhar tiros
        for tiro in tiros[:]:
            tiro[1] -= velocidade_tiro
            if tiro[1] < 0:
                tiros.remove(tiro)
            desenhar_tiro(tiro[0], tiro[1])

        # Mover e desenhar asteroides
        for asteroide in asteroides[:]:
            asteroide[1] += velocidade_asteroide
            desenhar_asteroide(asteroide[0], asteroide[1])

            # Verificar colisão com a nave
            if verificar_colisao(x, y, largura_nave, altura_nave, asteroide[0], asteroide[1], largura_nave, altura_nave):
                vidas -= 1
                asteroides.remove(asteroide)
                if vidas == 0:
                    rodando = False

            # Verificar colisão com tiros
            for tiro in tiros[:]:
                if verificar_colisao(tiro[0], tiro[1], 4, 10, asteroide[0], asteroide[1], largura_nave, altura_nave):
                    tiros.remove(tiro)
                    asteroides.remove(asteroide)
                    pontuacao += 10
                    break

        # Mostrar pontuação e vidas
        fonte = pygame.font.Font(None, 36)
        texto_pontuacao = fonte.render("Pontuação: " + str(pontuacao), True, branco)
        texto_vidas = fonte.render("Vidas: " + str(vidas), True, branco)
        tela.blit(texto_pontuacao, (10, 10))
        tela.blit(texto_vidas, (10, 50))

        pygame.display.update()

    pygame.quit()

# Iniciar o jogo
jogo()
