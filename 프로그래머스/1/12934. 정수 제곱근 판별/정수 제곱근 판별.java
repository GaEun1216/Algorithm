class Solution {
    public long solution(long n) {
        long answer;
        long compair = (long)Math.sqrt(n);
        if(compair*compair == n){
            answer = (compair + 1)*(compair + 1);
        }
        else{
            answer = -1;
        }
        return answer;
    }
}