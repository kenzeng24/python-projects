import numpy as np 
import pandas as pd 

if __name__ == "__main__": 
    
    n = 410
    z = np.random.normal(size=(n, 4))
    noise_file  = "noise.csv" 
    pd.DataFrame(z).to_csv(noise_file, header=False)