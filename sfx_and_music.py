import pygame
pygame.mixer.init()

def startbackgroundmusic():
    pygame.mixer.music.load('assets/audio/background_music/bmusic.mp3')
    pygame.mixer.music.play(-1)
def stopbackgroundmusic():
    pygame.mixer.music.stop()

    