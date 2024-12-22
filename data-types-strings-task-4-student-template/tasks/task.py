def check_str(s: str) -> bool:
    """
    Add your code here
    """

    l = [' ', '?', '!', ',', '-', "'", '"']

    filtered_s = ''.join(i for i in s.lower() if i not in l)

    return filtered_s == filtered_s[::-1]

print(check_str("A dog! A panic in a pagoda!"))

