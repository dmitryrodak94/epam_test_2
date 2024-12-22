from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    d = {}
    for i in s:
        d[i.lower()] = d.get(i, 0) + 1
    d = dict(sorted(d.items()))
    return d

print(get_dict('Oh, it is python'))