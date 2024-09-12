# Tocando música com a biblioteca 'pygame'

import pygame

# iniciando a biblioteca
pygame.init()

# abrindo o arquivo
pygame.mixer.music.load('audio.mp3')

# exibindo conteúdo do áudio
pygame.mixer.music.play()

# chave para parar o conteúdo
stop_music = input('Pressione qualquer botão para parar')
