
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,l = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(n)]
	
    def dfs(index, t, k): # t 는 맛 총합, k는 칼로리 총합 
        global maxtaste
        
        if k > l: return
        maxtaste = max(maxtaste,t)
        if index == n: return
        
        newt,newk = data[index]
       
        dfs(index + 1, t+newt,k+newk)
        dfs(index+1,t,k)
    maxtaste = 0
    dfs(0,0,0)
    print(f"#{test_case} {maxtaste}")
        