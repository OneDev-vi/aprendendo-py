from time import sleep
import pygame
pygame.init()
for c in range(0, 11):
    print (c)
    sleep(1)
pygame.mixer.music.load("siteporn.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()
print ("FIM")