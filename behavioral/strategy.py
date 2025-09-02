from abc import ABC, abstractmethod

class FilterStrategy(ABC):
    @abstractmethod
    def remove_value(self, val):
        pass

class RemoveNegativeStrategy(FilterStrategy):
    def remove_value(self, val):
        return val < 0

class RemoveOddStrategy(FilterStrategy):
    def remove_value(self, val):
        return abs(val) % 2

class Values:
    def __init__(self, values):
        self.values = values

    def filter(self, strategy):
        res = []
        for n in self.values:
            if not strategy.remove_value(n):
                res.append(n)
        return res

values = Values([-7, -4, -1, 0, 2, 6, 9])
print(values.filter(RemoveNegativeStrategy()))
print(values.filter(RemoveOddStrategy()))