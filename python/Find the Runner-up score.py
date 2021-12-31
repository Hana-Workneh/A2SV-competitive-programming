if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    x=sorted(list(set(arr)))
    print(x[-2])
