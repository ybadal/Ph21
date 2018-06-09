import requests as req
import re
import string
import matplotlib.pyplot as plt

url = 'http://nesssi.cacr.caltech.edu/cgi-bin/getcssconedbid_release2.cgi'
form = {'Name': 'Her X-1', 'Rad': 0.1, 'DB': 'photcat', 'OUT': 'web', 'SHORT': 'short'}

r = req.post(url, data=form)
# print(r.text)
data = r.text.splitlines()
# print(data)


time = []
mag = []
mag_err = []

for i in data:
    if re.match('^<tr>', i):
        entry = i.strip().split('<td>')
        mag.append(float(entry[2].strip("'")))
        mag_err.append(float(entry[3].strip("'")))
        time.append(float(entry[6].rstrip('</tr>').strip("'")))


plt.figure()
plt.xlabel('Time (MJD)')
plt.ylabel('Magnitude')
plt.errorbar(time, mag, yerr=mag_err, fmt='o', mfc='black', ms=2, mec='black', ecolor='red', capsize=2)
plt.savefig('Plot_1_1.png')


