#******************************************************************************************Importing Libraries*************************************************************************************************************************
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
#******************************************************************************************Connecting PostgreSQL*************************************************************************************************************************
ragul =psycopg2.connect(host='localhost',user='postgres',password='****',port=5432,database='phone pe')
cursor=ragul.cursor()
#******************************************************************************************Creating csv files*************************************************************************************************************************

d1=pd.read_csv(r".venv\agg_trans.csv")
d2=pd.read_csv(r".venv\agg_user.csv")
d3=pd.read_csv(r".venv\map_tran.csv")
d4=pd.read_csv(r".venv\map_user.csv")
d5=pd.read_csv(r".venv\top_tran.csv")
d6=pd.read_csv(r".venv\top_user.csv")
#******************************************************************************************Creating table in PostgreSQL with Dataframe*************************************************************************************************************************
def agg_trans():
    df=pd.DataFrame(d1)
    try:
        for _,column in df.iterrows():
                insert_query = '''
                    INSERT INTO agg_trans (states,transaction_year,quarters,transaction_type,transaction_count,transaction_amount)
                    VALUES (%s, %s, %s, %s, %s, %s)

                '''
                values = (
                    column['States'],
                    column['Transaction_Year'],
                    column['Quarters'],
                    column['Transaction_Type'],
                    column['Transaction_Count'],
                    column['Transaction_Amount']
                )
                try:
                    cursor.execute(insert_query,values)
                    ragul.commit()
                except:
                    ragul.rollback()
    except:
        print("values already exists in the agg_trans table")
def agg_user():
    df=pd.DataFrame(d2)
    try:
        for _,column in df.iterrows():
                insert_query = '''
                    INSERT INTO agg_user (success,code,data,responsetimestamp,subfolder,subsubfolder)
                    VALUES (%s, %s, %s, %s, %s, %s)

                '''
                values = (
                    column['success'],
                    column['code'],
                    column['data'],
                    column['responseTimestamp'],
                    column['subfolder'],
                    column['subsubfolder']
                )
                try:
                    cursor.execute(insert_query,values)
                    ragul.commit()
                except:
                    ragul.rollback()
    except:
        print("values already exists in the agg_user table")
def map_trans():
    df=pd.DataFrame(d3)
    try:
        for _,column in df.iterrows():
                insert_query = '''
                    INSERT INTO map_trans (states,transaction_year,quarters,district,transaction_type,transaction_count)
                    VALUES (%s, %s, %s, %s, %s, %s)

                '''
                values = (
                    column['States'],
                    column['Transaction_Year'],
                    column['Quarters'],
                    column['District'],
                    column['Transaction_Type'],
                    column['Transaction_Count']
                )
                try:
                    cursor.execute(insert_query,values)
                    ragul.commit()
                except:
                    ragul.rollback()
    except:
        print("values already exists in the map_trans table")
def map_user():
    df=pd.DataFrame(d4)
    try:
        for _,column in df.iterrows():
                insert_query = '''
                    INSERT INTO map_user(states,transaction_year,quarter,district,registeredusers)
                    VALUES (%s, %s, %s, %s, %s)

                '''
                values = (
                    column['States'],
                    column['Transaction_Year'],
                    column['Quarter'],
                    column['District'],
                    column['RegisteredUsers']
                )
                try:
                    cursor.execute(insert_query,values)
                    ragul.commit()
                except:
                    ragul.rollback()
    except:
        print("values already exists in the map_user table")
def top_trans():
    df=pd.DataFrame(d5)
    try:
        for _,column in df.iterrows():
                insert_query = '''
                    INSERT INTO top_trans (states,transaction_year,quarters,district,transaction_type,transaction_count,transaction_amount)
                    VALUES (%s, %s, %s, %s, %s, %s,%s)

                '''
                values = (
                    column['States'],
                    column['Transaction_Year'],
                    column['Quarters'],
                    column['District'],
                    column['Transaction_Type'],
                    column['Transaction_Count'],
                    column['Transaction_Amount']
                )
                try:
                    cursor.execute(insert_query,values)
                    ragul.commit()
                except:
                    ragul.rollback()
    except:
        print("values already exists in the top_trans table")
