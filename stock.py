import yfinance as yf
import pandas as pd
from IPython.display import display
from statistics_data import Statistics


class Stock:
    def __init__(self, ticker: str, start: str, end: str, trading_days: float = 252, risk_free: float = 0.04) -> None:
        self.name = ticker

        self.trading_days = trading_days

        self.yearly_rf = risk_free
        self.daily_rf = self.yearly_rf/self.trading_days

        self.data = yf.download(
            tickers=[ticker], start=start, end=end, interval='1d')
        self.daily_returns = self.__get_daily_returns()

        self.daily_statistics = self.__get_statistics(is_daily=True)
        self.yearly_statistics = self.__get_statistics(is_daily=False)

    def __get_statistics(self, is_daily: bool = True) -> Statistics:
        mean = self.daily_returns['Daily Returns'].mean() if is_daily else self.daily_returns['Daily Returns'].mean() * \
            self.trading_days

        var = self.daily_returns['Daily Returns'].var() if is_daily else self.daily_returns['Daily Returns'].var() * \
            self.trading_days**2

        std_dev = self.daily_returns['Daily Returns'].std() if is_daily else self.daily_returns['Daily Returns'].std() * \
            self.trading_days

        cv = std_dev/mean

        sharpe_ratio = (
            mean - (self.daily_rf if is_daily else self.yearly_rf))/std_dev

        return Statistics(mean, var, std_dev, cv, sharpe_ratio)

    def show_data(self):
        display(self.data)

    def show_daily_returns(self):
        display(self.daily_returns)

    def show_main_metrics(self):
        pass

    def __get_daily_returns(self):
        daily_returns_df = self.data
        daily_returns_df['Daily Returns'] = daily_returns_df['Adj Close'].pct_change()
        daily_returns_df.dropna(subset=['Daily Returns'], inplace=True)
        daily_returns_df.reset_index(inplace=True)
        return daily_returns_df[['Date', 'Daily Returns']]

    def show_statisticts(self):
        pass
