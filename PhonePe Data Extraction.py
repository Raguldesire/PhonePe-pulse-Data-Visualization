pip install gitpython

import csv
import subprocess
import pandas as pd
import requests
import git
import pandas as pd
import os

os.system("git clone https://github.com/phonepe/pulse.git")

#OS-os library Python has a built-in os module with methods for interacting with the operating system,
    # like creating files and directories,
    # management of files and directories, input, output, environment variables, process management, etc.
#os.listdir()--os.listdir() method in python is used to get the list of all files and directories in the specified directory.
            #If we don’t specify any directory, then list of files and directories in the current working directory will be returned.
#os.path.join()--os.path.join() method in python is used to join two or more path components.
                  #Syntax: os.path.join(path, *paths)
                  #path: A path-like object representing a file system path.
                  #*path: A path-like object representing a file system path. It represents the path components to be joined.
                  #A path-like object is either a string or bytes object representing a path.
#os.path.isdir()--os.path.isdir() method in python is used to check whether the specified path is a directory or not.


import os
import json
import pandas as pd

root_dir = (r'/content/pulse/data')

# Creates an empty list
data_list = []

# step -1 :Loop over all the state folders
for state_dir in os.listdir(os.path.join(root_dir, '/content/pulse/data/aggregated/transaction/country/india/state')):
    state_path = os.path.join(root_dir, '/content/pulse/data/aggregated/transaction/country/india/state', state_dir)
    if os.path.isdir(state_path):

        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):

                # Loop over all the JSON files (one for each quarter)
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)
                            # Extract the data we're interested in
                            for transaction_data in data['data']['transactionData']:
                                row_dict = {
                                    'States': state_dir,
                                    'Transaction_Year': year_dir,
                                    'Quarters': int(json_file.split('.')[0]),
                                    'Transaction_Type': transaction_data['name'],
                                    'Transaction_Count': transaction_data['paymentInstruments'][0]['count'],
                                    'Transaction_Amount': transaction_data['paymentInstruments'][0]['amount']
                                }
                                data_list.append(row_dict)

# Convert list of dictionaries to dataframe
df1 = pd.DataFrame(data_list)


import os
import json
import pandas as pd

root_dir = '/content/pulse/data/aggregated/user/country/india/state'

# Initialize empty list to hold dictionaries of data for each JSON file
data_list = []

# Loop over all the state folders
for state_dir in os.listdir(root_dir):
    state_path = os.path.join(root_dir, state_dir)
    if os.path.isdir(state_path):

        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):

                # Loop over all the JSON files (one for each quarter)
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)
                            if isinstance(data,list):
                              data_list += data
                            else:
                              data_list.append(data)
    if data_list:
      df2 = pd.DataFrame(data_list)  #json_normalize converts a list of dictionaries to a dataframe,normalize the semi structured data into a flat table
      df2['subfolder'] = state_dir
      df2['subsubfolder'] = 'state'


import os
import json
import pandas as pd

root_dir = (r'/content/pulse/data')

# Initialize empty list to hold dictionaries of data for each JSON file
data_list = []

# Loop over all the state folders
for state_dir in os.listdir(os.path.join(root_dir, '/content/pulse/data/map/transaction/hover/country/india/state')):
    state_path = os.path.join(root_dir, '/content/pulse/data/map/transaction/hover/country/india/state', state_dir)
    if os.path.isdir(state_path):

        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):

                # Loop over all the JSON files (one for each quarter)
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)

                            # Extract the data we're interested in
                            for hoverDataList in data['data']['hoverDataList']:
                                row_dict = {
                                    'States': state_dir,
                                    'Transaction_Year': year_dir,
                                    'Quarters': int(json_file.split('.')[0]),
                                    'District': hoverDataList['name'],
                                    'Transaction_Type': hoverDataList['metric'][0]['type'],
                                    'Transaction_Count': hoverDataList['metric'][0]['amount']
                                }
                                data_list.append(row_dict)

# Convert list of dictionaries to dataframe
df3 = pd.DataFrame(data_list)

import os
import json
import pandas as pd

root_dir = '/content/pulse/data/map/user/hover/country/india/state'

# Initialize empty list to hold dictionaries of data for each JSON file
data_list = []

# Loop over all the state folders
for state_dir in os.listdir(root_dir):
    state_path = os.path.join(root_dir, state_dir)
    if os.path.isdir(state_path):

        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):

                # Loop over all the JSON files (one for each quarter)
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)

                            # Extract the data we're interested in
                            for district, values in data['data']['hoverData'].items():
                                row_dict = {
                                    'States': state_dir,
                                    'Transaction_Year': year_dir,
                                    'Quarter': int(json_file.split('.')[0]),
                                    'District': district,
                                    'RegisteredUsers': values['registeredUsers'],
                                }
                                data_list.append(row_dict)

# Convert list of dictionaries to dataframe
df4 = pd.DataFrame(data_list)

import os
import json
import pandas as pd

root_dir = (r'/content/pulse/data')

# Initialize empty list to hold dictionaries of data for each JSON file
data_list = []

# Loop over all the state folders
for state_dir in os.listdir(os.path.join(root_dir, '/content/pulse/data/top/transaction/country/india/state')):
    state_path = os.path.join(root_dir, '/content/pulse/data/top/transaction/country/india/state', state_dir)
    if os.path.isdir(state_path):

        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):

                # Loop over all the JSON files (one for each quarter)
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)

                            # Extract the data we're interested in
                            for districts in data['data']['districts']:
                                row_dict = {
                                    'States': state_dir,
                                    'Transaction_Year': year_dir,
                                    'Quarters': int(json_file.split('.')[0]),
                                    'District': districts['entityName'],
                                    'Transaction_Type': districts['metric']['type'],
                                    'Transaction_Count': districts['metric']['count'],
                                    'Transaction_Amount': districts['metric']['amount']
                                }
                                data_list.append(row_dict)

# Convert list of dictionaries to dataframe
df5 = pd.DataFrame(data_list)

import os
import json
import pandas as pd

root_dir = '/content/pulse/data/top/user/country/india/state'

# Initialize empty list to hold dictionaries of data for each JSON file
data_list = []

# Loop over all the state folders
for state_dir in os.listdir(root_dir):
    state_path = os.path.join(root_dir, state_dir)
    if os.path.isdir(state_path):

        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):

                # Loop over all the JSON files
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)

                            # Extract the data we're interested in
                            for district in data['data']['districts']:
                                row_dict = {
                                    'State': state_dir,
                                    'Transaction_Year': year_dir,
                                    'Quarters': int(json_file.split('.')[0]),
                                    'District': district['name'] if 'name' in district else district['pincode'],
                                    'RegisteredUsers': district['registeredUsers'],
                                }
                                data_list.append(row_dict)

# Convert list of dictionaries to dataframe
df6 = pd.DataFrame(data_list)

# Data transformation on file1
# Drop any duplicates
d1 = df1.drop_duplicates()
d3 = df3.drop_duplicates()
d4 = df4.drop_duplicates()
d5 = df5.drop_duplicates()
d6 = df6.drop_duplicates()


null_counts = d1.isnull().sum()
null_counts = df2.isnull().sum()
null_counts = d3.isnull().sum()
null_counts = d4.isnull().sum()
null_counts = d5.isnull().sum()
null_counts = d1.isnull().sum()


d1.to_csv('agg_trans.csv', index=False)
df2.to_csv('agg_user.csv', index=False)
d3.to_csv('map_tran.csv', index=False)
d4.to_csv('map_user.csv', index=False)
d5.to_csv('top_tran.csv', index=False)
d6.to_csv('top_user.csv', index=False)


