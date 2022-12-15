package Greedy;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

class Main1715 {

    int countDiff(int[] bundles){
        int card_sum = bundles[0];
        int answer = 0;

        if(bundles.length > 1){
            for(int i=1; i<bundles.length; i++){
                card_sum = card_sum + bundles[i];
                answer += card_sum;
                System.out.println("cardSum: "+card_sum);
                System.out.println("answer: "+answer);
            }
        }

        return answer;
    }

    void solution() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n;
        int[] bundles;

        // n, bundles 받기
        n = Integer.parseInt(br.readLine());
        bundles = new int[n];

        for(int i=0; i<n; i++){
            bundles[i] = Integer.parseInt(br.readLine());
        }

        // bundles sort하기
        Arrays.sort(bundles);        

        // countDiff() 돌리기
        int answer = countDiff(bundles);

        bw.write(answer+"");
        bw.flush();
        bw.close();

    }
    
    public static void main(String[] args) throws IOException{
        new Main1715().solution();
    }
}
