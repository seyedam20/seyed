if __name__ == '__main__':
    a = []
    b = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append(name)
        b.append(score)
    n = b.count(min(b))
    i = 1
    while i <= n:
        c = b.index(min(b))
        b.remove(min(b))
        a.remove(a[c])
        i += 1
    d = b.count(min(b))
    e = 1
    g = []
    while e <= d:
        f = b.index(min(b))
        g.append(a[f])
        b.remove(min(b))
        a.remove(a[f])
        e += 1
    g.sort()
    for t in g:
        print(t)