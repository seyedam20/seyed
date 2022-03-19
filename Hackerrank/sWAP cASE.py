def swap_case(s):
    s.split()
    empty = []
    for i in s:
        if i.isupper():
            i = i.lower()
            empty.append(i)
        else:
            i = i.upper()
            empty.append(i)
    last = "".join(empty)
    return last
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)