from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    
    l = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            l.append('FizzBuzz')
        elif i % 5 == 0:
            l.append('Buzz')   
        elif i % 3 == 0: 
            l.append('Fizz')
        else:
            l.append(i)

    return l


print(get_fizzbuzz_list(5))


