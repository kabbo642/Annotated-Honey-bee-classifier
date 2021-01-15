# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 21:59:30 2020

@author: Kabbo
"""
""" Importing the libraries """
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import tensorflow 
import glob
from PIL import Image
import sys

# Using tensorflow backend

IMAGE_PATH = "D:\Annotated Honey Bees\The BeeImage Dataset Annotated Honey Bee Images "
IMAGE_WIDTH = 100
IMAGE_HEIGHT = 100
IMAGE_CHANNELS = 3
RANDOM_STATE = 2018
TEST_SIZE = 0.2
VAL_SIZE = 0.2
CONV_2D_DIM_1 = 16
CONV_2D_DIM_2 = 16
CONV_2D_DIM_3 = 32
CONV_2D_DIM_4 = 64
MAX_POOL_DIM = 2
KERNEL_SIZE = 3
BATCH_SIZE = 32
NO_EPOCHS_1 = 5
NO_EPOCHS_2 = 15
NO_EPOCHS_3 = 50
PATIENCE = 5
VERBOSE = 1

def missing_data(data):
    """ This function shows the missing data of the collumns 
    Args: This function takes a dataframe 
    Returns: This function returns a dataframe with total missing values with percentage for every column """
    total = data.isnull().sum().sort_values(ascending = False)
    percent = (data.isnull().sum()/data.isnull().count()*100).sort_values(ascending = False)
    return pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
"""os.listdir("D:\Annotated Honey Bees\The BeeImage Dataset Annotated Honey Bee Images\..")


bee_data = pd.read_csv("Dataset_temp1.csv")
print(missing_data(bee_data))
# there is no missing values
image_files_2 =glob.glob("D:\Annotated Honey Bees\The BeeImage Dataset Annotated Honey Bee Images\bee_imgs\bee_imgs\*.png")

image_files = list(os.listdir(IMAGE_PATH))
print("Number of image files: {}".format(len(image_files)))

#data_dir = '../input'
img_dir = os.path.join(IMAGE_PATH, 'bee_imgs', 'bee_imgs')
data_csv = os.path.join(IMAGE_PATH, 'bee_data.csv')
data = pd.read_csv(data_csv)
print('Number of rows:', len(data))"""

bee_data = pd.read_csv("bee_data.csv")
file_name = bee_data['file']

directory = "D:\Annotated Honey Bees\The BeeImage Dataset Annotated Honey Bee Images\bee_imgs\bee_imgs"
image_list = []
for filename in glob.glob('D:\Annotated Honey Bees\The BeeImage Dataset Annotated Honey Bee Images\bee_imgs\bee_imgs/*.png'): #assuming gif
    im=Image.open(filename)
    image_list.append(im)

def get_image(row_id, root="bee_imgs\bee_imgs\.."):
    """
    Converts an image number into the file path where the image is located, 
    opens the image, and returns the image as a numpy array.
    """
    filename = str(row_id)
    file_path = os.path.join(root, filename)
    img = Image.open(file_path)
    return np.array(img)
plt.imshow(get_image(file_name))
plt.show()


