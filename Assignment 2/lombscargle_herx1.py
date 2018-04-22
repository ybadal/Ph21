import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize']=8,5
import scipy.signal as signal
from astropy.io.votable import parse_single_table as parse

votable = parse("result_web_fileT5Mkdp.vot", pedantic=False)
y = np.concatenate(votable.array['Mag'])
t = np.concatenate(votable.array['ObsTime'])

frq = np.linspace(0.001,2,50000)
frq2 = np.linspace(0.001,0.8,50000)

pgram = signal.lombscargle(t, y, frq, normalize=True)
pgram2 = signal.lombscargle(t, y, frq2, normalize=True)

fig, ax = plt.subplots(2,1)
ax[0].plot(frq, pgram,'r') # plotting the spectrum
ax[0].set_xlabel(r'$f (Day^{-1})$')
ax[0].set_ylabel('Power')
ax[0].set_title('Lomb-Scargle Periodogram')
ax[1].plot(frq2, pgram2,'r') # plotting the spectrum
ax[1].set_xlabel(r'$f (Day^{-1})$')
ax[1].set_ylabel('Power')
ax[1].set_title('Lomb-Scargle Periodogram around expected frequency')

plt.tight_layout()
plt.savefig('her_x-1_lombscargle.png')
