import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('coloque o arquivo de .mp3 aqui')
pygame.mixer.music.play()
input()
pygame.event.wait()
