import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        Queue<Integer> r = new LinkedList<>();
        Queue<Integer> c = new LinkedList<>();
        Queue<Integer> cnt = new LinkedList<>();
        int[] dy = {-1,0,1,0}, dx = {0,1,0,-1};
        r.add(0);
        c.add(0);
        cnt.add(1);
        while(r.size() > 0){
            int row = r.poll(), col = c.poll(), count = cnt.poll();
            maps[row][col] = -1;
            if(row == maps.length-1 && col == maps[0].length-1) return count;
            for(int i=0;i<4;i++){
                int drow = dy[i], dcol = dx[i];
                if(0 <= row+drow && row+drow < maps.length && 0 <= col+dcol && col+dcol < maps[0].length)
                    if(maps[row+drow][col+dcol] == 1){
                        maps[row+drow][col+dcol] = -1;
                        r.add(row+drow);
                        c.add(col+dcol);
                        cnt.add(count+1);
                    }
            }
        } 
        
        return -1;
    }
}