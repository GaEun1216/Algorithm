
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    length = int(input())
    building = list(map(int,input().split()))
    cnt = 0
    for i in range(2,length-2):
        a = []
        for j in range(i-2,i+3):
            if i != j:
                a.append(building[j])
        key = max(a)
        cnt += max(building[i] - key,0)
    print(f"#{test_case} {cnt}")
