
T = int(input())
solve = []
for test_case in range(1, T + 1):
    N,K = map(int,input().split())
    V = [0] # 부피
    C = [0] # 가치
    bag = [[0]*(K+1) for _ in range(N+1)]

    for i in range(N):
        v,c = map(int,input().split())
        V.append(v)
        C.append(c)
    for i in range(1,N+1):
        for j in range(1,K+1):
            if V[i] <= j:
                bag[i][j] = max(bag[i-1][j-V[i]]+C[i],bag[i-1][j])
            else:
                bag[i][j] = bag[i-1][j]
    solve.append(bag[N][K])
for test_case in range(1, T + 1):
    print(f'#{test_case} {solve[test_case - 1]}')