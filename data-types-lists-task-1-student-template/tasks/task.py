from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    
    str_list_filtred = list(str_list)
    str_list_filtred.sort()
    l = []
    for i in str_list_filtred:
        if i not in l:
            l.append(i)
      



    return l

print(sort_unique_elements(('red', 'white', 'black', 'red', 'green', 'black')))