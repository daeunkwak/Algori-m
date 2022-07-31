/*
 author : https://github.com/daeunkwak/Problem-Solving
 title : 가장 큰 바이토닉 부분 수열
 description : 다이나믹 프로그래밍
 date : 2022-07-29
 */

package DP;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_11054 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int maxx = 0;
        for(int i = 0; i < N; i++){
            int res = howLong(arr, i);
            if (res > maxx){
                maxx = res;
            }
        }
        System.out.println(maxx);
    }

    // 문제점은 arr[idx]값을 빼고 지들끼리만 비교한다는것!
    // <-> idx를 기준으로 작거나 큰 조건도 만족하는지 확인해야한다.
    public static int howLong(int[] arr, int idx){
        int max = 0;
        int[] dp_left = new int[idx + 1];
        int[] dp_right = new int[arr.length - idx + 1];

        // 증가하는 수열 부분
        dp_left[0] = 1;
        for (int i = 1; i < (idx + 1); i++) {
            dp_left[i] = 1;
            for (int j = 0; j < i; j++) {
                if (arr[j] < arr[i] && dp_left[i] <= dp_left[j]) {
                    dp_left[i] = dp_left[j] + 1;
                }
            }
        }

        // 감소하는 수열 부분
        dp_right[1] = 1;
        for (int i = idx+2; i <= arr.length-idx-1; i++) {
            dp_right[i] = 1;
            for (int j = idx+1; j < i; j++) {
                if (arr[i] < arr[j] && dp_right[i] <= dp_right[j]) {
                    dp_right[i] = dp_right[j] + 1;
                } else if (arr[i] == arr[j]) {
                    dp_right[i] = dp_right[j];
                }
            }
        }

        // 최대길이 리턴
        Arrays.sort(dp_left);
        Arrays.sort(dp_right);
        max = dp_left[idx] + dp_right[arr.length - idx];
        System.out.println("max : " + max);
        return max;
    }
}
