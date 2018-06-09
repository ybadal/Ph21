import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize']=8,5
from astropy.stats import LombScargle as ls
from astropy.io.votable import parse_single_table as parse

votable = parse("result_web_fileT5Mkdp.vot", pedantic=False)
y = np.concatenate(votable.array['Mag'])
t = np.concatenate(votable.array['ObsTime'])
dy = np.concatenate(votable.array['Magerr'])

frq, pgram = ls(t, y, dy).autopower(minimum_frequency=0.01, maximum_frequency=20)
frq2, pgram2 = ls(t, y, dy).autopower(minimum_frequency=0.01, maximum_frequency=1)
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

x1data = np.dstack((t, y, dy))
np.savetxt("Her_X-1_data.txt", x1data[0], delimiter=" ")
