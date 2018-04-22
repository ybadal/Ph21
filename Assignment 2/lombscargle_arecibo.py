import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize']=8,8
import scipy.signal as signal

with open("arecibo1.txt","r") as data:
    y = []
    for line in data:
        y.append(np.float64(line))

Fs = 1000.0 # len(y);  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0,len(y)*Ts,Ts) # time vector

frq = np.linspace(0.001,500,50000)

pgram = signal.lombscargle(t, y, frq, normalize=True)

fig, ax = plt.subplots(3,1)
ax[0].plot(t,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[0].set_title('Signal')
ax[1].plot(frq, pgram,'r') # plotting the spectrum
ax[1].set_xlabel('f (Hz)')
ax[1].set_ylabel('Power')
ax[1].set_title('Lomb-Scargle Periodogram')

frq2 = np.linspace(100,150,50000)
pgram2 = signal.lombscargle(t, y, frq2, normalize=True)

ax[2].plot(frq2, pgram2, 'r') # zooming in
ax[2].set_xlabel('f (Hz)')
ax[2].set_ylabel('Power')
ax[2].set_title('Periodogram around expected signal frequency')

plt.tight_layout()
plt.savefig('arecibo_lombscargle.png')
