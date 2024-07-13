import yfinance as yf
import pandas as pd
from IPython.display import display

class Stock:
    def __init__(self, ticker: str, start: str, end: str) -> None:
        self.trading_days = 252
        
        self.rf_annualiced = 0.04 # Annualiced
        self.rf

        self.data = yf.download(tickers=[ticker], start=start, end=end, interval='1d')
        self.daily_returns = self.get_daily_returns()
        
        self.daily_mean = self.daily_returns.mean()
        self.yearly_mean = self.daily_mean*self.trading_days

        self.daily_var = self.daily_returns.var()
        self.yearly_var = self.daily_var*self.trading_days**2

        self.daily_std = self.daily_returns.std()
        self.yearly_std = self.daily_std*self.trading_days

        self.daily_cv = self.daily_std/self.daily_mean
        self.yearly_cv = self.yearly_std/self.yearly_mean

    def show_data(self):
        display(self.data)

    def show_daily_returns(self):
        display(self.daily_returns)
    
    def show_main_metrics(self):
      pass
         
    def get_daily_returns(self):
        self.data['Daily Returns'] = self.data['Adj Close'].pct_change()
        return self.data.dropna(subset=['Daily Returns'])['Daily Returns']
    
    def show_statisticts(self):
      pass

    def daily_median(self):
       return self.daily_returns.mean()
       