def pivot(my_list):
    n = 2
    i = 0
    while n < len(my_list):
        a = my_list[n] - my_list[n - 1]
        b = my_list[n - 1] - my_list[n - 2]
        if a * b < 0:
            i += 1
        n += 1
    return i
print(pivot(eval(input())))