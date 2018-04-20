import numpy as np
import matplotlib.pyplot as plt

Fs = 150.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval set to L=1
t = np.arange(0,1,Ts) # time vector

y = 3*np.cos(2*np.pi*4*t + 0.4) + 1 # frequency set to 4/L=4

n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(n/2)] # one side frequency range

Y = np.fft.fft(y)/n # fft computing and normalization
Y_disp = Y[range(n/2)]

inv = np.fft.ifft(Y)

fig, ax = plt.subplots(3, 1)
ax[0].plot(t,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[0].set_title('Signal')
ax[1].plot(frq,abs(Y_disp),'r') # plotting the spectrum
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')
ax[1].set_title('Positive Spectrum (FFT)')
ax[2].plot(t,inv)
ax[2].set_xlabel('Time')
ax[2].set_ylabel('Amplitude')
ax[2].set_title('Recovered Signal (Inverse FFT)')
plt.tight_layout()
plt.savefig('cosine_signal.png')
