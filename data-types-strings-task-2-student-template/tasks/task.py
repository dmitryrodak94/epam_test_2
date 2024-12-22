def get_longest_word( s: str) -> str:
    """
     Add your code here 
    """
    d ={i: len(i) for i in s.split()}

    
    s = max(d, key=lambda x: len(x) ) 
        


    return s

