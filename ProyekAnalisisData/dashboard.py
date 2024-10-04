import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for seaborn
sns.set(style="whitegrid")

# Load Data
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

#Cleaning Data
## Convert 'dteday' to datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])


# Sidebar for Navigation
st.sidebar.title("Bike Sharing Dashboard")
options = st.sidebar.radio("Select a section", ['Home', 'Assesing', 'EDA','Visualization','Conclusion'])

# Home Section
if options == 'Home':
    st.title("Bike Sharing Data Analysis")
    st.write("""
        Welcome to the Bike Sharing Data Dashboard! Here you can explore various trends and insights 
        from the bike sharing dataset, including the impact of weather, temperature, and time of the year on bike rentals. 
        Use the sidebar to navigate between different sections.
    """)
# Assesing Data
if options == 'Assesing':
    st.title("Assesing Data")
    
    st.subheader("Basic Information of Day Data")
    st.write(day_df.head())
    
    st.subheader("Day Data Summary")
    st.write(day_df.describe())
    
    st.subheader("Missing Values in Day Data")
    st.write(day_df.isnull().sum())
    
    st.subheader("Basic Information of Hour Data")
    st.write(hour_df.head())
    
    st.subheader("Hour Data Summary")
    st.write(hour_df.describe())
    
    st.subheader("Missing Values in Hour Data")
    st.write(hour_df.isnull().sum())



    st.write("""
    **Insights:**      
    - Find out the day_df information
    - Knowing that there is no missing value (0) in day.csv
    - Knowing that there is no duplication (0) in day.csv
    - Knowing hour_df information
    - Knowing that there is no missing value (0) in hour.csv
    - Knowing that there is no duplication (0) in hour.csv
    """)
    

# Exploratory Data Analysis (EDA) Section
if options == 'EDA':
    st.title("Exploratory Data Analysis")
    
    st.subheader("Explore data sepeda yang dirental berdasarkan month menggunakan day_df")
    monthly_df = day_df.groupby(["mnth", "yr"])["cnt"].sum().reset_index()
    st.write(monthly_df)

    st.subheader("Merge day_df dan hour_df menjadi all_df")
    all_df = pd.merge(
        left=day_df,
        right=hour_df,
        how="left",
        left_on="instant",
        right_on="instant",
        suffixes=('_day', '_hour')
    )
    st.write(all_df.head())

    st.write("""
    **Insights:**      
    - View trends in total monthly bike rentals by year, and be able to compare how rental trends change throughout the year and between years.
    - More in-depth analysis that links daily data with specific hourly details
        """)

# Visualization Section
if options == 'Visualization':
    st.title("Visualization of Bike Rentals")

    # Visualization 1: Bike Rentals by Temperature Range in 2011
    st.subheader("Bike Rentals by Temperature Range in 2011")
    data_2011 = day_df[day_df["yr"] == 0]  # Filter for 2011 data
    temp_bins = pd.cut(data_2011["temp"], bins=5, labels=["Very Cold", "Cold", "Mild", "Warm", "Hot"])
    data_2011["temp_range"] = temp_bins

    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(x="temp_range", y="cnt", data=data_2011, palette="coolwarm", ax=ax1)
    ax1.set_title("Bike Rentals by Temperature Range in 2011", fontsize=15)
    ax1.set_xlabel("Temperature Range", fontsize=12)
    ax1.set_ylabel("Bike Rentals", fontsize=12)
    st.pyplot(fig1)

    # Visualization 2: Rental Trends Throughout the Year and Between Years
    st.subheader("Rental Trends Throughout the Year and Between Years")
    monthly_df = day_df.groupby(["mnth", "yr"])["cnt"].sum().reset_index()
    month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthly_df["month_name"] = monthly_df["mnth"].apply(lambda x: month_labels[x - 1])

    fig2, ax2 = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=monthly_df, x="month_name", y="cnt", hue="yr", marker="o", palette="viridis", ax=ax2)
    ax2.set_title("Bike Rental Trend by Month and Year", fontsize=16)
    ax2.set_xlabel("Month", fontsize=12)
    ax2.set_ylabel("Total Bike Rentals", fontsize=12)
    ax2.grid(True)
    st.pyplot(fig2)

    st.write("""
    **Insights What temperature ranges corresponded to the highest and lowest bike rentals in 2011?:**
    - Highest rentals occur in moderate to warm temperatures
    - Bike rentals in extreme temperature conditions (either too cold or too hot)
    """)

    st.write("""
    **Insights Visualisasi How rental trends change throughout the year and between years?:**
    - Bike rentals tend to fluctuate according to seasonal changes, with warmer months favoring more outdoor activities. In addition, patterns between years may reflect long-term trends, either an increase or decrease in the popularity of cycling.
    """)

# Conclusion
if options == 'Conclusion':
    st.title("Conclusion")

    st.write("""
    - Temperature has a major influence on users' decision to rent a bicycle. A comfortable temperature range is the main factor that favors rental demand, while extreme temperatures tend to decrease user interest.
    - There is a clear seasonal pattern, where bicycle rentals increase during the spring and summer months (May to September) and decrease during the winter (December to February). This reflects the impact of weather and outdoor activities on bicycle demand.
    """)
           
    

