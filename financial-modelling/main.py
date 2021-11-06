import numpy as np 
import pandas as pd 
import os 
import train_model

def main():
    
    # check if the required files exist 
    noise_file = "noise.csv" 
    theta_file = "theta.npy"
    for file in [noise_file, theta_file]:
        assert os.path.isfile(file), f"{file} not found"

    z = pd.read_csv(noise_file, header=None, index_col=0).values
    theta = np.load("theta.npy", allow_pickle=True).tolist()
    output = train_model.G(z,theta)

    # save inputs and outputs as csv files 
    output_file = "output.csv"
    pd.DataFrame(output).to_csv(output_file, header=None)
    print(f'created: {output_file}')
    

if __name__ == "__main__":
    
    main()
                  