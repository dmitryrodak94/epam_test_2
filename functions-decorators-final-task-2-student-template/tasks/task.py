from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    """
    Add your code here or call it from here   
    """
    valid_indexes = sorted([index for index in indexes if 0 <= index < len(s)])
    
    result = []
    start = 0
    
    for index in valid_indexes:
        result.append(s[start:index])
        start = index
    
    result.append(s[start:])
    
    return result

