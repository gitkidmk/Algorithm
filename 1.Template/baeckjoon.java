import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

// 백준은 클래스명이 Main이여야 함, 동일 폴더에서 여러 Java 파일 작업할 경우 동일한 class 명이 불가(class Main : X)하므로, 뒤에 숫자 붙여서 사용하기
// System input, print 대신 효율성을 위해 BufferReader, BufferWriter 사용

class Main_0{
    void solution() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input = br.readLine();
        bw.write(input);
        int answer=0;

        bw.write(answer+"");
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws IOException{
        new Main_0().solution();
    }

}