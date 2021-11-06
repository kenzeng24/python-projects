import numpy as np 
import pandas as pd 

def generate(n = 410):
    n = 410
    z = np.random.normal(size=(n, 8))
    noise_file  = "noise.csv" 
    pd.DataFrame(z).to_csv(noise_file, header=False)
    print(f'created: {noise_file}')

if __name__ == "__main__": 
    
    generate()