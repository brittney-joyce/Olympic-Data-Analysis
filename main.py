#Import statements
import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

#Code Execution
#note for large files this will take a while and will take a lot of scrolling
#this code is used to traverse files and collect data
with open('Data/sports/hockey/hockey_ticket_master_pg0.json', encoding="UTF-8") as cf:
    data = json.loads(cf.read())
    pprint(data['_embedded']['events'][0])
