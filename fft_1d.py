from scipy import signal
import numpy as np
import matplotlib.pyplot as plt





s0 = [np.sin(2 *np.pi*1000 * i) for i in range(1000)]
N = len(s0)

fs = 44100

freq = np.fft.fftfreq(len(s0), d=1/fs)
sf =  np.fft.fft(s0[:N])
plt.plot(freq[0:], np.abs(sf[0:]))
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.title("FFT")
plt.show()


