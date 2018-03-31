#Import Dependencies

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Importing CSV's
summer_df = pd.read_csv ("olympic_medalists.csv", encoding = "ISO-8859-1")
winter_df = pd.read_csv ("winter.csv", encoding = "ISO-8859-1")

#Merge Summer and Winter Olympic Information
SW_Merge = summer_df.merge(winter_df, on='Country')

SW_Merge.to_csv("Summer_and_Winter", encoding="ISO-8859-1", index=False)
