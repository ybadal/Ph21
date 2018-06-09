import interloper                                                                      
from pymc import MCMC                                                          
from pymc.Matplot import plot                                                  
from matplotlib.pyplot import hist2d                                           
import matplotlib.pyplot as plt                                                
                                                                               
M = MCMC(interloper)                                                                   
M.sample(iter = 500000, burn = 1000, thin = 5)                                  
print                                                                          
plot(M)                                                                        
M.alpha.summary()                                                              
M.beta.summary()                                                               
                                                                               
                                                                               
alpha_arr = M.trace('alpha')[:]                                                
beta_arr = M.trace('beta')[:]                                                  
                                                                               
                                                                               
H, xedges, yedges, img = hist2d(alpha_arr, beta_arr, 250)                      
extent = [yedges[0], yedges[-1], xedges[0], xedges[-1]]                        
fig = plt.figure()                                                             
ax = fig.add_subplot(1, 1, 1)                                                  
im = ax.imshow(H, cmap=plt.cm.hot, extent=extent)                              
fig.colorbar(im, ax=ax)                                                        
plt.axes().set_aspect(0.67)                                                    
plt.tight_layout(pad=0.3)                                                      
plt.savefig('interloper_gaussian_distant_high_iteration.png') 
plt.close()                                                                    

