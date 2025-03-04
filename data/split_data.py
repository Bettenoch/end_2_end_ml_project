import numpy as np
from fetch_data import housing
from sklearn.model_selection import train_test_split

def shuffle_and_split_data(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    training_set_indices = shuffled_indices[:test_set_size]
    test_set_indices = shuffled_indices[test_set_size:]
    
    return np.iloc[training_set_indices], np.iloc[test_set_indices]
   #ILOC IS A PANDAS METHOD TO SELECT DATA USING INDEX-BASED SELECTION IE COLS AND ROWS

training_set, test_set = shuffle_and_split_data(housing, 0.2)

print (len(test_set))

#using scikit built in library 
training_set, test_set = train_test_split(housing, random_state=42, test_size=0.2)
