class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();
        int result = s.solution(2,1,20);

        System.out.printf("result: %d%n", result);
    }

    public int solution(int a, int b, int n) {
        int answer = 0;
        int left = n;
        while (n >= a) {
            left = (n / a) * b;
            answer += left;
            n = left+(n%a);
        }
        return answer;
    }

}

