import java.util.*;

class Solution {
    // 연속 부분 수열 합의 개수
    int[] ele;

    Set<Integer> getSubSum(int k){
        Set<Integer> subSet = new HashSet<>();
        for (int i=0; i<ele.length; i++){
            int s = 0;
            for (int j=0; j<k; j++){
                System.out.println(k+","+i+","+j+","+(i+j)%k+","+ele[(i+j)%k]);
                s += ele[(i+j)%ele.length];
            }
            subSet.add(s);
        }
        return subSet;
    }
    
    public int solution(int[] elements) {
        int answer = 0;
        this.ele = elements;
            
        // Set 인터페이스의 tot_set 생성
        Set<Integer> tot_set = new HashSet<>();

        // for 부분집합 길이 : 2 ~ (elements길이-1) = i (1일때와 elements길이 에서의 tot_set은 명확하다)
            // getSubSum(i) 호출
        for (int i=1; i<=elements.length; i++){
            Set<Integer> ss = getSubSum(i);
            tot_set.addAll(ss);
        }

        // answer에 tot_set 개수 담는다.
        answer = tot_set.size();

        return answer;
    }

    public static void main(String[] args){
        new Solution().solution(new int[]{7,9,1,1,4});
    }
}