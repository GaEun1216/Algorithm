class Solution {
    public int solution(long num) {
        int i;
        for(i=0;i<500;i++){
            if(num == 1) break;
            if(num%2 == 0){
                num = num / 2;
            }
            else{
                num = num*3 + 1;
            }
        }
        if(i==500){
            i = -1;
        }
        return i;
    }
}