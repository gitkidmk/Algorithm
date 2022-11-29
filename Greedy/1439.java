// package는 제외하기
package Greedy;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

class Main{
    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        char[] s = input.toCharArray();
        int flag = 0;
        if(s[0] == '0'){
            flag = 1;
        }

        int[] arr = {0,0};

        for (char ss: s){
            if (ss=='0' && flag == 1){
                arr[0]+=1;
                flag = 0;
            }
            if (ss=='1' && flag == 0){
                arr[1]+=1;
                flag = 1;
            }
        }

        Arrays.sort(arr);
        
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(arr[0]+"");
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws Exception{
        new Main().solution();
    }
}