import numpy as np
import math
import matplotlib.pyplot as plt
from astropy.stats import LombScargle


filename = 'Her_X-1_data.txt'
number_bins = 25


def periodogram(filenam):
    """Takes file filename and outputs best period with automatically determined frequency grid."""
    time, magnitude, err = np.loadtxt(filenam, dtype='float', comments='%').T
    frequency, power = LombScargle(time, magnitude, err).autopower(minimum_frequency=0.01, maximum_frequency=20)
    period = 1/frequency[np.argmax(power)]
    print period
    return period


def floatList(lst):
    """Converts a list of strings into a list of floats (if possible)."""
    for i in range(len(lst)):
        lst[i] = float(lst[i])


def bin_number(time, period, numb_bins):
    """Takes as argument time value, period, and number of bins required and returns the bin number of that time
    value."""
    ph = time/period
    phase = ph % 2
    bin_value = (phase * float(numb_bins)/2)
    bin_num = int(bin_value)
    return bin_num


def folding(filenam, period, numb_bins):
    """Folds lightcurve data from a file and returns a list of folded data."""
    data_file = open(filenam, "r")
    folded_list = [0]*numb_bins
    weights = [0]*numb_bins
    binErr = [0]*numb_bins

    for line in data_file:
        data = line.split()
        floatList(data)
        time = data[0]
        amplitude = data[1]
        err = data[2]
        weight = float(err) ** -2
        bin_num_data = bin_number(float(time), float(period), number_bins)
        folded_list[bin_num_data] += amplitude * weight  # Weighs amplitude by error
        weights[bin_num_data] += weight

    for i in range(len(weights)):
        if weights[i] != 0:
            folded_list[i] /= weights[i]
            binErr[i] = math.sqrt(1.0/weights[i])  # Calculates bin errors
        else:
            folded_list[i] = float('NaN')

    return folded_list, binErr


def plotTuple(filenam, period, numb_bins):
    """Returns a list of (bin number, value, error) tuples for the folded lightcurve."""
    plot = [(0, 0, 0)]*numb_bins
    folded_list, binErr = folding(filenam, period, numb_bins)
    for i in range(numb_bins):
        plot[i] = (i, folded_list[i], binErr[i])
    return plot


def plotCurve(filenam, period, numb_bins):
    """Plots the list of tuples for the folded lightcurve."""
    folded_list = plotTuple(filenam, period, numb_bins)
    x, y, z = zip(*folded_list)

    plt.errorbar(x, y, yerr=z, fmt='o', mfc='black', ms=2, mec='black', ecolor='red',capsize=2)
    plt.gca().invert_yaxis()
    plt.xlabel('Phased Time (MJD)')
    plt.ylabel('Magnitude')
    plt.savefig('folded_her_x-1.png')


best_period = periodogram(filename)
plotCurve(filename, best_period, number_bins)
