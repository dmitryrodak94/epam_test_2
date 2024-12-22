from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    l = []
    l.extend(str(num))
    l = [int(i) for i in l]
    return tuple(l)

print(get_tuple(87178291199))
