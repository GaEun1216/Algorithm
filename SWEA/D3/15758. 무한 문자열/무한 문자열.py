def gcd(a,b):
    if b > a: a,b = b,a
    while b >0:
        a,b = b,a%b
    return a

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m = input().split()
    ln = len(n)
    lm = len(m)
    num = gcd(ln,lm)
    if n == m:
        print(f'#{test_case} yes')
    else:
        yes = True
        key = n[:num]
        for i in range(0,ln,num):
            if n[i:i+num] != key:
                yes = False
        for i in range(0,lm,num):
            if m[i:i+num] != key:
                yes = False
        if yes:
            print(f'#{test_case} yes')
        else:
            print(f'#{test_case} no')
    
    
