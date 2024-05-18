
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    game = [ list(input()) for _ in range(N)]
    game2 = list(zip(*game))
    answer = "NO"
    # 가로 / 세로
    for x in range(N):
        for y in range(N-4):
            if '.' not in game[x][y:y+5] \
                    or '.' not in game2[x][y:y+5]:
                answer = "YES"
                break
        if answer == "YES": break

    # 대각선
    for x in range(N-4):
        for y in range(N-4):
            cnt = cnt2 = 0
            for i in range(5):
                if game[x+i][y+i] == 'o':
                    cnt += 1
                if game[x+4-i][y+i] == 'o':
                    cnt2 += 1
            if cnt == 5 or cnt2 == 5:
                answer = "YES"
                break
        if answer == "YES": break



    print(f'#{test_case} {answer}')