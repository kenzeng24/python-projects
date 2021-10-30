# Author: Ken Zeng 
# Simulate financial index data from a 
# multivariate normal distribution

import numpy as np 
import pandas as pd 
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

    # ideally each column of xnorm2 should be independet
    # should be independent guassian distribution 
    theta = {
        "eigen_basis":pca.components_, 
        "mean1":mean1, 
        "mean2":mean2, 
        "sigma1":sigma1,
        "sigma2":sigma2
    }
    return theta, xnorm2


def G(z, theta):
    """simulate financial data from the input noise""" 
    xhat = z
    

    # to reverse the training process: 
    # we unnormalize and then reconstruct data 
    # using PCA components 
    xhat = xhat * theta["sigma2"] + theta["mean2"] 
    xhat = np.dot(xhat, theta["eigen_basis"]) 

    # unnormalize and then reverse cuberoot 
    xhat = xhat * theta["sigma1"] + theta["mean1"] 
    xhat = xhat**3 
    return xhat 


if __name__ == "__main__":
    
    filename = "train.csv"
    assert os.path.isfile(filename), f"{filename} not found"

    # train theta parameters using train.csv 
    data = pd.read_csv(filename, header=None, index_col=0).values
    theta, xnorm2 = train(data)	 

    # save parameters theta as npy file  
    np.save('theta.npy',theta)
    
    error = np.mean(abs(G(xnorm2,theta) - data))
    assert error < 1e-10, "reconstruction error is too large"
                  
             

