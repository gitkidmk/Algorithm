package Sort;

import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

// 귤 고르기
class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        int count = 0;

        // tangerine을 HashMap에 담는다
        Map<Integer, Integer> map = new HashMap<Integer, Integer> ();

        for(int t : tangerine){
            int new_val = 1;
            if(map.containsKey(t)){
                new_val = map.get(t) + 1;
            }
            map.put(t, new_val);
        }
        
        // 해당 tHashMap을 value 오름차순으로 sort 한다
        List<Map.Entry<Integer, Integer>> entryLsit = map.entrySet()
                                                        .stream()
                                                        .sorted(Collections.reverseOrder(Map.Entry.comparingByValue()))
                                                        .collect(Collectors.toList());
     
        // for loop
        for (Map.Entry<Integer, Integer> e : entryLsit){
            if(count < k){
                count += e.getValue();
                answer += 1;
            }
            else break;
        }

        return answer;
    }

    public static void main(String[] args){
        int answer = new Solution().solution(4, new int[]{1, 3, 2, 5, 4, 5, 2, 3});
        System.out.println(answer);
    }
}