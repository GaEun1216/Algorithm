T = int(input())

key = {}
key_2 = {}
i = j = N = 1
while True:
    key[N] = (i, j)
    key_2[(i, j)] = N
    i,j = i -1,j+1
    if i < 1:
        i, j = j, 1
    N += 1
    if i == j == 300:
        break


result = []
for test_case in range(1, T + 1):
    p, q = map(int, input().split())
    pi, pj = key[p]
    qi, qj = key[q]
    answer = key_2[(pi + qi, pj + qj)]
    result.append(answer)

for test_case in range(1, T + 1):
    print(f'#{test_case} {result[test_case - 1]}')