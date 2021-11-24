import numpy as np 
import pandas as pd 

def generate(n = 408, nfeatures=8):
    
    z = np.random.normal(size=(n, nfeatures))
    noise_file  = "noise.csv" 
    pd.DataFrame(z).to_csv(noise_file, header=False, index=False)
    print(f'created: {noise_file}')

if __name__ == "__main__": 
    
    generate()