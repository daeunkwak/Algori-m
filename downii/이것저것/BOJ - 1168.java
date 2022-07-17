/**
 author : https://github.com/daeunkwak
 title : 요세푸스 문제 2
 description :
 date : 2022-07-11
 */


import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_1168 {
    public static void main(String[] args) throws IOException {
        BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        List<Integer> list = new ArrayList<>();

        for (int i = 1; i <= N; i++) {
            list.add(i);
        }

        StringBuilder sb = new StringBuilder();
        sb.append("<");
        int deadIdx = 0;
        while (list.size() > 0) {
            deadIdx = (deadIdx + K - 1) % list.size();
            sb.append(list.remove(deadIdx)).append(", ");
        }
        sb.delete(sb.length() - 2, sb.length()).append(">");
        System.out.println(sb);
//        int idx = K - 1;
//
//        for(int i = 0; i < N-1; i++){
//            if (idx >= list.size()){
//                idx %= list.size();
//            }
//
//            sb.append(list.remove(idx) + ", ");
//            idx += K-1;
//        }
//        sb.append(list.remove(0));
//
//        System.out.println("<" + sb + ">");
//        bw.flush();
//        bw.close();
//        br.close();
    }
}
