def tabdil(list1, list2):
    list1.append(0)
    list2.append(0)
    copy= []
    fake = []
    final = []
    i = 0
    j = 0
    k = 0
    while True:
        while i < len(list1) - 1:
            if list1[i] < list1[i + 1]:
                copy.append(list1[i])
                i += 1
            else:
                copy.append(list1[i])
                i += 1
                break
        while j < len(list2) - 1:
            if list2[j] < list2[j + 1]:
                fake.append(list2[j])
                j += 1
            else:
                fake.append(list2[j])
                j += 1
                break
        if len(copy) < len(fake):
            min = copy
            max = fake
        else:
            min = fake
            max = copy
        while k < len(min):
            if min[k] in max:
                final.append(min[k])
            k += 1
        copy = []
        fake = []
        k = 0
        if i >= len(list1) - 1 and j >= len(list2) - 1:
            return final
print(tabdil(eval(input()), eval(input())))