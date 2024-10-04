# Proyek-Analisis-Data--Bike-Sharing-Data-Set

# Bike Sharing Data Dashboard

This dashboard provides a visual analysis of bike sharing data based on weather, time, and other factors. The dataset includes daily and hourly information on bike rentals, and this dashboard helps to explore various trends and insights.

## Project Structure


├── dashboard.py         # Main Streamlit dashboard code
├── day.csv              # Daily bike sharing data
├── hour.csv             # Hourly bike sharing data
├── requirements.txt     # Required libraries for the project
└── README.md            # Instructions on how to run the project


How to Run the Dashboard
1. Clone the Repository
### First, clone the repository to your local machine using the command:

git clone <repository-url>

2. Navigate to the Directory
### Change your current working directory to the project folder:
cd <directory-name>

3. Install Required Libraries
### Install all necessary dependencies listed in the requirements.txt file. You can do this using pip:
pip install -r requirements.txt

The following libraries will be installed:

- streamlit: Used to create the web-based interactive dashboard.
- pandas: For data manipulation and analysis.
- matplotlib and seaborn: For creating visualizations.
- numpy: For numerical computations.

4. Run the Streamlit Dashboard
### Once the libraries are installed, you can run the Streamlit app by executing the following command in your terminal:

streamlit run dashboard.py

### Streamlit will launch the dashboard in your default browser, and you will see the interface to explore the bike sharing data.

## Exploring the Dashboard
The dashboard consists of the following sections:

### Home
- This section gives an overview of the dataset and explains the purpose of the dashboard.

### Exploratory Data Analysis (EDA)
- Displays basic information about the dataset, including a sample of the data, statistical summaries, and checks for missing values.

### Visualization
- Bike Rentals by Temperature Range in 2011: A bar chart showing the distribution of bike rentals based on temperature categories in the year 2011.
- Rental Trends Throughout the Year and Between Years: A line chart that visualizes the total bike rentals per month and compares trends across different years.
