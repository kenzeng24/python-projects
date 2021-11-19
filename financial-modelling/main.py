import numpy as np 
import pandas as pd 
import scipy.stats as stats
import os 
import argparse 


def G(z, theta, h=0.1):
    """simulate financial data from the input noise""" 
    
    # convert first set of noise to uniform distribution
    # and then converting to integer to sample 
    index = theta["N"] * stats.norm.cdf(z[:,:4])
    index = index.astype(int)
    
    # sample from gaussian kernel using additional noise 
    n, _ = z.shape
    sampled = np.zeros((n,4))
    for i in range(4):
        sampled[:,i] = theta["distribution"][i][index[:,i]]
    xhat = sampled + np.sqrt(h) * z[:,4:]
    
    # to reverse the training process: 
    # we unnormalize and then reconstruct data 
    # using PCA components 
    xhat = xhat * theta["sigma2"] + theta["mean2"] 
    xhat = np.dot(xhat, theta["eigen_basis"]) 

    # unnormalize and then reverse cube root 
    xhat = xhat * theta["sigma1"] + theta["mean1"] 
    xhat = xhat**3 
    return xhat 


def main(noise_file = "noise.csv", 
         theta_file = "theta.npy",
         output_file = "generated_samples.csv", 
         scale=0.3):
    
    # check if the required files exist 
    for file in [noise_file, theta_file]:
        assert os.path.isfile(file), f"{file} not found"

    z = pd.read_csv(noise_file, header=None, index_col=None).values
    theta = np.load(theta_file, allow_pickle=True).tolist()
    output = G(z,theta, h=0.01)

    # save inputs and outputs as csv files 
    pd.DataFrame(output).to_csv(output_file, header=None, index=False)
    print(f'created: {output_file}')
    

if __name__ == "__main__":
    
    main()
                  