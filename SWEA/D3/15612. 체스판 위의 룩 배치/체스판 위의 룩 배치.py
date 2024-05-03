T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    chess = []
    arr = [0]*8
    brr = [0]*8
    cnt = 0
    for i in range(8):
        chess.append(list(input()))
        for j in range(8):
            if chess[i][j] == 'O':
                cnt+=1
                arr[i]+=1
                brr[j]+=1
    if arr.count(1) == 8 and brr.count(1)==8 and cnt == 8:
        print(f'#{test_case} yes')
    else: print(f'#{test_case} no')