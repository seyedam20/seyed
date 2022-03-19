if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list1 = list(set(arr))
    list1.remove(max(list1))
    print(max(list1))