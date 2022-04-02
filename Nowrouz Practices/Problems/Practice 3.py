inp = eval(input())
my_string = []
for i in inp:
    my_string.append(i)
even_index = [x for x in range(len(my_string)) if x % 2 == 0]
odd_index = [x for x in range(len(my_string)) if x % 2 == 1]
ans1 = my_string.copy()
ans2 = False
my_string2= True
if my_string[0] == '0':
    for i in even_index:
        ans1[i] = '0'
    for j in odd_index:
        ans1[j] = '1'
if my_string[0] == '1':
    for i in even_index:
        ans1[i] = '1'
    for j in odd_index:
        ans1[j] = '0'
if my_string[0] == '?':
    ans2 = my_string.copy()
    for i in even_index:
        ans1[i] = '0'
        ans2[i] = '1'
    for j in odd_index:
        ans1[j] = '1'
        ans2[j] = '0'
j = 0
if my_string[0] == '0':
    for i in my_string:
        if i == '?':
            if my_string.index(i) % 2 == 0:
                my_string[j] = '0'
            else:
                my_string[j] = '1'
        j += 1
j = 0
if my_string[0] == '1':
    for i in my_string:
        if i == '?':
            if my_string.index(i) % 2 == 0:
                my_string[j] = '1'
            else:
                my_string[j] = '0'
        j += 1
if my_string[0] == '?':
    my_string2 = my_string.copy()
    for i in my_string:
        if i == '?':
            if my_string.index(i) % 2 == 0:
                my_string[j] = '1'
                my_string2[j] = '0'
            else:
                my_string[j] = '0'
                my_string2[j] = '1'
        j += 1
if my_string == ans1 or ans2:
    print(True)
elif my_string2 == ans1 or ans2:
    print(True)
else:
    print(False)