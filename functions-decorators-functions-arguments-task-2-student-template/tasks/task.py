def union(*args) -> set:
    # raise NotImplementedError("Implement me!")
    s = set()
    for row in args:
        row = set(row)
        s.update(row)
    
    return s


def intersect(*args) -> set:
    # raise NotImplementedError("Implement me!")
    s = set()

    result = set(args[0])

    for row in args:
        result.intersection_update(row)
    
    return result




print(union(('S', 'A', 'M'), ['S', 'P', 'A', 'C']))
print(intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C')))