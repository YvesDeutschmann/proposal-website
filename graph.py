import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

def convert_to_unix(date):
    """Converts a datetime date to a unix integer."""
    return(date - datetime(1970,1,1)).total_seconds()

def convert_to_datetime(timestamp):
    """Converts a unix integer into a pandas datetime object."""
    return datetime.fromtimestamp(timestamp)

def load_data():
    symbol = 'MSFT'
    # get start & endtime for ohlc data
    end = convert_to_unix(datetime(2020, 9, 2))
    start = convert_to_unix(datetime(2019, 11, 20))

    query = 'https://finnhub.io/api/v1/stock/candle?symbol={}&resolution=D&from={}&to={}&token=btbq75v48v6p15lfi6bg'.format(
        symbol, 
        start, 
        end
    )
    r = requests.get(query)
    
    data = pd.DataFrame(r.json())
    data = data.set_index(data.t.apply(lambda x: convert_to_datetime(x)))

    return data

def plot_data(data):

    fig = go.Figure(data=[
    go.Candlestick(
        x=data.index,
        open=data.o,
        high=data.h,
        low=data.l,
        close=data.c)])

    return fig