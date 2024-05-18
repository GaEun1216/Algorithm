T = int(input())

key = {}
key_2 = {}
i = j = 1
for N in range(1, 50000):
    key[N] = (i, j)
    key_2[(i, j)] = N
    i,j = i -1,j+1
    if i < 1:
        i, j = j, 1


result = []
for test_case in range(1, T + 1):
    p, q = map(int, input().split())
    pi, pj = key[p]
    qi, qj = key[q]
    answer = key_2[(pi + qi, pj + qj)]
    result.append(answer)

for test_case in range(1, T + 1):
    print(f'#{test_case} {result[test_case - 1]}')