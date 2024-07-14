from dataclasses import dataclass
from stock import Stock
import numpy as np
import pandas as pd


@dataclass
class StockInPortfolio:
    stock: Stock
    weight: float


@dataclass
class Portfolio:
    stocks: list[StockInPortfolio]

    def show_composition(self):
        print("Portfolio composition:")
        for stock_in_portolio in self.stocks_in_portfolio:
            print(f"Stock {stock_in_portolio.stock.name} Weight in portfolio: {
                  stock_in_portolio.weight}")

    def get_stocks_in_portofolio_mean_returns(self):
        mean_returns = [
            stock_in_portfolio.stock.yearly_statistics.mean for stock_in_portfolio in self.stocks]
        return np.array(mean_returns)

    def get_covariance_matrix(self):
        returns_df = pd.DataFrame()
        for stock_in_portfolio in self.stocks:
            if returns_df.empty:
                returns_df = stock_in_portfolio.stock.daily_returns.rename(
                    columns={'Daily Returns': f'{stock_in_portfolio.stock.name} Daily Returns'})
            else:
                returns_df = returns_df.merge(stock_in_portfolio.stock.daily_returns.rename(
                    columns={'Daily Returns': f'{
                        stock_in_portfolio.stock.name} Daily Returns'}),
                    on='Date', how='inner')

        returns_df.drop('Date', axis=1, inplace=True)
        return returns_df.cov()


class CreatePortfolio:
    @staticmethod
    def optimized_portfolio(tickers: list[str], start_date: str, end_date: str, optimization_strategy) -> Portfolio:

        portfolio = CreatePortfolio.equally_weighted_portfolio(
            tickers=tickers, start_date=start_date, end_date=end_date)
        return optimization_strategy.optimize(portfolio)

    @staticmethod
    def equally_weighted_portfolio(tickers: list[str], start_date: str, end_date: str):
        stock_list = [
            Stock(ticker, start_date, end_date) for ticker in tickers]
        weight = 1/len(stock_list)
        return Portfolio([StockInPortfolio(stock=stock, weight=weight) for stock in stock_list])
