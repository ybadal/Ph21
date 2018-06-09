import numpy as np
from numpy import random as rnd
from scipy.special import comb as choose
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib import rc
# rc('text', usetex=True)
# rc('font', family='serif')
# Same issue as before, rcParams interfered with pymc plot

def generate_data(n, alpha, beta):
    '''Generates position array x_k for the lighthouse problem, for n pulses 
    total from the lighthouse. We assume WLOG that x_k consists only of those
    flashes that reach a detector (pulses emitted at shore-bound azimuth'''
    theta = [rnd.uniform(0,2*np.pi) for i in range(0,n)]
    shore_bound = lambda th: th < np.pi / 2 or th > 3 * np.pi / 2
    xk = [beta*np.tan(theta_k) + alpha for theta_k in theta if shore_bound(
        theta_k)]

    return xk


def log_likelihood(x_k, alpha, beta):
    '''Log-likelihood function for position array x_k. For derivation of pdf
    w.r.t. position, see report.'''
    log_single = lambda xk, alpha, beta: np.log( (beta/(2*np.pi)) / 
            ((xk - alpha)**2 + beta**2) )

    log_array = np.sum([ log_single(xk, alpha, beta) for xk in x_k ])

    return log_array


def log_gaussian_prior(param, mean, std):
    '''Log-gaussian prior for param.'''
    gaussian = -(param - mean)**2 / (2* std**2)
    return gaussian


def log_posterior1(alpha, x_k, beta, mean, std):
    '''Un-normalized log-posterior for known beta, position array x_k, with
    Gaussian prior'''
    post = log_likelihood(x_k, alpha, beta) + log_gaussian_prior(alpha,
            mean, std)
    return post

def log_posterior2(alpha, beta, x_k, mean_alpha, std_alpha, mean_beta, 
        std_beta):
    '''Un-normalized log-posterior for position array x_k, with both alpha
    and beta unknown.'''
    post = log_likelihood(x_k, alpha, beta) + log_gaussian_prior(alpha,
            mean_alpha, std_alpha) + log_gaussian_prior(beta,
                    mean_beta, std_beta)
    return post


def plot_posterior1(alpha_arr, x_k, beta, mean, std, plot_label = None):
    '''Plot posterior distribution over alpha parameter array alpha_arr, 
    with known beta, for Gaussian prior with parameters mean, std.'''
    post_arr = [ log_posterior1(alpha, x_k, beta, mean, std) for alpha in 
            alpha_arr ]
    post_arr -= np.max(post_arr) # Normalizing posterior
    post_dist = np.exp(post_arr)
    plt.plot(alpha_arr, post_dist, label = plot_label)
    plt.legend(prop = {"size" : 11})


def plot_posterior2(alpha_arr, beta_arr, x_k, mean_alpha, std_alpha, 
        mean_beta, std_beta, plot_label = None):
    '''Plot posterior distribution over alpha and beta parameter arrays for
    Gaussian priors for both parameters.'''
    post_grid = [[ log_posterior2(alpha, beta, x_k, mean_alpha, std_alpha,
        mean_beta, std_beta) for alpha in alpha_arr] for beta in beta_arr ]
    post_grid -= np.max(post_grid) # Normalizing
    post_dist = np.exp(post_grid)
    plt.imshow(post_dist, extent = [np.min(alpha_arr), np.max(alpha_arr), 
        np.min(beta_arr), np.max(beta_arr)])
    plt.title(plot_label)
    plt.colorbar()


if __name__ == "__main__":
    
    # Lighthouse problem for known beta

    # Set real parameters
    alpha = 1.0
    beta = 1.5

    for std in [0.3, 0.1, 0.05]:
        for n in [10, 50, 250]:
            mean = 0.9 
            data = generate_data(n, alpha, beta)
            alpha_arr = np.linspace(0, 2, 200)
            plot_posterior1(alpha_arr, data, beta, mean, std,
                    plot_label = ("$n$ = %i, $\\langle x_k \\rangle$ = %f" 
                        % (n, np.mean(data)))
                    )
        plt.axes().set_aspect(1)
        plt.title(
                "$\\alpha$ = %f, $\\beta$ = %f, $\\mu$ = %f, $\\sigma$ = %f" 
                % (alpha, beta, mean, std)
                )
        plt.tight_layout()
        plt.savefig("lighthouse_alpha_sig_%s.png" % std)
        plt.close()

    # Lighthouse problem for unknown alpha, beta
    for std in [0.3, 0.1]:
        for n in [10, 50, 250]:
            mean_alpha = 0.9
            mean_beta = 1.6
            data = generate_data(n, alpha, beta)
            alpha_arr = np.linspace(0, 2, 200)
            beta_arr = np.linspace(0, 3, 300)
            plt.jet()
            plot_posterior2(alpha_arr, beta_arr, data, mean_alpha, std, 
                    mean_beta, std
                    )
            plt.axes().set_aspect(0.67)
            plt.title(
                    ("$\\alpha$ = %f, $\\beta$ = %f, $\\mu_{\\alpha}$ = %f, " 
                        + "$\\mu_{\\beta}$ = %f, \n" +
                        "$\\sigma_{\\alpha} = \\sigma_{\\beta}$ = %f, " + 
                        "n = %i")
                    % (alpha, beta, mean_alpha, mean_beta, std, n)
                    )
            plt.tight_layout()
            plt.savefig("lighthouse_contour_sig_%s_%s.png" % (std, n))
            plt.close()

