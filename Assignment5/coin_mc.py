import coin
from pymc import MCMC
from pymc.Matplot import plot


# Run MCMC
nChains = 10
M = MCMC(coin)
M.sample(iter = 1000, burn = 0, thin = 1)
print
plot(M)
M.pHeadsEst.summary()

