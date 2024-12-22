from typing import Union
from math import *

NumType = Union[int, float]

def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
  result = None
  # (12 * a + 25 * b) / (1 + a**(2**b))


  return round((12 * a + 25 * b) / (1 + a**(2**b)), 2)

