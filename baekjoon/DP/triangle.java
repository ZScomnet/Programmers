import java.util.*;
import java.io.*;

public class Main{
	private static int N;
	private static int[][] triangle;

	static void solution(){
		int max = triangle[0][0];
		for(int i=1;i<N;i++){
			for(int j=0;j<i+1;j++){
				if(j==0){
					triangle[i][j] += triangle[i-1][j];
				}else if(j==i){
					triangle[i][j] += triangle[i-1][i-1];
				}else{
					if(triangle[i-1][j-1] > triangle[i-1][j]){
						triangle[i][j] += triangle[i-1][j-1];
					}else{
						triangle[i][j] += triangle[i-1][j];
					}
				}
				if(i == N-1 && max < triangle[i][j]){
					max = triangle[i][j];
				}
			}
		}
		System.out.println(max);
	}

	public static void main(String args[]) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		triangle = new int[N][N];
		for(int i = 0;i<N;i++){
			st = new StringTokenizer(br.readLine());
			for(int j = 0;j<i+1;j++){
				triangle[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		solution();
	}
}