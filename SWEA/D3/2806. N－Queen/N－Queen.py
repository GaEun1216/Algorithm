# 백트래킹 문제!!
# 가지치기 해야하므로 깊이우선으로 간다
def promising(row):
    for i in range(row):
        if column[row] == column[i] or row - i == abs(column[row]-column[i]):
            return False
    return True

def dfs(row): #
    global result
    if row == N: #끝까지 계산한 경우
        result += 1
    else:
        for col in range(N):
            column[row] = col
            if promising(row):
                dfs(row+1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    column = [-1]*N
    result = 0

    dfs(0)
    print(f"#{tc} {result}")
