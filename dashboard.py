import streamlit as st
import pandas as pd
from datetime import datetime
import statistics_file
import select_data
import main_file_

countries = pd.read_csv('Data/Currencies.csv')
st.set_page_config(page_title=None, page_icon=None, layout="wide")
col1, col2, col3 = st.columns(3)
with col1:
    country = st.selectbox('Country:',countries['Country'].sort_values())
    currency = countries[countries['Country']==country].Currency.iloc[0]
    stats = statistics_file.current_data(currency)
    prev = stats['prev']
    p_sel = str(round(prev['sell'],2))
    p_buy = str(round(prev['buy'],2))
    p_avg = str(round((prev['sell']+prev['buy'])/2,2))
    st.metric("Current Average Rate", str(round((stats['sell']+stats['buy'])/2,2)), p_avg+" Last Month")
with col2:
    start_date = st.date_input("From:",datetime(2017,1,1),max_value=datetime(2024,1,19),min_value=datetime(2017,1,1))
    st.metric("Current Buying Rate", str(round(stats['buy'],2)), p_buy+" Last Month")
with col3:
    end_date = st.date_input("To:",datetime(2024,1,19),max_value=datetime(2024,1,19),min_value=datetime(2017,1,1))
    st.metric("Current Selling Rate", str(round(stats['sell'],2)), p_sel+" Last Month")
dat_col1,dat_col2 = st.columns(2)
with dat_col1:
    st.markdown('**Kenya Shilling Against '+country+' Currency**')
    chart_data = select_data.select_data(main_file_.read_data(),{'currency':currency,'start_date':str(start_date),'end_date':str(end_date)})
    xr_type = st.radio('Exchange Rate type', ['Buy','Sell'], horizontal= True)
    st.line_chart(chart_data, x="Date", y=xr_type)
with dat_col2:
    st.markdown('**Rate of Inflation**')
    st.markdown('From: _'+str(start_date)+'_')
    st.markdown('To: _'+str(end_date)+'_')
    st.line_chart(chart_data, x="Date", y=xr_type)