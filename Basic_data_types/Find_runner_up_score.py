if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    setarr=list(set(arr))
    reoreder=setarr.sort()
    print(setarr[-2])
