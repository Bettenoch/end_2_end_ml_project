import numpy as np
from fetch_data import housing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
import pandas as pd

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

#splitting by stratified sampling we will choose median income to represent well

# first we will create an income category 

housing["income_cat"] = pd.cut(housing["median_income"], bins=[0., 1.5, 3.0, 4.5, 6., np.inf], labels=[1, 2, 3, 4, 5])


#split the data using income_cat

splitter = StratifiedShuffleSplit(n_splits=10, test_size=0.2, random_state=42)
splits =[]

for train_index, test_index in splitter.split(housing, housing["income_cat"]):
    strat_train_set_n = housing.iloc["train_index"]
    strat_test_set_n = housing.iloc["test_index"]
    splits.append([strat_train_set_n, strat_test_set_n])
    
strat_train_set, strat_test_set = splits[0]