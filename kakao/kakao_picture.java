//import java.util.*;
//import java.io.*;
//
//class Solution {
//    private static int result = 0;
//    private static int[][] term = new int[8][8];
//    private static char[][] rel = new char[8][8];
//    private static int[] line = {-1,-1,-1,-1,-1,-1,-1,-1};
//
//    public static boolean compare(int left,int right,int depth,int idx){
//        if(left == right) return false;
//        if(rel[left][right] == '<' && Math.abs(depth-idx) >= term[left][right]+1) return false;
//        if(rel[left][right] == '=' && Math.abs(depth-idx) != term[left][right]+1) return false;
//        if(rel[left][right] == '>' && Math.abs(depth-idx) <= term[left][right]+1) return false;
//        if(rel[right][left] == '<' && Math.abs(depth-idx) >= term[right][left]+1) return false;
//        if(rel[right][left] == '=' && Math.abs(depth-idx) != term[right][left]+1) return false;
//        if(rel[right][left] == '>' && Math.abs(depth-idx) <= term[right][left]+1) return false;
//        else return true;
//    }
//
//    public static void dfs(int depth){
//        if(depth == 8){
//            result++;
//            return;
//        }
//        for(int i=0;i<8;i++) { // i = friends
//            boolean set = true;
//            for(int j=0;j<depth;j++) // j = friends_idx
//                if(!compare(i,line[j],depth,j)) set = false;
//            if(set){
//                line[depth] = i;
//                dfs(depth+1);
//                line[depth] = -1;
//            }
//        }
//    }
//    public int solution(int n, String[] data) {
//        for(int i=0;i<8;i++) line[i] = -1;
//        char[] f = {'A','C','F','J','M','N','R','T'};
//        HashMap<Character,Integer> friends = new HashMap<>();
//        for(int i=0;i<8;i++) friends.put(f[i],i);
//        for(String s : data){
//            int left = friends.get(s.charAt(0)),right = friends.get(s.charAt(2)),length = Character.getNumericValue(s.charAt(4));
//            char cmp = s.charAt(3);
//            term[left][right] = length;
//            term[right][left] = length;
//            rel[left][right] = cmp;
//            rel[right][left] = cmp;
//        }
//        dfs(0);
//        return result;
//    }
//}