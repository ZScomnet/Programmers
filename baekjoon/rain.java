import java.util.*;
import java.io.*;

public class Main{
	private static int[][] wall;
	private static int row,col;
	private static int answer = 0;
	private static int left,water,h;

	static void solution(){
		for(int i=row-1;i>=0;i--){
			left = 0;
			water = 0;
			for(int j=0;j<col;j++){
				if(wall[i][j] == 1 && left == 0){
					left = 1;
				}else if(wall[i][j] == 1 && left == 1){
					answer += water;
					water = 0;
				}else if(left == 1 && wall[i][j] == 0){
					water++;
				}
			}
		}
		System.out.println(answer);
	}

	public static void main(String args[]) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		row = Integer.parseInt(st.nextToken());
		col = Integer.parseInt(st.nextToken());
		wall = new int[row][col];
		st = new StringTokenizer(br.readLine());
		for(int j=0;j<col;j++){
			int h = Integer.parseInt(st.nextToken());
			for(int i=row-1;i>=0;i--){
				if(h>0){
					wall[i][j] = 1;
					h--;
				}else{
					wall[i][j] = 0;
				}
			}
		}
		solution();
	}
}