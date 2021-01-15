# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 19:41:45 2020

@author: Kabbo
"""
"*************** pre-processing ***************"
"*************** Importing Libraries **********"
# used to change filepaths
import os

import matplotlib as mlp
import matplotlib.pyplot as plt
from IPython.display import display

#%matplotlib inline

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# import Image from PIL
# ... YOUR CODE FOR TASK 1 ...
from PIL import Image



dataset_1 = pd.read_csv("bee_data.csv")
# first 10 rows of the data set
print(dataset_1.head())
# the shape of the dataset
print(dataset_1.shape)
# index of the dataset
print(dataset_1.index)
# the columns of the dataset
print(dataset_1.columns)
# checking for missing values
print(dataset_1.isnull().sum())
# checking the file column of the dataset
print(dataset_1.info)
# describing the dataset
print(dataset_1.describe)
# In dataset_2  subspicies value is -1
dataset_2 = dataset_1[dataset_1["subspecies"] == '-1']
print(dataset_1[dataset_1["subspecies"] == '-1'].count())
print( dataset_2['subspecies'].describe)
# dataset with out the non existing subspecies 
dataset_3 = dataset_1[dataset_1["subspecies"] != '-1']

" Now we will see how photos we can use with the appropriate data " 


dataset_3.to_csv(r'D:\Annotated Honey Bees\The BeeImage Dataset Annotated Honey Bee Images\Dataset_temp1.csv')
