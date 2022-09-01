from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

def fft_langmuir(x, s1, s2, N):
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

x = [i/2 for i in range(1,1000)]
s1 = [np.sin(2 * i) for i in range(1,1000)]
s2 = [np.sin(2 * i + np.pi/2) for i in range(1,1000)]

# ~ fft_langmuir(x, s1, s2, 100)

# ~ plt.plot(s1)
# ~ plt.plot(s2)
# ~ plt.show()

# ~ fs = 1000

# ~ f, Cxy = signal.coherence(s1, s2, fs, nperseg=50)
# ~ plt.semilogy(f, Cxy)
# ~ plt.xlabel('frequency [Hz]')
# ~ plt.ylabel('Coherence')
# ~ plt.show()

time = np.arange(0, 10, 0.1)
y = np.sin(time)
y1 = np.sin(time + np.pi/2)

result = np.correlate(y, y1, mode='full')
lags = np.arange(-time[-1],time[-1]+0.1,0.1) #adding 0.1 to include the last instant of time also
plt.figure()
plt.plot(lags,result)
plt.xlabel('Lag')
plt.ylabel('autocorrelation')
plt.show()
