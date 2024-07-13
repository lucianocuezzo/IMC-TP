from stock import Stock

s = Stock(ticker='YPF',start="2020-01-02", end="2021-07-05")
s.show_daily_returns()
print(s.daily_median())