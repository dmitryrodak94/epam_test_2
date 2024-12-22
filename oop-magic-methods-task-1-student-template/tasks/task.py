from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values

    def __add__(self, other):
        if isinstance(other, str):
            return [f'{num} {other}' for num in self.values]


print(Counter([1, 2, 3]) + "Mississippi")

# ["1 Mississippi", "2 Mississippi" , "3 Mississippi"]