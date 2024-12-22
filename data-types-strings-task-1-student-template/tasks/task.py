def get_fractions(a_b: str, c_b: str) -> str:
    """
    Add your code here  
    """
    def del_denominator(a: str) -> list:
        a = list(map(lambda x: int(x), a.split('/')))
        return a 

    result =  f'{a_b} + {c_b} = {str(del_denominator(a_b)[0] + del_denominator(c_b)[0])}/\
{str(del_denominator(a_b)[1])}'


    return result

print(get_fractions('1/3', '5/3'))
