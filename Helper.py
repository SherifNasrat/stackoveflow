# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_data(path,encoding):
    """Reads a CSV file into a Pandas DataFrame and returns the DataFrame with specified encoding.

    Parameters:
    path (string): Path to the CSV file to be read.
    encoding (string): The type of encoding to read the file with.

    Returns:
    Pandas DataFrame containing the CSV data with the specified encoding.

   """

    data = pd.read_csv(path,encoding=encoding)
    return data

def plot_barchart_dictionary(x,y,x_rotation,y_label,title,figsize_x=10,figsize_y=10):
    """This function draws a bar chart of the given dictionary keys on the x-axis and values on the y-axis.

    Parameters:
    x (array_like): Labels to be added on the x-axis of the bar chart.
    y (array_like): The values that will be mapped to each label on the x-axis.
    x_rotation (int): The rotation of the labels on the x-axis.
    y_label (string): The label that will appear on the y-axis.
    title (string): The title of the figure.
    figsize_x (int): The width of the window/figure, default=10.
    figsize_y (int): The height of the window/figure, default=10.

    Returns:
    Pandas DataFrame containing the CSV data with the specified encoding.

   """
    y_pos = np.arange(len(y))

    plt.figure(figsize=(figsize_x,figsize_y))
    plt.bar(y_pos, y, align='edge',width=0.7, alpha=0.5)
    plt.xticks(y_pos, x,rotation=x_rotation)
    plt.ylabel(y_label)
    plt.title(title)

    plt.show()
    
def column_rename_firstvalue (df):
    """This function takes a Pandas DataFrame and returns a list with the first valid entry in each column for renaming later.

    Parameters:
    df (Pandas DataFrame): The dataframe with the columns that you need to rename.

    Returns:
    list containing the first valid entry in each column.

   """

    new_headers = []
    for col in df.columns:
        first_valid_indx = df[col].first_valid_index()
        new_headers.append(df[col][first_valid_indx])
    return new_headers

