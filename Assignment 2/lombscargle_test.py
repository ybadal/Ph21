import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize']=8,4
import scipy.signal as signal

Fs = 1500.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0.01,1.0,Ts) # time vector

y = 4*np.exp(-250*(t-0.5)**2) # gaussian with B=250, A=4

frq = np.linspace(0.001,75,15000)

pgram = signal.lombscargle(t, y, frq, normalize=True)

fig, ax = plt.subplots(2,1)
ax[0].plot(t,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[0].set_title('Signal')
ax[1].plot(frq, pgram,'r') # plotting the spectrum
ax[1].set_xlabel('f (Hz)')
ax[1].set_ylabel('$Power$')
ax[1].set_title('Lomb-Scargle Periodogram')

plt.tight_layout()
plt.savefig('gaussian_lombscargle.png')

