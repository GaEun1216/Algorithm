class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int i = 1;
        int j = 0;
        while(i<=n && j < section.length){
            if(i == section[j]){// 값이 일치하면
                answer++;
                i+=m;
                j++;
            }
            else if(i < section[j]){
                i++;
            }
            else{
                j++;
            }
            
        }
        return answer;
    }
}