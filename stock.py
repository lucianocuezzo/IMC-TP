import yfinance as yf
import pandas as pd
from IPython.display import display

class Stock:
    def __init__(self, ticker: str) -> None:
        self.historical_data = yf.download(tickers=[ticker], period='max', interval='1d')
        self.daily_historical_returns = self.get_daily_returns(self.historical_data)
        self.yearly_historical_returns = self.get_yearly_returns(self.historical_data)

    def show_data(self):
        display(self.historical_data)
    
    def show_main_metrics():

        return
         
    def get_daily_returns(historical_data: pd.DataFrame):
        historical_data['Daily Returns']= historical_data['Adj Close'].pct_change()
        return historical_data.dropna(subset=['Daily Returns'])
    
    def get_yearly_returns(self):
        return

    def show_statisticts(self):


if __name__== "__main__":
    apple_stock = Stock("AAPL")
    apple_stock.show_data()
