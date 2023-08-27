# importing required library
import datetime
import pytz
import pandas as pd 
import MetaTrader5 as mt5 
import numpy as np

# adding timeFrames
time_frame = {
    'frame_M15' : mt5.TIMEFRAME_M15,
    'frameframe_M30' : mt5.TIMEFRAME_M30,
    'frame_H1' : mt5.TIMEFRAME_H1,
    'frame_H4' : mt5.TIMEFRAME_H4,
    'frame_D1' : mt5.TIMEFRAME_D1,
    'frame_W1' : mt5.TIMEFRAME_W1,
    'frame_M1' : mt5.TIMEFRAME_MN1
}

# the values for now
now = datetime.datetime.now()

# list of assets
assets = {
    'eurodollar':'EURUSD',
    'dollarfrank':'USDCHF',
    'pounddollar':'GBPUSD',
    'dollarcanda':'USDCAD',
    'bitcoin':'BTCUSD',
    'ethrioum':'ETHUSD',
    'gold':'XAUUSD', 
    'silver':'XAGUSD', 
    }


# timezone list
timezone = ['America/Newyork', 'Europe/London', 'Europe/Paris', 'Asia/Tokyo', 'Australia/Sydney']

# function for getting qoutes

def get_quotes(time_frame = time_frame['frame_H4'], year = 2023, month = 8, day = 18, asset = assets['gold']):
    if not mt5.initialize():
        print("initialize() failed, error code =", mt5.last_error())

        quit()

    timezone = pytz.timezone('Europe/Paris')
    time_from = datetime.datetime(year, month, day, tzinfo = timezone)
    time_to = datetime.datetime.now(tz = timezone) + datetime.timedelta(days = 1)
    rates = mt5.copy_rates_range(asset, time_frame, time_from, time_to)
    rates_frame = pd.DataFrame(rates)
    return rates_frame


print(get_quotes(time_frame=frame_H4,year=2023, month=8, day=25))
