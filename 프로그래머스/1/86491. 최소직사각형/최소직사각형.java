class Solution {
    public int solution(int[][] sizes) {
        int n =0, m=0;
        for(int i=0;i<sizes.length;i++){
            if(sizes[i][1]>sizes[i][0]){
                if(n<sizes[i][0]) n = sizes[i][0];
                if(m<sizes[i][1]) m = sizes[i][1];
            }
            else{
                if(n<sizes[i][1]) n = sizes[i][1];
                if(m<sizes[i][0]) m = sizes[i][0];
            }
        }
        
        return n*m;
    }
}