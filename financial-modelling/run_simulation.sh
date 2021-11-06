rm theta.npy 
rm noise.csv
rm output.csv

python3 generate_noise.py
python3 train_model.py
python3 main.py 
