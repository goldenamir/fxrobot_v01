# importing required library
import datetime
import pytz
import pandas as pd 
import MetaTrader5 as mt5 
import numpy as np 

# adding timeFrames
frame_M15 = mt5.TIMEFRAME_M15 # 15-minute time 
frameframe_M30 = mt5.TIMEFRAME_M30 # 30-minute time frame 
frame_H1 = mt5.TIMEFRAME_H1 # Hourly time frame 
frame_H4 = mt5.TIMEFRAME_H4 # 4-hour time frame 
frame_D1 = mt5.TIMEFRAME_D1 # Daily time frame 
frame_W1 = mt5.TIMEFRAME_W1 # Weekly time frame 
frame_M1 = mt5.TIMEFRAME_MN1 # Monthly time frame 

# the values for now
now = datetime.datetime.now()

# list of assets
assets = ['EURUSD', 'USDCHF', 'GBPUSD', 'USDCAD', 'BTCUSD','ETHUSD', 'XAUUSD', 'XAGUSD', 'SP500m', 'UK100','XAUUSD']


# timezone list
timezone = ['America/Newyork', 'Europe/London', 'Europe/Paris', 'Asia/Tokyo', 'Australia/Sydney']

# function for getting qoutes

def get_quotes(time_frame, year = 2023, month = 8, day = 18, asset = 'XAUUSD'):
    if not mt5.initialize():
        print("initialize() failed, error code =", mt5.last_error())

        quit()

    timezone = pytz.timezone('Europe/Paris')
    time_from = datetime.datetime(year, month, day, tzinfo = timezone)
    time_to = datetime.datetime.now(tz = timezone) + datetime.timedelta(days = 1)
    rates = mt5.copy_rates_range(asset, time_frame, time_from, time_to)
    rates_frame = pd.DataFrame(rates)
    return rates_frame


