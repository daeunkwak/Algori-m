/*
 author : https://github.com/daeunkwak/Problem-Solving
 title : 제곱수의 합
 description : 다이나믹 프로그래밍
 date : 2022-08-13
 */

package DP;
import java.io.*;

public class BOJ_1699 {

    static int[] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        dp = new int[100001];
        dp[1] = 1;

        for(int i = 2; i <= N; i++){
            int min = 100001;

            for(int j = 1; j <= (int)i/2; j++){
                if (j*j == i){
                    min = 1;
                    break;
                }
                else{
                    min = Math.min(min, dp[j] + dp[i - j]);
                }
            }
            dp[i] = min;
        }

        System.out.println(dp[N]);
    }
}
