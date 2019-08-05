# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_data(path,encoding):
    data = pd.read_csv(path,encoding=encoding)
    return data

def plot_barchart_dictionary(x,y,x_rotation,y_label,title,figsize_x=10,figsize_y=10):
    
    y_pos = np.arange(len(y))

    plt.figure(figsize=(figsize_x,figsize_y))
    plt.bar(y_pos, y, align='edge',width=0.7, alpha=0.5)
    plt.xticks(y_pos, x,rotation=x_rotation)
    plt.ylabel(y_label)
    plt.title(title)

    plt.show()
    
def column_rename_firstvalue (df):
    new_headers = []
    for col in df.columns:
        first_valid_indx = df[col].first_valid_index()
        new_headers.append(df[col][first_valid_indx])
    return new_headers

