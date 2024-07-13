from portfolio import Portfolio


class OptimizationStrategy:

    def optimize(self, portfolio: Portfolio) -> Portfolio:
        raise NotImplementedError("Implemented by subclasses.")


class MinimizeSTD(OptimizationStrategy):
    pass


class MaximizeSharpeRatio(OptimizationStrategy):
    pass
