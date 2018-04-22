import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 8, 8

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
zoom_Y= Y_disp[(peak_index - 25):(peak_index + 25)]

fig, ax = plt.subplots(4, 1)
ax[0].plot(t,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[0].set_title('Signal')

ax[1].plot(frq1,abs(Y_disp),'r') # plotting the spectrum
ax[1].set_xlabel(r'$f=\frac{k}{L}$ (Hz)')
ax[1].set_ylabel('$|h_k|$')
ax[1].set_title('Positive Absolute Spectrum (FFT)')

ax[2].plot(zoom_frq,np.real(zoom_Y))
ax[2].set_xlabel(r'$f=\frac{k}{L}$ (Hz)')
ax[2].set_ylabel('$h_k$')
ax[2].set_title('Positive Spectrum near peak (Real part plotted)')

ax[3].plot(zoom_frq,abs(zoom_Y))
ax[3].set_xlabel(r'$f=\frac{k}{L}$ (Hz)')
ax[3].set_ylabel('$|h_k|$')
ax[3].set_title('Positive Absolute Spectrum near peak')

plt.tight_layout()
plt.savefig('arecibo_plot.png')

print(peak)

fft_data = np.dstack((zoom_frq,abs(zoom_Y)))  # saving FFT to file for analysis in CurveFit
# print(fft_data[0])
np.savetxt("fft_data.dat", fft_data[0], delimiter=" ", header="Frequency(Hz) |h_k|", comments="S")

raw_fft = np.dstack((frq1, abs(Y_disp)))
np.savetxt("full_fft.csv", raw_fft[0], delimiter=",", header="Frequency(Hz), |h_k|", comments="")

non_normalized_fft = np.dstack((frq,abs(Y)))
np.savetxt("non_normalized_fft.csv", non_normalized_fft[0], delimiter=",", header="Frequency (Hz), |h_k|", comments="")

