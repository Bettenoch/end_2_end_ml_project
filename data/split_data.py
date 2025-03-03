import numpy as np
from fetch_data import housing

def shuffle_and_split_data(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio) 
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices] #ILOC IS A PANDAS METHOD TO SELECT DATA USING INDEX-BASED SELECTION IE COLS AND ROWS

training_set, test_set = shuffle_and_split_data(housing, 0.2)

print (len(test_set))