# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from os import path

# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'img')

# Dados gerais do jogo.
WIDTH = 480 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo


# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class Player(pygame.sprite.Sprite):
    #Construtor de classe
    def __init__(self):
        #Construtor da classe pai(Sprite)
        pygame.sprite.Sprite.__init__(self)
        #Carregando a imagem de fundo
        player_image = pygame.image.load(path.join(img_dir,"playerShip1_orange.png")).convert()
        self.image = player_img

        #Diminuindo o tamanho da imagem
        self.image  = pygame.transform.scale(player_image, (50,38))

        #Deixando transparente
        self.image.set_colorkey(BLACK)

        #Detalhes do posicionamento
        self.rect = self.image.get_rect()

        #Centraliza embaixo da tela
        self.rect.centerrx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        
        self.speedx = 0
    #Metodo que salva a posicao da navinha
    def update(self):
        self.rect.x += self.speedx
        
        #Matem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0: 
            self.rect.left = 0

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Navinha")

#Variavel para o ajuste da velocidade
clock =  pygame.time.Clock()

background = pygame.image.load

# Nome do jogo
pygame.display.set_caption("Asteroids")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
background_rect = background.get_rect()

#Cria uma nave. O construtor sera chamado automaticamente
player=Player()

#Cria um grupo de sprites e adiciona a nave
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Comando para evitar travamentos.
try:
    
    # Loop principal.
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
            #Verifica se voce apertou alguma tecla
            if event.type == pygame.KEYDOWN:
                #Dependendo da tecla, altera a velocidade
                if event.key == pygame.K_LEFT:
                    player.speedx = 8
            
            #Verifica se soltou alguma tecla
            if event.type == pygame.KEYUP:
                #Dependendo da tecla, altera a velocidade
                if event.key == pygame.K_LEFT:
                    speedx = 0
                if event.key == pygame.K_RIGHT:
                    speedx = 0
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
            
            #Depois de processar eventos
            #Atualiza de acao de cada sprite
            all_sprites.update()
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)

        #Depois de desenhar tudo, inverte o display
        pygame.display.flip()

finally:
    pygame.quit()
