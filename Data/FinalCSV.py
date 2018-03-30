#Import Dependencies

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Importing CSV's
summer_df = pd.read_csv ("summer.csv", encoding = "ISO-8859-1")
winter_df = pd.read_csv ("winter.csv", encoding = "ISO-8859-1")
dictionary_df = pd.read_csv ("dictionary.csv", encoding = "ISO-8859-1")

#Merge Summer and Winter Olympic Information
SW_Merge = summer_df.append(winter_df)

#Adding Country Name to Merged CSV

SW_Merge['Country_Name'] = ""

#Incomplete Just here for show
