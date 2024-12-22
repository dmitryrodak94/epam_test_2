from typing import List, Tuple, Union
from functools import reduce


def seq_sum(sequence: Union[List, Tuple]) -> int:
    """
    Add your code here or call it from here   
    """
    n = 0
    total = 0

    for item in sequence:

        if isinstance(item, (list, tuple)):  
            total += seq_sum(item)  
        elif isinstance(item, (int, float)):  
            total += item  
        
    return total


print(seq_sum([1,2,3,[4,5, (6,7)]]))