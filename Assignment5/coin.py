import numpy as np
from pymc import Uniform, Binomial, Normal, deterministic
from bayesian import toss


# Set parameter values
pHeads = 0.4
nTosses = 1000


# Generate coin data
nHeads = toss(pHeads, nTosses)


# Parameter prior
# pHeadsEst = Normal("pHeadsEst", mu = 0.5, tau = (1/(0.05)**2))
# pHeadsEst = Normal("pHeadsEst", mu = 0.5, tau = (1/(0.2)**2))
# pHeadsEst = Normal("pHeadsEst", mu = 0.8, tau = (1/(0.05)**2))
# pHeadsEst = Normal("pHeadsEst", mu = 0.8, tau = (1/(0.2)**2))
pHeadsEst = Uniform("pHeadsEst", lower = 0.0, upper = 1.0)


# Model
nHeadsModel = Binomial("nHeadsModel", n = nTosses, p = pHeadsEst,
        value = nHeads, observed = True)

