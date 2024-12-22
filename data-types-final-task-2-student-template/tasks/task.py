from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    """
    Add your code here or call it from here   
    """
    matrix, l = [], []
    for r in range(row_start, row_end + 1):
        for c in range(column_start, column_end + 1):
            l.append(r *c)
        matrix.append(l)
        l = []
    return matrix


row_start = 2
row_end = 4
column_start = 3
column_end = 7



print(check(row_start, row_end, column_start, column_end))