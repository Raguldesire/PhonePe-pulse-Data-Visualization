# PhonePe-pulse-Data-Visualization

# In this project, we retrieves data from the PhonePe Pulse Github repository, transforms it and stores it in a PostgreSQL database. It then creates an interactive dashboard using Streamlit and Plotly to visualize the data.

![image](https://github.com/Raguldesire/PhonePe-pulse-Data-Visualization/assets/136821041/6cb11a23-4798-4462-91a3-c0bc7193d3c7)

# Process Involved:
1. ***Data extraction:*** Clone the GitHub using scripting to fetch the data from the
Phonepe pulse Github repository and store it in a suitable format such as CSV
or JSON.
2. ***Data transformation:*** Use a scripting language such as Python, along with
libraries such as Pandas, to manipulate and pre-process the data. This may
include cleaning the data, handling missing values, and transforming the data
into a format suitable for analysis and visualization.
3. ***Database insertion:*** Use the "PostgreSQL-connector-python" library in Python to
connect to a PostgreSQL database and insert the transformed data using SQL
commands.
4. **Dashboard creation:** Use the Streamlight and Plotly libraries in Python to create
an interactive and visually appealing dashboard. Plotly's built-in geo map
functions can be used to display the data on a map and Streamlit can be used
to create a user-friendly interface with multiple dropdown options for users to
select different facts and figures to display.
5. ***Data retrieval:*** Use the "PostgreSQL-connector-python" library to connect to the
postgreSQL database and fetch the data into a Pandas data frame. Use the data in
the data frame to update the dashboard dynamically.
6. ***Deployment:*** Ensure the solution is secure, efficient, and user-friendly. Test
the solution thoroughly and deploy the dashboard publicly, making it
accessible to users.
This approach leverages the power of Python and its numerous libraries to extract,
transform, and analyze data, and create a user-friendly dashboard for visualizing
the insights obtained from the data...

# Required libraries to be imported
```python
import pymongo
import psycopg2
import pandas as pd
import os
import streamlit as st
import PIL 
from PIL import Image
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import requests
import geopandas as gpd
import psycopg2.extras as extras
```
