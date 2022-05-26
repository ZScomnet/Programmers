//import java.util.*;
//import java.io.*;
//
//class Solution {
//    public int[] solution(int m, int n, int[][] picture) {
//        int[][] visited = new int[m][n];
//        int[] answer = new int[2];
//        int[][] d ={{-1,0},{0,1},{1,0},{0,-1}};
//        for(int i=0;i<m;i++)
//            for(int j=0;j<n;j++) visited[i][j] = picture[i][j];
//
//        for(int i=0;i<m;i++){
//            for(int j=0;j<n;j++){
//                if(visited[i][j] == -1 || visited[i][j] == 0) continue;
//                Queue<Integer> r = new LinkedList<>();
//                Queue<Integer> c = new LinkedList<>();
//                r.add(i);
//                c.add(j);
//                answer[0]++;
//                int areaValue = visited[i][j];
//                int area = 0;
//                while(!r.isEmpty() && !c.isEmpty()){
//                    int row = r.poll();
//                    int col = c.poll();
//                    visited[row][col] = -1;
//                    area++;
//                    for(int[] s : d){
//                        int drow=s[0],dcol=s[1];
//                        if(0 <= row+drow && row+drow < m && 0 <= col+dcol && col+dcol < n)
//                            if(visited[row+drow][col+dcol] == areaValue){
//                                visited[row+drow][col+dcol] = -1;
//                                r.add(row+drow);
//                                c.add(col+dcol);
//                            }
//
//                    }
//                    answer[1] = Math.max(answer[1],area);
//                }
//            }
//        }
//
//
//        return answer;
//    }
//}