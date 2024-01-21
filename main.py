import pandas as pd

exchange_rates = pd.read_csv('Data/historical_data.csv')
# Add date column to the dataset
exchange_rates['Date'] = pd.to_datetime(exchange_rates[['Year', 'Month', 'Day']])