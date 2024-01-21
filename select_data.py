from datetime import datetime

def select_data(data,query={'currency':'US DOLLAR','start_date':'2017-01-01','end_date':'2024-01-19'}):
    '''
    This function filters data based on currency and a range of date
    data: pandas dataframe
    query (Dictionary):
        currency: country name (default: US Dollar)
        start_date: from which date (default: 01/01/2017)
        end_date: to which date (default: 19/01/2024)
    Example:
        {currency: 'United States',start_date: '01/01/2017', end_date: '01/01/2024'}
    '''
    filtered_data = data[(data['Date'] >= query['start_date']) &
                         (data['Date'] <= query['end_date']) &
                         (data['Currency'] == query['currency'])]
    return filtered_data