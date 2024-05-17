
T = 10 #int(input())
for test_case in range(1, T + 1):
    N = int(input()) # 100
    value = [ map(int,input().split()) for _ in range(N)]
    arr = list(zip(*(value)))
    # Red : 1, Blue : 2
    # 빨간색이 나오고 파란색이 나오면 교착
    result = 0
    for i in range(N):
        isRed = False
        for j in range(N):
            if arr[i][j] == 1:
                isRed = True
            # 파란색이면서 앞에 빨간색이 있을 때
            if arr[i][j] == 2 and isRed:
                result += 1
                isRed = False
    print(f"#{test_case} {result}")


