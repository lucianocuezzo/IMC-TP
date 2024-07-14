from stock import Stock
from portfolio import CreatePortfolio
from optimization_strategy import OptimizationStrategy, MinimizeSTD

minimize_std = MinimizeSTD(0.12)
portfolio = CreatePortfolio.optimized_portfolio(
    ["NVDA", "AAPL", "MSFT", "YPF"], start_date="2020-01-01", end_date="2022-01-01", optimization_strategy=minimize_std)
