print('reproduzindo música MP3')
import pygame
pygame.mixer.init()
pygame.mixer_music.load('desafio021.mp3')
pygame.mixer_music.play()
input('Curti o som')