many = int(input())
for _ in range(many):
    n, k = list(input().split())
    n = int(n)
    k = int(k)
    a = list(input().split())
    b = list(input().split())
    j = 0
    while len(a) > 0:
        if j >= len(a):
            break
        if k >= int(a[j]):
            k += int(b[j])
            a.remove(a[j])
            b.remove(b[j])
            j = 0
        else:
            j += 1
    print(k)