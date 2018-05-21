import numpy as np
from numpy import random as rnd
from scipy.special import comb as choose
from scipy.stats import norm
import matplotlib.pyplot as plt


# Start by writing a function to calculate the likelihood function
def likelihood(n, h, p):
    '''Returns the probability of h heads in n trials, with probability of heads being p'''
    return choose(n, h, exact=True)*(p**h)*((1-p)**(n-h))


# Write function to find posterior, assuming constant prior
def constant_posterior(n, h, p, c):
    '''Returns the posterior for a constant prior c'''
    return c*likelihood(n, h, p)


# Write function to find posterior, assuming Gaussian prior
def gaussian_posterior(n, h, p, c, mean, var):
    '''Returns the posterior for a Gaussian prior'''
    return norm(mean, var).pdf(p)*likelihood(n, h, p)


# Write function to provide coin toss data
def toss(p, n):
    '''Returns the number of heads in n tosses, with probability of heads p'''
    return sum(rnd.binomial(1, p, n))


def plot_constant(n, p, c):
    h_array = np.linspace(0, 1, 200)
    fig, ax = plt.subplots(1,1)
    ax.plot(h_array, constant_posterior(n, toss(p, n), h_array, c))
    ax.set_xlabel('H')
    ax.set_ylabel('P(X|D)')
    ax.set_title('n = %s, Actual H = %s' % (n, p))
    plt.tight_layout()
    plt.savefig('const_%s_%s.png' % (n, p))

plot_constant(100, 0.5, 0.3)

