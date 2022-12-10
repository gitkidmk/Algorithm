import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Stack;
import java.util.StringTokenizer;

class Main{

    LinkedList<Integer>[] graph;
    static boolean[] visited;

    void dfs(int node){
        //주어진 node를 stack에 담기
        Stack<Integer> stack = new Stack<>();
        stack.push(node);

        while (!stack.empty()){
            int n = stack.pop();
            if(visited[n] == false){
                visited[n] = true;
                for(int el : graph[n]){
                    stack.push(el);
                }
            }
        }
        
    }

    void solution() throws IOException{        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int answer = 0;
        visited = new boolean[n+1];

        //Array of LinkedList인 2차원 배열 생성 : warning 분석
        graph = new LinkedList[n+1];

        // Array of LinkedList 초기화
        for(int i=1; i<n+1; i++){
            graph[i] = new LinkedList<Integer>();
        }
        
        // graph에 연관관계 채워넣기
        for(int i = 1; i < m+1; i++){
            StringTokenizer st2 = new StringTokenizer(br.readLine()," ");

            int o = Integer.parseInt(st2.nextToken());
            int p = Integer.parseInt(st2.nextToken());
            
            graph[o].add(p);
            graph[p].add(o);
        }

        for(int i = 1; i < n+1; i++){
            if(visited[i]==false){
                dfs(i);
                answer ++;
            }
        }
        
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(Integer.toString(answer));
        bw.flush();
        bw.close();
    }
    public static void main(String[] args) throws IOException{
        new Main().solution();
    }
}