import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 8,5

with open("arecibo1.txt","r") as data:
    y = []
    for line in data:
        y.append(np.float64(line))

Fs = 1000.0 # len(y);  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0,len(y)*Ts,Ts) # time vector

n = len(y) # length of the signal
k = np.arange(-n/2,n/2)
T = n/Fs
frq = k/T # two sides frequency range
frq1 = frq[(n/2):] # one side frequency range

Y = np.fft.fft(y) # fft computing and normalization
Y_disp = Y[range(n/2)]/n

peak_index = np.argmax(abs(Y_disp))
peak = frq1[peak_index]

zoom_frq = frq1[(peak_index - 25):(peak_index + 25)]
zoom_Y = Y_disp[(peak_index - 25):(peak_index + 25)]

# plot fft and gaussians to test dt

fig, ax = plt.subplots(1,1)
ax.plot(zoom_frq, np.real(zoom_Y), label = "FFT")

t0 = t[n/2] # t_0 center the Gaussian

for dt in [t0/2.0, t0/4.0, t0/8.0, t0/16.0]:
    h = np.exp(-(t - t0)**2 / (dt)**2)
    Fh = np.fft.fft(h)/n
    zoom_Fh = 0.5*np.concatenate((Fh[-26:],Fh[:24]))
    ax.set_xlabel(r'$f=\frac{k}{L}$ (Hz)')
    ax.set_ylabel('$h_k$')
    ax.plot(zoom_frq, zoom_Fh.real,label = (r"$\Delta t = %f \ \mathrm{s}$" % dt))
    ax.legend(prop = {"size" : 16})

plt.tight_layout()
plt.savefig('dt_compare_others.png')

