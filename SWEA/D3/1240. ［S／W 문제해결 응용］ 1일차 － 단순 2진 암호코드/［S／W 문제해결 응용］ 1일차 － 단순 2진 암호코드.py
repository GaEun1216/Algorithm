T = int(input())
key = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5,
       '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
result = []

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    brr = []
    # 1이 포함된 행을 찾아서 brr에 저장
    for i in range(N):
        if 1 in arr[i]:
            brr = arr[i]
            break  # 첫 번째로 1이 포함된 행을 찾으면 더 이상 검색하지 않음

    # 가장 마지막 1을 찾고 그 앞의 56자리 (암호) 추출
    for j in range(M - 1, 0, -1):
        if brr[j] == 1:
            secret = brr[j-55:j+1]
            break

    answer = []
    # 7자리씩 끊어서 키 값을 이용해 숫자 추출
    for i in range(0, 56, 7):
        tmp = ''.join(map(str, secret[i:i+7]))
        answer.append(key[tmp])

    # 검증 코드 계산
    total = 0
    for i in range(8):
        if i % 2 == 0:
            total += 3 * answer[i]
        else:
            total += answer[i]

    # 검증 코드가 유효하면 결과에 합을 추가, 아니면 0을 추가
    if total % 10 == 0:
        result.append(sum(answer))
    else:
        result.append(0)

# 최종 결과 출력
for test_case in range(1, T + 1):
    print(f'#{test_case} {result[test_case - 1]}')
