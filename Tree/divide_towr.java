import java.util.*;

class Solution {
    public int dfs(Map<Integer,ArrayList<Integer>> tree, int now,int[] counter){
        int result = 1;
        counter[now] = 1;
        for(int next : tree.get(now))
            if(counter[next] == 0) {
                counter[next] = 1;
                result += dfs(tree,next,counter);
            }
        return result;
    }
    
    public int solution(int n, int[][] wires) {
        int answer = 99999999;
        Map<Integer,ArrayList<Integer>> tree = new HashMap<>();
        for(int[] w : wires){
            int start = w[0],end = w[1];
            if(tree.containsKey(w[0])){
                ArrayList<Integer> node = tree.get(w[0]);
                node.add(w[1]);
                tree.put(w[0],node);
            }else{
                ArrayList<Integer> node = new ArrayList<>();
                node.add(w[1]);
                tree.put(w[0],node);
            }
            if(tree.containsKey(w[1])){
                ArrayList<Integer> node = tree.get(w[1]);
                node.add(w[0]);
                tree.put(w[1],node);
            }else{
                ArrayList<Integer> node = new ArrayList<>();
                node.add(w[0]);
                tree.put(w[1],node);
            }
        }
        for(int[] w : wires){
            int[] counter = new int[n+1];
            counter[w[0]] = 1;
            counter[w[1]] = 1;
            int left = dfs(tree,w[0],counter);
            int right = dfs(tree,w[1],counter);
            answer = Math.min(Math.abs(left-right),answer);
        }
        
        return answer;
    }
}