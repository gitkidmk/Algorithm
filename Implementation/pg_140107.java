package Implementation;

class Solution_140107 {
    // 점 찍기
    // 시간초과

    public long solution(int k, int d) {
        long answer = 0;
        // d*d 숫자 타입 선정을 잘 해야 함.
        // Math.sqrt(), Math.pow() 이런거 잘 알아야 함.
        
        for(int i=0; i<=d; i=i+k){
            for(int j=0; j<=i; j=j+k){
                if((long)(Math.pow(i,2) + Math.pow(j,2)) <= (long)Math.pow(d,2)){
                    if(i == j) answer += 1;
                    else answer += 2;
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        long result = new Solution_140107().solution(2, 4);
        System.out.printf("result: %d%n", result);
    }
}