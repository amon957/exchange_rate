import select_data
import main_file_

def current_data(currency):
    data = main_file_.read_data()
    df = select_data.select_data(data,{'currency':currency,'start_date':'2023-12-19','end_date':'2024-01-19'})
    df_sorted = df.sort_values(by='Date', ascending=False)
    last_1_m = {'sell':df_sorted.iloc[-1].Sell,'buy':df_sorted.iloc[-1].Buy}
    return ({'prev':last_1_m,'sell':df_sorted.iloc[0].Sell,'buy':df_sorted.iloc[0].Buy})
