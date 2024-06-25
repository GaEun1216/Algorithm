class Solution {
    public int solution(String s) {
        int answer = 1;
        int size = s.length();
        int diffcnt = 0;
        int keycnt = 0;
        char key = s.charAt(0);
        for(int i=0; i<size; i++){
            if(key == s.charAt(i)){
                keycnt++;
            }else{
                diffcnt++;
            }
            if(keycnt == diffcnt && i+1 < size){
                answer++;
                key = s.charAt(i+1);
                diffcnt = keycnt = 0;
            }
        }
        return answer;
    }
}