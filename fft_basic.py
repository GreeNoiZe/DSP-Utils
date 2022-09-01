from scipy import signal
import numpy as np
import matplotlib.pyplot as plt



def fft_compare(x, s1, s2, N):
    T_0 = x[1] - x[0]
    T = np.round(T_0, decimals=7)
    fs = 1/T
    freq = np.linspace(0,fs/2,int(len(s1[:N])/2) + 1)
    s1f =  np.fft.rfft(s1[:N])
    s2f =  np.fft.rfft(s2[:N])
    plt.plot(freq, np.abs(s1f))
    plt.plot(freq, np.abs(s2f))
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.title("FFT from the langmuir probe")
    plt.show()

