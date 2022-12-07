import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

class Main{
    void dfs(int node){

    }

    void solution() throws IOException{        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        //2차원 배열의 1차는 Array, 2차는 List
        LinkedList<Integer>[] graph = new LinkedList[n+1];
        boolean[] visited = new boolean[n+1];
        
        // List graph = new LinkedList<Integer>();
        for(int i = 1; i < n+1; i++){
            StringTokenizer st2 = new StringTokenizer(br.readLine()," ");

            int o = Integer.parseInt(st2.nextToken());
            int p = Integer.parseInt(st2.nextToken());
            
            graph[o].add(p);
            graph[p].add(o);
        }

        System.out.println(Arrays.toString(graph) + " & " + Arrays.toString(visited));


        
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write("TEST...!");
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws IOException{
        new Main().solution();
    }
}