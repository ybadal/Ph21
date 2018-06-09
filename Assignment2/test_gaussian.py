import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 8, 8

Fs = 150.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval set to L=1
t = np.arange(0,1,Ts) # time vector

y = 4*np.exp(-250*(t-0.5)**2) # gaussian with B=250, A=4

n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(n/2)] # one side frequency range

Y = np.fft.fft(y) # fft computing and normalization
Y_disp = Y[range(n/2)]/n

inv = np.fft.ifft(Y)

fig, ax = plt.subplots(4, 1)
ax[0].plot(t,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[0].set_title('Signal')
ax[0].set_aspect(0.032)

ax[1].plot(frq,Y_disp,'r') # plotting the spectrum
ax[1].set_xlabel(r'$f=\frac{k}{L}$ (Hz)')
ax[1].set_ylabel('$h_k$')
ax[1].set_title('Positive Spectrum (FFT)')
ax[1].set_aspect(12)

ax[2].plot(frq,abs(Y_disp),'r') # plotting the spectrum
ax[2].set_xlabel(r'$f=\frac{k}{L}$ (Hz)')
ax[2].set_ylabel('$|h_k|$')
ax[2].set_title('Positive Absolute Spectrum (FFT)')
ax[2].set_aspect(22)

ax[3].plot(t,inv)
ax[3].set_xlabel('Time')
ax[3].set_ylabel('Amplitude')
ax[3].set_title('Recovered Signal (Inverse FFT)')
ax[3].set_aspect(0.032)

plt.tight_layout()
plt.savefig('gaussian_signal.png')

print(Y_disp[0]) # check normalization
