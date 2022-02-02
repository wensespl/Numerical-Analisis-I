import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

x = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
y = [480, 89, -66, 10, 338, 807, 1238, 1511, 1583, 1462, 1183, 804]
n = len(y)

plt.plot(x,y, 'o')

Y = fft(y)/n
plt.plot(x ,Y, 'o')

plt.show()