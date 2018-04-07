import matplotlib.pyplot as plt
from astropy.io.votable import parse_single_table as parse1

votable = parse1("result_web_fileT5Mkdp.vot", pedantic=False)


mag = votable.array['Mag']
mag_err = votable.array['Magerr']
time = votable.array['ObsTime']


plt.figure()
plt.xlabel('Time (MJD)')
plt.ylabel('Magnitude')
plt.errorbar(time, mag, yerr=mag_err, fmt='o', mfc='black', ms=2, mec='black', ecolor='red', capsize=2)
plt.savefig('Plot_1_2.png')

