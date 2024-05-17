
move = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

T = int(input())
for test_case in range(1, T + 1):
    N,M,K = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    result = "Possible"
    for i in range(N):
        goods = (arr[i]//M)*K
        if goods < i + 1:
            result = "Impossible"
            break


    print(f"#{test_case} {result}")


