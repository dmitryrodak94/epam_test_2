from typing import List
import math


def foo(nums: List[int]) -> List[int]:
    l = []

    for i in range(0, len(nums)):
        l.append(int(math.prod(nums[i+1:] + nums[:i])))

    return l

print(foo([1, 2, 3, 4, 5]))