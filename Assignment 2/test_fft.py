import numpy as np
import matplotlib.pyplot as plt


N = 200
T = 1.0/200
x = np.linspace(0.0, N*T, N)
y = 2*np.cos((2.0*np.pi)*x/200.0) + 3
yf = np.fft.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)


fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.show()
