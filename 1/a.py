import yfinance as yf
import streamlit as st

st.write("""
# Basic Stock Price App (by saurabh kumar)
Shown are the stock closing price and volume and dividends of INFOSYS!
""")

st.sidebar.text("ARTI")
from PIL import Image
st.sidebar.image(Image.open("infy.JPG"),caption="infosys logo")


# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'INFY'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1mo', start='2000-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
st.line_chart(tickerDf.Dividends)
st.line_chart(tickerDf.Open)
st.line_chart(tickerDf.High)
st.line_chart(tickerDf.Low)