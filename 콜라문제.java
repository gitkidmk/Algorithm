class Solution {
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