# Simulating Financial Data 

## Context 

In the last two decades, the increasing number of shocks and financial crises has been a major issue for the financial risk management teams.

Among the wide range of exercises in this field, Stress tests have become a main guideline for the regulator in order to assess the banking system resilience against the realizations of various categories of risk (market, credit, operational, climate, etc). The main challenge is to simulate unfavorable extreme (but plausible) negative returns similar to a historical dataset.

## Task 

This is an unsupervised learning problem: Given real data from stock market indexes that will act as a train dataset, the task is to learn a generative model that simulates synthetic stock market indexes.

## Model Training 

In order to simulate new data from our model: 

```bash  
python3 train_model.py 
python3 generate_noise.py
python3 main.py
```

This will generate the following three files. If these files alread exist, then the our scripts will overwrite the existing files. 
```
theta.npy 
noise.csv
output.csv
```

To Generate a new batch of sample datapoints, you only need to run: 
```bash
python3 generate_noise.py
python3 main.py
```




 
