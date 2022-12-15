package Greedy;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

class AtoB {
    public static void main(String[] args) throws IOException{
        // 숫자 받아오기, target num
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().split("\\s");

        int target = Integer.parseInt(input[0]);
        int num = Integer.parseInt(input[1]);
        char[] num_char = input[1].toCharArray();
        int count = 1;

        while(true){
            if (num == target){
                break;
            }
            if (num < target){
                count = -1;
                break;
            }

            if (num%2 == 0){
                num /= 2;
                num_char = Integer.toString(num).toCharArray();
            } else if (num_char[num_char.length-1] == '1'){
                num_char = Arrays.copyOfRange(num_char, 0, num_char.length-1);
                num = Integer.parseInt(String.valueOf(num_char));
            } else{
                count = -1;
                break;
            }
            count++;    
        }

        bw.write(count+"");
        bw.flush();
        bw.close();

    }
    
}
