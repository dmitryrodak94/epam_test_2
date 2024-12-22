from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    l = []
    for i in range(0, len(lst)-1):
            l.append((lst[i], lst[i+1]))




    return l

print(get_pairs(['need', 'to', 'sleep', 'more']))