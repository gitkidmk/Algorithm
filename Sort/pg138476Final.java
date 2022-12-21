package Sort;

import java.util.*;

public class pg138476Final {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        // key: 무게, value: 개수
         Map<Integer, Integer> map = new HashMap<>();

         for(int t : tangerine){
            // Map 메소드
            // 1. getOrDefault(key, default)
            // 2. put
            // Map에 대한 기본 메소드 정리 필요 
            map.put(t, map.getOrDefault(t, 0)+1);
         }
         // map의 key 값만 set 형태로 가져옴
         List<Integer> list = new ArrayList<>(map.keySet());

         // map의 value 값 기준으로 map key로만 구성된 list 내림차순 정렬
         // case1. Comparator에 대해 잘 알아야 함...! lambda 사용 가능
         list.sort((o1,o2) -> map.get(o2)-map.get(o1));

         // case2. Collections를 활용한 sort 방법도 있다. 이 또한 Comparator 활용
        //  Collections.sort(list, (o1,o2)-> map.get(o2)-map.get(o1));

         for(int l : list){
            k -= map.get(l);
            answer ++;
            if (k < 0) break;
         }

        return answer;
    }
    public static void main(String[] args){
        int answer = new pg138476Final().solution(4, new int[]{1, 3, 2, 5, 4, 5, 2, 3});
        System.out.println(answer);
    }    
}
