class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for(int i= left; i <= right;i++){
            int cnt = 0;
            for(int x = 1; x<=i;x++)
                if(i%x == 0){
                    cnt++;
                }
            if(cnt%2==0){
                answer += i;
            }
            else{
                answer -= i;
            }
        }
        return answer;
    }
}