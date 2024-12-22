from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """

    for filter in filters:
        data = filter(data)
    return selector(data)
    


def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""
    def selector(data: DataType) -> DataType:
        l = []
        for row in data:
            d = {k: v for k, v in row.items() if k in columns}
            l.append(d)
        return l
    
    return selector


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""
    def filters(data: DataType) -> DataType:
        l = []
        for row in data:
            if row.get(column) in values:
                l.append(row)
            

        return l

    return filters



def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
        
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    return value
    # assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":

    test_query()



    # data = [{'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}]


    # # filters = field_filter(*('sport', *('Basketball', 'volleyball')))
    # # filterrsss = filters(*list(data))
    # # print(filterrsss) 
    

    # selector = select(*('name', 'gender', 'sport'))
    # filtered_data = selector(data)
    # print(filtered_data)


