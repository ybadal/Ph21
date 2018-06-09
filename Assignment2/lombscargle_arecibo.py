import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize']=8,8
from astropy.stats import LombScargle as ls

with open("arecibo1.txt","r") as data:
    y = []
    for line in data:
        y.append(np.float64(line))

Fs = 1000.0 # len(y);  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0,len(y)*Ts,Ts) # time vector

frq, pgram = ls(t, y).autopower(minimum_frequency=0.01, maximum_frequency=500)

frq2, pgram2 = ls(t, y).autopower(minimum_frequency=136, maximum_frequency=138)

fig, ax = plt.subplots(3,1)
ax[0].plot(t,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[0].set_title('Signal')
ax[1].plot(frq, pgram,'r') # plotting the spectrum
ax[1].set_xlabel('f (Hz)')
ax[1].set_ylabel('Power')
ax[1].set_title('Lomb-Scargle Periodogram')
ax[2].plot(frq2, pgram2, 'r') # zooming in
ax[2].set_xlabel('f (Hz)')
ax[2].set_ylabel('Power')
ax[2].set_title('Periodogram around expected signal frequency')

plt.tight_layout()
plt.savefig('arecibo_lombscargle.png')

