import numpy as np
from numpy import random as rnd
from scipy.special import comb as choose
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)
rc('font', family='serif')


# Start by writing a function to calculate the likelihood function
def likelihood(n, h, p):
    '''Returns the probability of h heads in n trials, with probability of heads being p'''
    return choose(n, h, exact=True)*(p**h)*((1-p)**(n-h))


# Write function to find posterior, assuming constant prior
def constant_posterior(n, h, p, c):
    '''Returns the posterior for a constant prior c'''
    return c*likelihood(n, h, p)


# Write function to find posterior, assuming Gaussian prior
def gaussian_posterior(n, h, p, mean, var):
    '''Returns the posterior for a Gaussian prior'''
    return norm(mean, var).pdf(p)*likelihood(n, h, p)


# Write function to provide coin toss data
def toss(p, n):
    '''Returns the number of heads in n tosses, with probability of heads p'''
    return sum(rnd.binomial(1, p, n))


def plot_constant(n, p, c, plot_label=None):
    '''Saves a plot of the posterior function for a coin toss, assuming contant prior'''
    h_array = np.linspace(0, 1, 200)
    post = constant_posterior(n, toss(p, n), h_array, c) 
    log_post_arr = [np.log(k) for k in post]
    log_post_arr -= np.max(log_post_arr) # Normalization
    post_arr = np.exp(log_post_arr)
    plt.plot(h_array, post_arr, label = plot_label)
    plt.legend(prop={"size" : 11})


def plot_gaussian(n, p, mean, var, plot_label=None):
    '''Saves a plot of the posterior function for a coin toss, assuming Gaussian prior'''
    h_array = np.linspace(0, 1, 200)
    post = gaussian_posterior(n, toss(p, n), h_array, mean, var)
    log_post_arr = [np.log(k) for k in post]
    log_post_arr -= np.max(log_post_arr)
    post_arr = np.exp(log_post_arr)
    plt.plot(h_array, post_arr, label = plot_label)
    plt.legend(prop={"size" : 11})

if __name__ == "__main__":
    for p in [0.3, 0.5, 0.9]:
        for n in [10, 50, 200]:
            plot_constant(n, p, 0.1, plot_label = "n = %i" % n)
        plt.xlabel('H')
        plt.ylabel('P(X|D)')
        plt.title('Actual H = %s, Constant Prior' %  p)
        plt.tight_layout()
        plt.savefig('const_%s.png' % p)
        plt.close()

    for p in [0.3, 0.5, 0.9]:
        for offset in [0.01, 0.1, 0.3]:
            for var in [0.1, 0.3]:
                for n in [10, 50, 200]:
                    mean = p - offset
                    plot_gaussian(n, p, mean, var, plot_label = "n = %i" % n)
                plt.xlabel('H')
                plt.ylabel('P(X|D)')
                plt.title(r'Actual H = %s, $\mu = %s$, $\sigma = %s$, Gaussian Prior' % (p, mean, var))
                plt.tight_layout()
                plt.savefig('gaussian_%s_%s_%s.png' % (p, mean, var))
                plt.close()
