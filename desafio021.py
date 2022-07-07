print('reproduzindo música MP3')
import pygame
pygame.mixer.init()  #inicializando o mixer pygame
pygame.mixer.music.load('desafio021.mp3') #Carregar um arquivo de música para reprodução
pygame.mixer.music.play() #Iniciar a reprodução da música
while(pygame.mixer.music.get_busy()): pass

# pygame.mixer.music.get_busy = verifique se o stream de música está tocando.