# Importar módulos necesarios
from stock import Stock
from portfolio import CreatePortfolio
from optimization_strategy import MinimizeSTD, MaximizeSharpeRatio

# Definir las acciones y el rango de fechas
tickers = ["BBAR", "BMA", "CEPU", "CRESY", "EDN", "GGAL", "IRS", "LOMA", "PAM", "SUPV", "TEO", "TGS", "YPF"]
start_date = "2020-01-02"
end_date = "2024-07-05"

# Crear objetos Stock para cada acción
stocks = [Stock(ticker, start_date, end_date) for ticker in tickers]

# Calcular los retornos diarios de cada acción
for stock in stocks:
    print(f"Retornos diarios de {stock.name}:")
    stock.show_daily_returns()

    # Calcular los principales estadísticos (diarios y anualizados)
for stock in stocks:
    print(f"Estadísticos diarios de {stock.name}:")
    print(f"Media={stock.daily_statistics.mean:.4f}, Varianza={stock.daily_statistics.var:.4f}, Desvio Estandar={stock.daily_statistics.std_dev:.4f}, CV={stock.daily_statistics.cv:.4f}, Sharpe Ratio={stock.daily_statistics.sharpe_ratio:.4f}")
    print(f"Estadísticos anualizados de {stock.name}:")
    print(f"Media={stock.yearly_statistics.mean:.4f}, Varianza={stock.yearly_statistics.var:.4f}, Desvio Estandar={stock.yearly_statistics.std_dev:.4f}, CV={stock.yearly_statistics.cv:.4f}, Sharpe Ratio={stock.yearly_statistics.sharpe_ratio:.4f}")
    print()

# Determinar la acción más volátil durante el período
volatilities = [(stock.name, stock.yearly_statistics.std_dev) for stock in stocks]
most_volatile = max(volatilities, key=lambda x: x[1])
print(f"La acción más volátil durante el período es {most_volatile[0]} con una desviación estándar de {most_volatile[1]}.")

# Calcular la matriz de varianzas y covarianzas de los retornos medios para cada acción
portfolio = CreatePortfolio.equally_weighted_portfolio(tickers, start_date, end_date)
cov_matrix = portfolio.get_covariance_matrix()
print("Matriz de varianzas y covarianzas:")
print(cov_matrix)

# Calcular el portafolio que minimiza la volatilidad (desvío estándar) con un rendimiento de 12%
minimize_std = MinimizeSTD(0.12)
optimized_portfolio_min_std = CreatePortfolio.optimized_portfolio(
    tickers=tickers, start_date=start_date, end_date=end_date, optimization_strategy=minimize_std)
print("Portafolio que minimiza la volatilidad con un rendimiento del 12%:")
optimized_portfolio_min_std.show_composition()

# Calcular el portafolio de máximo ratio de Sharpe
maximize_sr = MaximizeSharpeRatio(0.04)
optimized_portfolio_max_sr = CreatePortfolio.optimized_portfolio(
    tickers=tickers, start_date=start_date, end_date=end_date, optimization_strategy=maximize_sr)
print("Portafolio de máximo ratio de Sharpe:")
optimized_portfolio_max_sr.show_composition()