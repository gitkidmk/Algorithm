package Implementation;

import java.util.*;

public class happyNumber {
    public boolean isHappy(int n) {
        boolean is_happy = true;
        Set<Integer> sq_answer = new HashSet<Integer>();
        
        // case 0) 365 이라는 숫자에 대해 3, 6, 5 따로 숫자를 갖기 위해 나는 string으로 변환 후 charArray로 전환
        // case 1) 하지만, n이 0보다 클때까지 365를 10으로 나눈 나머지를 저장해나갈 수 있다.
        

        while (true) {
            // n to string
            // string to char array : chars
            int c_sum = 0;
            while(n>0){
                int d = n % 10;
                n = n / 10;
                c_sum += d*d;     
            }
            // TODO: 아래 조건 간추리기
            if (c_sum == 1)
                break;
            if (sq_answer.contains(c_sum)) {
                is_happy = false;
                break;
            } else { 
                sq_answer.add(c_sum);
                n = c_sum;
            }
        }

        return is_happy;
    }

    public static void main(String[] args){
        boolean answer = new happyNumber().isHappy(2);
        System.out.println(answer);
    }
    
}