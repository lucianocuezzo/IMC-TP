
from scipy.optimize import minimize
import pandas as pd
import numpy as np

from portfolio import Portfolio, StockInPortfolio


class OptimizationStrategy():

    def generate_new_portfolio(self, old_portfolio: Portfolio, optimized_weights: list[float]):
        stocks = [
            stock_in_portfolio.stock for stock_in_portfolio in old_portfolio.stocks]

        stocks_in_portfolio = [StockInPortfolio(
            stock=stock, weight=weight) for stock, weight in zip(stocks, optimized_weights)]

        return Portfolio(stocks_in_portfolio)

    def optimize(self, portfolio: Portfolio) -> Portfolio:
        return portfolio


class MinimizeSTD(OptimizationStrategy):
    def __init__(self, target_return: float) -> None:
        self.target_return = target_return

    def variance(self, weights: list[float], covariance_matrix: pd.DataFrame):
        return np.dot(weights.T, np.dot(covariance_matrix, weights))

    def __get_constraints(self, mean_returns: np.array):
        return [
            {'type': 'eq', 'fun': lambda weights: np.sum(
                weights) - 1},
            {'type': 'ineq', 'fun': lambda weights: -np.dot(
                weights, mean_returns) + self.target_return}
        ]

    def optimize(self, portfolio: Portfolio) -> Portfolio:

        cov_matrix = portfolio.get_covariance_matrix()
        initial_weights = np.array(
            [stock_in_portfolio.weight for stock_in_portfolio in portfolio.stocks])
        mean_returns = portfolio.get_stocks_in_portofolio_mean_returns()
        constraints = self.__get_constraints(mean_returns)
        bounds = [(0, 1) for _ in range(len(initial_weights))]

        result = minimize(fun=self.variance, x0=initial_weights, args=(
            cov_matrix,), constraints=constraints, bounds=bounds, options={'disp': True})

        if result.success:
            print('Optimal Weights:', result.x)
            print('Portfolio Variance:', result.fun)
            print('Portfolio Standard Deviation:', np.sqrt(result.fun))
            print('Expected Portfolio Return:', np.dot(result.x, mean_returns))
            return super().generate_new_portfolio(portfolio, result.x)
        else:
            print('Optimization failed:', result.message)
            return portfolio


class MaximizeSharpeRatio(OptimizationStrategy):
    pass
