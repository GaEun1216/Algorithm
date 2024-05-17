
move = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

def dfs(num, count):
    global result

    for a in node[num]:
        if visited[a] == -1:
            visited[num] = 0
            dfs(a,count+1)
            visited[num] = -1

    result = max(result,count)

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    visited = [-1]*(N+1)
    node = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        node[a].append(b)
        node[b].append(a)

    count , result = 1, 0
    for i in range(1,N+1):
        dfs(i,count)

    print(f"#{test_case} {result}")


