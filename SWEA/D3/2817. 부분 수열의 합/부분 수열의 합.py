T = int(input())
def dfs(i, value):
    global result
    if value == K:
        result += 1
        return
    if i >= N or value > K:
        return
    i += 1

    dfs(i,value+arr[i-1])
    dfs(i,value)


for test_case in range(1, T + 1):

    N,K = map(int,input().split())
    arr = list(map(int,input().split()))
    result = 0
    dfs(0, 0)
    print(f"#{test_case} {result}")


