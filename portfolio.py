import datetime as dt
from dataclasses import dataclass

from stock import Stock
from optimization_strategy import OptimizationStrategy


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


class CreatePortfolio:
    @staticmethod
    def optimized_portfolio(tickers: list[str], start_date: str, end_date: str, optimization_strategy: OptimizationStrategy) -> Portfolio:

        portfolio = CreatePortfolio.equally_weighted_portfolio(
            tickers=tickers, start_date=start_date, end_date=end_date)
        return optimization_strategy.optimize(portfolio)

    @staticmethod
    def equally_weighted_portfolio(tickers: list[str], start_date: dt.datetime, end_date: dt.datetime):
        stock_list = [
            Stock(ticker, start_date, end_date) for ticker in tickers]
        weight = 1/len(stock_list)
        return Portfolio([StockInPortfolio(stock=stock, weight=weight) for stock in stock_list])


