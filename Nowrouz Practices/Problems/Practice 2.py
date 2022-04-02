def short(num):
    i = 0
    j = 0
    max = -1
    remaining_list = []
    while num > 0:
        r = num % 10
        num //= 10
        remaining_list.append(str(r))
        i += 1
    remaining_list = remaining_list[::-1]
    while j < len(remaining_list) - 1:
        result_list = remaining_list.copy()
        result_list[j] = str(int(result_list[j]) + int(result_list[j + 1]))
        result_list.pop(j + 1)
        ans = "".join(result_list)
        j += 1
        if int(ans) >= int(max):
            max = ans
    return max
print(short(int(input())))