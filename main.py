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
    # pprint(data['_embedded']['events'][0])
    for entry in data['_embedded']['events']:
        print(entry['name'])
        print("Min Ticket Price: {} \n Max Ticket Price: {}".format(entry['priceRanges'][0]['min'], entry['priceRanges'][0]['max']))
