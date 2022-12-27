package Implementation;

import java.util.*;

public class happyNumber {
    public boolean isHappy(long n) {
        boolean is_happy = true;
        Set<Long> sq_answer = new HashSet<Long>();

        while (true) {
            // n to string
            // string to char array : chars
            long c_sum = 0;
            char[] chars = Long.toString(n).toCharArray();
            // chars for loop
            for (char c : chars){
                Integer cc = Character.getNumericValue(c);
                c_sum += cc*cc;
            }
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