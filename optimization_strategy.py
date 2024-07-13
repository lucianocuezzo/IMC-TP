from portfolio import Portfolio
import pandas as pd



class OptimizationStrategy():

    @staticmethod
    def get_covariance_matrix(portfolio: Portfolio):

    def get_portfolio_return(portfolio: Portfolio):


    @staticmethod
    def optimize(portfolio: Portfolio) -> Portfolio:
        raise NotImplementedError("Implemented by subclasses.")


class MinimizeSTD(OptimizationStrategy):
    pass


class MaximizeSharpeRatio(OptimizationStrategy):
    pass