def top_user():
    df=pd.DataFrame(d6)
    try:
        for _,column in df.iterrows():
                    insert_query = '''
                        INSERT INTO top_user (state,transaction_year,quarter,district,registereduser)
                        VALUES (%s, %s, %s, %s, %s)

                    '''
                    values = (
                        column['State'],
                        column['Transaction_Year'],
                        column['Quarters'],
                        column['District'],
                        column['RegisteredUsers']
                    )
                    try:
                        cursor.execute(insert_query,values)
                        ragul.commit()
                    except:
                        ragul.rollback()
    except:
         print("values already exists in the top_user table")

#******************************************************************************************Creating streamlit dashboard*************************************************************************************************************************
SELECT = option_menu(
    menu_title = None,
    options = ["About","Home","Basic insights","Contact"],
    icons =["bar-chart","house","toggles","at"],
    default_index=2,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "#080233","size":"cover", "width": "100%"},
        "icon": {"color": "#3120a4", "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#bd0c3f"},
        "nav-link-selected": {"background-color": "#0cb2bd"}})




#******************************************************************************************Basic insights*************************************************************************************************************************
if SELECT == "Basic insights":
    st.title(":violet[BASIC INSIGHTS]")
    st.write("----")
    st.subheader(":green[Let's know some basic insights about the data]")
    options = ["--select--",
               "Top 10 states based on year and amount of transaction",
               "List 10 states based on type and amount of transaction",
               "Top 5 Transaction_Type based on Transaction_Amount",
               "Top 10 Registered-users based on States and District",
               "Top 10 Districts based on states and Count of transaction",
               "List 10 Districts based on states and amount of transaction",
               "List 10 Transaction_Count based on Districts and states",
               "Top 10 RegisteredUsers based on states and District"]
    
               #1
               
    select = st.selectbox("Select the option",options)
    if select=="Top 10 states based on year and amount of transaction":
        cursor.execute("SELECT DISTINCT States, Transaction_Year, SUM(Transaction_Amount) AS Total_Transaction_Amount FROM top_trans GROUP BY States, Transaction_Year ORDER BY Total_Transaction_Amount DESC LIMIT 10");
        
        df = pd.DataFrame(cursor.fetchall(), columns=['States','Transaction_Year', 'Transaction_Amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 states and amount of transaction")
            st.bar_chart(data=df,x="Transaction_Amount",y="States")
            
            #2
            
    elif select=="List 10 states based on type and amount of transaction":
        cursor.execute("SELECT DISTINCT States, SUM(Transaction_Count) as Total FROM top_trans GROUP BY States ORDER BY Total ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['States','Total_Transaction'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("List 10 states based on type and amount of transaction")
            st.bar_chart(data=df,x="Total_Transaction",y="States")
            
            #3
            
    elif select == "Top 5 Transaction_Type based on Transaction_Amount":
        cursor.execute("SELECT DISTINCT Transaction_Type, SUM(Transaction_Amount) AS Amount FROM agg_trans GROUP BY Transaction_Type ORDER BY Amount DESC LIMIT 5")
        df = pd.DataFrame(cursor.fetchall(), columns=['Transaction_Type', 'Transaction_Amount'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 5 Transaction_Type based on Transaction_Amount")
            st.bar_chart(data=df, y="Transaction_Type", x="Transaction_Amount")

            #4
            
    elif select=="Top 10 Registered-users based on States and District":
        cursor.execute("SELECT DISTINCT State, District, SUM(registereduser) AS Users FROM top_user GROUP BY State, District ORDER BY Users DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','RegisteredUsers'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Registered-users based on States and District")
            st.bar_chart(data=df,y="State",x="RegisteredUsers")
            
            #5
            
    elif select=="Top 10 Districts based on states and Count of transaction":
        cursor.execute("SELECT DISTINCT States,District,SUM(Transaction_Count) AS Counts FROM map_trans GROUP BY States,District ORDER BY Counts DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['States','District','Transaction_Count'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Districts based on states and Count of transaction")
            st.bar_chart(data=df,y="States",x="Transaction_Count")
            
            #6
            
    elif select=="List 10 Districts based on states and amount of transaction":
        cursor.execute("SELECT DISTINCT States,Transaction_year,SUM(Transaction_Amount) AS Amount FROM agg_trans GROUP BY States, Transaction_year ORDER BY Amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['States','Transaction_year','Transaction_Amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Least 10 Districts based on states and amount of transaction")
            st.bar_chart(data=df,y="States",x="Transaction_Amount")
            
            #7
            
    elif select=="List 10 Transaction_Count based on Districts and states":
        cursor.execute("SELECT DISTINCT States, District, SUM(Transaction_Count) AS Counts FROM map_trans GROUP BY States,District ORDER BY Counts ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['States','District','Transaction_Count'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("List 10 Transaction_Count based on Districts and states")
            st.bar_chart(data=df,y="States",x="Transaction_Count")
            
            #8
             
    elif select=="Top 10 RegisteredUsers based on states and District":
        cursor.execute("SELECT DISTINCT States,District, SUM(RegisteredUsers) AS Users FROM map_user GROUP BY States,District ORDER BY Users DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns = ['States','District','RegisteredUsers'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 RegisteredUsers based on states and District")
            st.bar_chart(data=df,y="States",x="RegisteredUsers")
#******************************************************************************************Connecting Postgresql*************************************************************************************************************************
# execute a SELECT statement
cursor.execute("SELECT * FROM agg_trans")

# fetch all rows
rows = cursor.fetchall()
from streamlit_extras.add_vertical_space import add_vertical_space
#******************************************************************************************Basic things of phonepe*************************************************************************************************************************
if SELECT == "Home":
    st.image(Image.open(".venv\phonepe.png"),width = 500)
    col1,col2, = st.columns(2)
    with col1:
        st.subheader(":violet[PhonePe]  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    with col2:
        video_file = open('.venv\make_your_1st_bhim_upi_payment_english_comp.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        
    st.subheader(':violet[Registered Users Hotspots - States]')
#******************************************************************************************Importing csv files for plotting*************************************************************************************************************************
    Data_Aggregated_Transaction_df= pd.read_csv(r'F:\asehyeash\.venv\Data_Aggregated_Transaction_Table.csv')
    Data_Aggregated_User_Summary_df= pd.read_csv(r'F:\asehyeash\.venv\Data_Aggregated_User_Summary_Table.csv')
    Data_Aggregated_User_df= pd.read_csv(r'F:\asehyeash\.venv\Data_Aggregated_User_Table.csv')
    Scatter_Geo_Dataset =  pd.read_csv(r'F:\asehyeash\.venv\Data_Map_Districts_Longitude_Latitude.csv')
    Coropleth_Dataset =  pd.read_csv(r'F:\asehyeash\.venv\Data_Map_IndiaStates_TU.csv')
    Data_Map_Transaction_df = pd.read_csv(r'F:\asehyeash\.venv\Data_Map_Transaction_Table.csv')
    Data_Map_User_Table= pd.read_csv(r'F:\asehyeash\.venv\Data_Map_User_Table.csv')
    Indian_States= pd.read_csv(r'F:\asehyeash\.venv\Longitude_Latitude_State_Table.csv')


    c1,c2=st.columns(2)
    with c1:
        Year = st.selectbox(
                ':blue[Please select the Year]',
                ('2018', '2019', '2020','2021','2022'))
    with c2:
        Quarter = st.selectbox(
                ':blue[Please select the Quarter]',
                ('1', '2', '3','4'))
    year=int(Year)
    quarter=int(Quarter)
  #******************************************************************************************Visualization of dataframes*************************************************************************************************************************  
    Transaction_scatter_districts=Data_Map_Transaction_df.loc[(Data_Map_Transaction_df['Year'] == year ) & (Data_Map_Transaction_df['Quarter']==quarter) ].copy()
    Transaction_Coropleth_States=Transaction_scatter_districts[Transaction_scatter_districts["State"] == "india"]
    Transaction_scatter_districts.drop(Transaction_scatter_districts.index[(Transaction_scatter_districts["State"] == "india")],axis=0,inplace=True)
    # Dynamic Scattergeo Data Generation
    
    Transaction_scatter_districts = Transaction_scatter_districts.sort_values(by=['Place_Name'], ascending=False)
    Scatter_Geo_Dataset = Scatter_Geo_Dataset.sort_values(by=['District'], ascending=False) 
    Total_Amount=[]
    for i in Transaction_scatter_districts['Total_Amount']:
        Total_Amount.append(i)
    Scatter_Geo_Dataset['Total_Amount']=Total_Amount
    Total_Transaction=[]
    for i in Transaction_scatter_districts['Total_Transactions_count']:
        Total_Transaction.append(i)
    Scatter_Geo_Dataset['Total_Transactions']=Total_Transaction
    Scatter_Geo_Dataset['Year_Quarter']=str(year)+'-Q'+str(quarter)
    # Dynamic Coropleth
    
    Coropleth_Dataset = Coropleth_Dataset.sort_values(by=['state'], ascending=False)
    Transaction_Coropleth_States = Transaction_Coropleth_States.sort_values(by=['Place_Name'], ascending=False)
    Total_Amount=[]
    for i in Transaction_Coropleth_States['Total_Amount']:
        Total_Amount.append(i)
    Coropleth_Dataset['Total_Amount']=Total_Amount
    Total_Transaction=[]
    for i in Transaction_Coropleth_States['Total_Transactions_count']:
        Total_Transaction.append(i)
    Coropleth_Dataset['Total_Transactions']=Total_Transaction 
    
    
   #******************************************************************************************Connecting states into a scatter************************************************************************************************************************* 
    
    #scatter plotting the states codes 
    Indian_States = Indian_States.sort_values(by=['state'], ascending=False)
    Indian_States['Registered_Users']=Coropleth_Dataset['Registered_Users']
    Indian_States['Total_Amount']=Coropleth_Dataset['Total_Amount']
    Indian_States['Total_Transactions']=Coropleth_Dataset['Total_Transactions']
    Indian_States['Year_Quarter']=str(year)+'-Q'+str(quarter)
    fig=px.scatter_geo(Indian_States,
                        lon=Indian_States['Longitude'],
                        lat=Indian_States['Latitude'],                                
                        text = Indian_States['code'], #It will display district names on map
                        hover_name="state", 
                        hover_data=['Total_Amount',"Total_Transactions","Year_Quarter"],
                        )
    fig.update_traces(marker=dict(color="white" ,size=0.3))
    fig.update_geos(fitbounds="locations", visible=False,)
    # scatter plotting districts
    Scatter_Geo_Dataset['col']=Scatter_Geo_Dataset['Total_Transactions']
    fig1=px.scatter_geo(Scatter_Geo_Dataset,
                        lon=Scatter_Geo_Dataset['Longitude'],
                        lat=Scatter_Geo_Dataset['Latitude'],
                        color=Scatter_Geo_Dataset['col'],
                        size=Scatter_Geo_Dataset['Total_Transactions'],     
                    #text = Scatter_Geo_Dataset['District'], #It will display district names on map
                        hover_name="District", 
                        hover_data=["State", "Total_Amount","Total_Transactions","Year_Quarter"],
                        title='District',
                        size_max=22)
    
    fig1.update_traces(marker=dict(color="rebeccapurple" ,line_width=1))    #rebeccapurple
#coropleth mapping india
    fig_ch = px.choropleth(
                        Coropleth_Dataset,
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',                
                        locations='state',
                        color="Total_Transactions",                                       
                        )
    fig_ch.update_geos(fitbounds="locations", visible=False,)
#combining districts states and coropleth
    fig_ch.add_trace( fig.data[0])
    fig_ch.add_trace(fig1.data[0])
    st.write("### **:violet[PhonePe India Map]**")
    colT1,colT2 = st.columns([6,4])
    with colT1:
        st.plotly_chart(fig_ch, use_container_width=True)
    with colT2:
        st.info(
        """
        Details of Map:
        - The darkness of the state color represents the total transactions
        - The Size of the Circles represents the total transactions dictrict wise
        - The bigger the Circle the higher the transactions
        - Hover data will show the details like Total transactions, Total amount
        """
        )
        st.info(
        """
        Important Observations:
        - User can observe Transactions of PhonePe in both statewide and Districtwide.
        - We can clearly see the states with highest transactions in the given year and quarter
        - We get basic idea about transactions district wide
        """
        )
# -----------------------------------------------FIGURE2 HIDDEN BARGRAPH------------------------------------------------------------------------
    Coropleth_Dataset = Coropleth_Dataset.sort_values(by=['Total_Transactions'])
    fig = px.bar(Coropleth_Dataset, x='state', y='Total_Transactions',title=str(year)+" Quarter-"+str(quarter))
    with st.expander(":red[See Bar graph for the same data]"):
        st.plotly_chart(fig, use_container_width=True)
        st.info('**:blue[The above bar graph showing the increasing order of PhonePe Transactions according to the states of India, Here we can observe the top states with highest Transaction by looking at graph]**')

#******************************************************************************************About PhonePe*************************************************************************************************************************

if SELECT == "About":
    st.image(Image.open(".venv\phonepe.png"),width = 500)
    col1,col2 = st.columns(2)
    with col1:
        st.write("---")
        video_file = open('.venv\pulse-video.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    with col2:
        st.write("---")
        st.subheader("The Indian digital payments story has truly captured the world's imagination."
                 " From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and states-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government."
                 " Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. "
                 "PhonePe Pulse is our way of giving back to the digital payments ecosystem.")
    st.write("---")
    st.title("THE :red[BEAT] OF :violet[PHONEPE]")
    st.write("---")
    st.subheader(":violet[Phonepe became a leading digital payments company]")
    st.subheader(":green[10 key points to know about PhonePe's Indus app store, the rival of Google Play Store.]")
    st.write("1. PhonePe's Challenge: PhonePe is a digital payments company, and it wants to take on Google in the app business. They have created the Indus Appstore to do this.")
    st.write("2. No Fees for Developers: PhonePe is promising Android app developers that they won't have to pay any fees to use their platform. This means they can keep all the money they earn from in-app payments.")
    st.write("3. Made-in-India App Store: The Indus Appstore is proudly made in India. It's their answer to Google Play Store, but it's more focused on Indian users.")
    st.write("4. App Listings Are Free: For the first year, developers can list their apps on the Indus Appstore for free. After that, they will have to pay a small fee.")
    st.write("5. No Extra Charges for In-App Payments: Developers can choose any payment gateway they like for their apps. The Indus App Store won't take any extra money for in-app payments.")
    st.write("6. Localised Experience: The app store will be available in 12 different Indian languages, so users can explore it in the language they prefer.")
    st.write("7. How to Get Started: Developers can register and upload their apps on the Indus Appstore through their website, www.indusappstore.com.")
    st.write("8. Launch Pad for New Developers: New developers will have a special place called Launch Pad where their apps can get more visibility and better search results.")
    st.write("9. Big Market Opportunity: India is expected to have over 1 billion smartphone users by 2026. This means there's a huge opportunity for app developers in India.")
    st.write("10. Support and Tools: Indus App Store offers tools to help developers grow their apps. They have a customer support team in India that's available 24/7. Also, developers can list their apps in Indian languages and make engaging videos to promote them.")
    with open(".venv\PhonePe_Pulse_BCG_report.pdf","rb") as f:
        data = f.read()
    st.download_button(":green[DOWNLOAD REPORT]",data,file_name="PhonePe_pulse_BCG_report.pdf")

#******************************************************************************************About me*************************************************************************************************************************
if SELECT == "Contact":
    name = "Ragul"
    mail = (f'{"Mail :"}  {"ragul1119@gmail.com"}')
    description = "DATA-SCIENTIST..!"
    social_media = {"GITHUB": "https://github.com/Raguldesire","LinkedIn":"https://www.linkedin.com/in/ragul-s-92270b186/"}
    st.title('Phonepe Pulse data visualisation')
    st.write("The goal of this project is to extract data from the Phonepe pulse Github repository, transform and clean the data, insert it into a MySQL database, and create a live geo visualization dashboard using Streamlit and Plotly in Python. The dashboard will display the data in an interactive and visually appealing manner, with at least 10 different dropdown options for users to select different facts and figures to display. The solution must be secure, efficient, and user-friendly, providing valuable insights and information about the data in the Phonepe pulse Github repository.")
    st.write("---")
    st.subheader(mail)
    st.write("#")
    st.columns(len(social_media))
    st.subheader("Check out the link for :green[github] ,:green[Linkedin] ")
    for index, (platform, link) in enumerate(social_media.items()):
        st.write(f"[{platform}]({link})")
