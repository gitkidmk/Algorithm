package Greedy;

import java.util.Arrays;

class Solution {
    int sosu(int number){
        //number는 무조건 0 초과이다
        int count = 0;
        for(int i=1; i*i<=number; i++){
            if(i*i==number) count += 1;
            else if(number%i == 0) count += 2;
        }
        return count;
    }
    
    public int solution(int number, int limit, int power) {
        int answer = 0;
        int[] arr = new int[number];
        // 1~number를 돌면서 각 소수 개수 arr를 생성한다
        for(int i=1; i<=number; i++){
            arr[i-1] = sosu(i);
        }
        
        //arr를 돌면서 limit 초과이면 power로 교체한다
        for(int i=0; i<number; i++){
            if (arr[i]>limit) arr[i] = power;
        }
        
        // arr sum을 answer에 담는다
        answer = Arrays.stream(arr).sum();
        return answer;
    }

    public static void main(String[] args){
        int answer = new Solution().solution(5, 3, 2);
        System.out.println(answer);
    }
}
