class Solution
{
    public int solution(int n, int a, int b)
    {
        int answer = 0;
        while(n > 0){       
            a = (int)(a/2)+ a%2;
            b = (int)(b/2)+ b%2;
            answer++;
            if(a==b) break;
            
            n = n/2;
        }


        return answer;
    }
}