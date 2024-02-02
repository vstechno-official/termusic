import os
import pygame
import time

print("Welcome to Termusic!")
print("Pause/Stop your music with CTRL+C")

file_path = input("Enter the file path of the .mp3 file: ")

pygame.mixer.init()

pygame.mixer.music.load(file_path)

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    print("🎵" * 10)
    time.sleep(2.0)
    print("\r", end="")

    print("Playing: [", end="")
    for i in range(20):
        print("▓", end="")
        time.sleep(0.1)
    print("] 100%")

    time.sleep(1)

pygame.mixer.music.stop()
pygame.mixer.quit()

print("Music stopped! Thanks for listening.")
