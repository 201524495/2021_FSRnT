import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import pygame
import time

pygame.init()
pygame.mixer.init()
sounda = pygame.mixer.Sound('/home/pi/Downloads/seeed-voicecard/out.wav')
sounda.play()
time.sleep(1)

fs, data = wavfile.read('/home/pi/Downloads/seeed-voicecard/out.wav')
time = np.linspace(0, 100, num=(len(data)))
plt.plot(time, data)
plt.show()
