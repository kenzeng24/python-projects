
# Author: Ken Zeng 
# Simulate financial index data from a 
# multivariate normal distribution

import numpy as np 
import pandas as pd 
from sklearn.decomposition import PCA

def normalize(x):
  	"""normalize each column of a dataframe"""
  	mu = np.mean(x, axis=0)
	sigma = np.std(x, axis=0)
	return (x-mu) / sigma, mu, sigma

def train(data):
	"""learn parameters theta from input data""" 
	x = df.values 
	pca = PCA(n_components=4)
	xnorm1, mean1, sigma1 = normalize(x**(1/3))
	xnorm2, mean2, sigma2 = normalize(pca.fit_transform(xnorm1))
	theta = {
		"eigen_basis":pca.components_, 
		"mean1":mean1, 
		"mean2":mean2, 
		"sigma1":sigma1,
		"sigma2":sigma2 		
	}
	return theta

def G(z, theta):
	"""simulate financial data from the input noise""" 
	xhat = z 
	xhat = xhat * theta["sigma2"] + theta["mean2"] 
	xhat = np.dot(xhat, theta["eigen_basis"] 
	xhat = xhat * theta["sigma1"] + theta["mean1"] 
	xhat = xhat**3 
	return xhat 


if __init__ == "__main__":
	
	# may need to edit this depending on the input
	data_path = "/data/train.csv"
  	
	# train theta parameters using train.csv 
	df = pd.read_csv(data_path, header=None, index_col=0)
	data = df.values
	theta = train(data)	 
	
	# generate simulated data using random noise 
	n = 410  
	filename = "Z.csv" 
	z = np.random.normal(size=(n, 4))
	output = G(z,theta)

	# save inputs and outputs as csv files 
	output_file = "output.csv"
	noise_file  = "noise.csv" 
	pd.DataFrame(z).to_csv(output_file) 
	pd.DataFrame(output).to_csv(noise_file)

