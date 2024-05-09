class Solution {
    public int[] solution(long n) {
        String str = n + "";
        int len = str.length();
        int[] answer = new int[len];
        for(int i=0;i<len;i++){
            answer[i] = Integer.parseInt(str.substring(len-1-i,len-i));
        }
        return answer;
    }
}