# 테스트 케이스의 수 입력
T = int(input())

# 테스트 케이스 반복
for t in range(T):
    # 주머니의 개수 N과 나눠 줄 주머니의 개수 K 입력
    N, K = map(int, input().split())
    # 주머니 속 사탕의 개수 입력
    candies = list(map(int, input().split()))

    # 사탕 개수를 내림차순으로 정렬
    candies.sort(reverse=True)
    
    # 최솟값 초기화
    min_diff = float('inf')
    
    # 주머니를 나눠 줄 수 있는 경우
    if N > K:
        # 주머니를 나눠 줄 수 있는 경우의 수 계산
        combinations = N - K + 1
        for i in range(combinations):
            # 최대와 최소 사탕 개수의 차이 계산
            diff = candies[i] - candies[i + K - 1]
            # 최솟값 갱신
            min_diff = min(min_diff, diff)
    else:
        # 주머니를 나눠 줄 수 없는 경우, 모든 사탕을 한 주머니에 넣음
        min_diff = candies[0] - candies[-1]

    # 결과 출력
    print(f'#{t + 1} {min_diff}')