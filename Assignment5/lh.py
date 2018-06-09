import numpy as np
from pymc import Uniform, Cauchy, Normal, deterministic
from lighthouse import generate_data


# set true values of parameters
alphaTrue = 1.0
betaTrue = 1.5
n = 10000


# generate detector array
xk = generate_data(n, alphaTrue, betaTrue)


# parameter prior alpha
alpha = Uniform("alpha", lower = 0.0, upper = 2.0)
# alpha = Normal("alpha", mu = 0.9, tau = (1 / (0.3)**2))
# alpha = Normal("alpha", mu = 0.9, tau = (1 / (0.05)**2))



# parameter prior beta
beta = Uniform("beta", lower = 0.0, upper = 2.0)
# beta = Normal("beta", mu = 1.6, tau = (1 / (0.3)**2))
# beta = Normal("beta", mu = 1.6, tau = (1 / (0.05)**2))


# model: flash arrival points
xkModel = Cauchy("xkModel", alpha = alpha, beta = beta, value = xk,
        observed = True)

