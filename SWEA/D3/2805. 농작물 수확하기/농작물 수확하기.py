
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        value = list(map(str,input()))
        arr.append(list(map(int,value)))

    key = 0
    result = 0
    middle = N//2
    for i in range(N):
        key = min(i,N-i-1)
        result+= sum(arr[i][middle-key:middle+key+1])


    print(f"#{tc} {result}")
