from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    """
    Add your code here or call it from here   
    """
    l = []
    for item in sequence:
            if isinstance(item, (list, tuple)):
                  l.extend(linear_seq(item))

                  
            else:
                  l.append(item)
    return l


sequence = [1,2,3,[4,5, (6,7)]]
print(linear_seq(sequence))