import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import matplotlib.ticker as plticker
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

results = pd.read_csv('/Users/ravindraprasad/Ravindra/FIFA2018/Datasets/results.csv')
world_cup = pd.read_csv('/Users/ravindraprasad/Ravindra/FIFA2018/Datasets/World Cup 2018 Dataset.csv')

for i in range (len(results['home_team'])):
    winner.append('Draw')
   
    if (results['home_score'][i] > results ['away_score'] [i]):
    
        winner.append(results ['home_team'][i])
    elif (results['home_score'][i] < results ['away_score'] [i]):
        winner.append(results ['away_team'][i])
        
