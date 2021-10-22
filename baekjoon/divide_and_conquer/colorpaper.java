import java.util.*;
import java.io.*;

public class Main{

	static int N;
	static int[][] paper;
	static int white,blue = 0;

	static int divide(int length,int row,int col){
		if(length == 1){
			return paper[row][col];
		}
		else{
			int ul = divide(length/2,row,col);
			int ur = divide(length/2,row,col+length/2);
			int dl = divide(length/2,row+length/2,col);
			int dr = divide(length/2,row+length/2,col+length/2);
			if(ul == 0 && ur == 0 && dl == 0 && dr == 0){
				return 0;
			}
			else if(ul == 1 && ur == 1 && dl == 1 && dr == 1){
				return 1;
			}
			else{
				if(ul == 0){
					white++;
				}
				else if(ul == 1){
					blue++;
				}
				if(ur == 0){
					white++;
				}
				else if(ur == 1){
					blue++;
				}
				if(dl == 0){
					white++;
				}
				else if(dl == 1){
					blue++;
				}
				if(dr == 0){
					white++;
				}
				else if(dr == 1){
					blue++;
				}
			}
		}
		return -1;
	}

	static void solution(){
		int result = divide(N,0,0);
		if(result == 0){
			white++;
		}else if(result == 1){
			blue++;
		}
		System.out.println(white);
		System.out.println(blue);
	}


	public static void main(String args[]) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		paper = new int[N][N];
		for(int i=0;i<N;i++){
			st = new StringTokenizer(br.readLine());
			for(int j=0;j<N;j++){
				paper[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		solution();
	}
}