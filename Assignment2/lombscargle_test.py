import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize']=8,4
from astropy.stats import LombScargle as ls

Fs = 150.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0.01,1.0,Ts) # time vector

y = 3*np.cos(2*np.pi*4*t) # sine wave with freq 4 Hz
# y = 4*np.exp(-250*(t-0.5)**2) # gaussian with B=250, A=4

frq, pgram = ls(t, y).autopower(minimum_frequency=0.01, maximum_frequency=75)

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
plt.savefig('sine_lombscargle.png')

