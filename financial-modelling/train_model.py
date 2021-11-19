# Author: Ken Zeng 
# Simulate financial index data from a 
# multivariate normal distribution

import numpy as np 
import pandas as pd 
import scipy.stats as stats
import os 
from sklearn.decomposition import PCA


def normalize(x):
    """normalize each column of a dataframe"""
    
    mu = np.mean(x, axis=0)
    sigma = np.std(x, axis=0)
    return (x-mu) / sigma, mu, sigma


def train(data):
    """learn parameters theta from input data""" 
    
    pca = PCA(n_components=4)

    # cube root data to make values closer to a MVN 
    # Then apply PCA to remove correlation between different features 
    xnorm1, mean1, sigma1 = normalize(data**(1/3))
    xnorm2, mean2, sigma2 = normalize(pca.fit_transform(xnorm1))
    
    # save the distribution of the normalized values 
    N, _ = xnorm2.shape
    dist = {} 
    for i in range(4):
        dist[i] = np.sort(xnorm2[:,i])
    
    # ideally each column of xnorm2 should be independet
    # should be independent guassian distribution 
    theta = {
        "eigen_basis":pca.components_, 
        "mean1":mean1, 
        "mean2":mean2, 
        "sigma1":sigma1,
        "sigma2":sigma2,
        "distribution":dist,
        "N":N
    }
    return theta, xnorm2


def main():
    """ train the parameters theta reuqired for G
        and check that reconstruction error is negligible"""
    filename = "train.csv"
    assert os.path.isfile(filename), f"{filename} not found"

    # train theta parameters using train.csv 
    data = pd.read_csv(filename, header=None, index_col=0).values
    theta, xnorm2 = train(data)	 

    # save parameters theta as npy file 
    param_file = 'theta.npy'
    np.save(param_file,theta)
    print(f'created: {param_file}')


if __name__ == "__main__":
    
    main()
    


             

