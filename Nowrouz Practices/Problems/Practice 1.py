n = int(input())
my_list = list(map(int, input().split()))
my_list.append(-1)
ans = 0
for i in range(1, len(my_list) - 2):
    if my_list[i] > my_list[i - 1] and my_list[i] > my_list[i + 1]:
        ans += 1
        if my_list[i + 2] == max(my_list[i], max(my_list[i + 1], my_list[i + 2])):
            my_list[i + 1] = my_list[i + 2]
        elif my_list[i] > my_list[i + 1]:
            my_list[i + 1] = my_list[i]
        else:
            my_list[i] = my_list[i + 1]
my_list.pop(len(my_list) - 1)
print(ans)
print(my_list)