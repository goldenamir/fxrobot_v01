
import streamlit as st
import datetime
import pytz
import pandas as pd 
import MetaTrader5 as mt5 

# Streamlit UI
st.title("Forex Robot Streamlit App")

# Define timeFrames
time_frame = {
    'frame_M15': mt5.TIMEFRAME_M15,
    'frameframe_M30': mt5.TIMEFRAME_M30,
    'frame_H1': mt5.TIMEFRAME_H1,
    'frame_H4': mt5.TIMEFRAME_H4,
    'frame_D1': mt5.TIMEFRAME_D1,
    'frame_W1': mt5.TIMEFRAME_W1,
    'frame_M1': mt5.TIMEFRAME_MN1
}

# Define assets
assets = {
    'eurodollar': 'EURUSD',
    'dollarfrank': 'USDCHF',
    'pounddollar': 'GBPUSD',
    'dollarcanda': 'USDCAD',
    'bitcoin': 'BTCUSD',
    'ethrioum': 'ETHUSD',
    'gold': 'XAUUSD', 
    'silver': 'XAGUSD'
}

# ... (rest of the code remains the same) ...

# Function for getting quotes
def get_quotes(time_frame, year, month, day, asset):
    if not mt5.initialize():
        st.error("initialize() failed, error code =", mt5.last_error())
        quit()

    timezone_obj = pytz.timezone('Europe/Paris')
    time_from = datetime.datetime(year, month, day, tzinfo=timezone_obj)
    time_to = datetime.datetime.now(tz=timezone_obj) + datetime.timedelta(days=1)
    rates = mt5.copy_rates_range(asset, time_frame, time_from, time_to)
    rates_frame = pd.DataFrame(rates)
    return rates_frame

now = datetime.datetime.now()

selected_time_frame = st.selectbox("Select Time Frame", list(time_frame.keys()))
selected_asset = st.selectbox("Select Asset", list(assets.keys()))
year = st.slider("Select Year", 2000, now.year, now.year)
month = st.slider("Select Month", 1, 12, now.month)
day = st.slider("Select Day", 1, 31, now.day)

if st.button("Get Quotes"):
    st.write(f"Fetching quotes for {selected_asset} on {selected_time_frame} time frame.")
    quotes_df = get_quotes(time_frame[selected_time_frame], year, month, day, assets[selected_asset])
    st.write("Quotes DataFrame:")
    st.write(quotes_df)
