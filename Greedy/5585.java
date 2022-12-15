package Greedy;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

// 백준은 클래스명이 Main이여야 하네...!
class Main5585{

    int count=0;

    void solution() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String input = br.readLine();
        int pay = Integer.parseInt(input);
        int remained = 1000-pay;
        int[] coins = {500,100,50,10,5,1};

        int answer = calculateCount(coins, remained);

        bw.write(answer+"");
        bw.flush();
        bw.close();
    }

    public int calculateCount(int[] coins, int remained){
        for(int coin: coins){
            count += remained / coin;
            remained = remained % coin;
        }
        return count;
    }

    public static void main(String[] args) throws IOException{
        new Main5585().solution();
    }

}