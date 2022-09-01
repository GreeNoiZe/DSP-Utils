from scipy.signal import butter, lfilter

#Creation of an array with all data files in the directory
data_files = os.listdir('/home/dennis/Dev/PythonDev/MistralPython/Data/data_07_12_2020')

#Creation of an array with all data (2 files in this examples for the 2 Langmuir probes)
data =  [np.genfromtxt(open(f'/home/dennis/Dev/PythonDev/MistralPython/Data/data_07_12_2020/{items}', 'r'), delimiter = ',') for items in data_files]

#Creation of an array containing the voltages
C1_sonde_fenetre = [(data[0][i][1]) for i in range(len(data[0]))]
C2_smartprobe = [(data[1][i][1] ) for i in range(len(data[0]))]
C1_t = [(data[0][i][0]) for i in range(len(data[0]))]

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def fft_langmuir(x, s1, s2, N):
    T_0 = x[1] - x[0]
    T = np.round(T_0, decimals=7)
    global fs
    fs = 1/T
    freq = np.linspace(0,fs/2,int(len(s1[:N])/2))
    s1f =  np.fft.rfft(s1[:N])
    # ~ print('F0 =', np.where(np.abs(s1f[1:]) == max(np.abs(s1f[1:]))))
    s2f =  np.fft.rfft(s2[:N])
    # ~ f0 = freq(np.where(np.max(s1f)))
    f0_index = np.where(np.abs(s1f[1:]) == np.max(np.abs(s1f[1:])))
    print('f0_index =',f0_index)
    global f0
    f0 = freq[f0_index]
    print('f0 =',f0)
    plt.plot(freq, np.abs(s1f[1:]))
    plt.plot(freq, np.abs(s2f)[1:])
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.title("FFT from the langmuir probe")
    plt.show()


fft_langmuir(C1_t, C1_sonde_fenetre, C2_smartprobe, 1000)

def run():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import freqz
   	

    # Sample rate and desired cutoff frequencies (in Hz).
    lowcut = f0 + 200.
    highcut = f0 - 200.

    # Plot the frequency response for a few different orders.
    plt.figure(1)
    plt.clf()
    for order in [3, 6, 9]:
        b, a = butter_bandpass(lowcut, highcut, fs, order=order)
        w, h = freqz(b, a, worN=2000)
        plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="order = %d" % order)

    plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)],
             '--', label='sqrt(0.5)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Gain')
    plt.grid(True)
    plt.legend(loc='best')

    # Filter a noisy signal.
    T = 0.05
    nsamples = int(T * fs)
    t = np.linspace(0, T, nsamples, endpoint=False)
    a = 0.02
    f0 = 600.0
    x = 0.1 * np.sin(2 * np.pi * 1.2 * np.sqrt(t))
    x += 0.01 * np.cos(2 * np.pi * 312 * t + 0.1)
    x += a * np.cos(2 * np.pi * f0 * t + .11)
    x += 0.03 * np.cos(2 * np.pi * 2000 * t)
    plt.figure(2)
    plt.clf()
    plt.plot(t, x, label='Noisy signal')

    y = butter_bandpass_filter(x, lowcut, highcut, fs, order=6)
    plt.plot(t, y, label='Filtered signal (%g Hz)' % f0)
    plt.xlabel('time (seconds)')
    plt.hlines([-a, a], 0, T, linestyles='--')
    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc='upper left')

    plt.show()


run()
