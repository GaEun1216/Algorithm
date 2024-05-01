n,k = map(int,input().split())
bag = [0]+[list(map(int,input().split())) for i in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1): # 물건 개수
    for j in range(1,k+1): # 가치
        if j >= bag[i][0]: # bag[i][0] : 무게 / bag[i][1] : 가치
            dp[i][j] = max(bag[i][1]+dp[i-1][j-bag[i][0]],dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])
        