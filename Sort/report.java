import java.util.*;
import java.io.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        HashMap<String,Integer> cnt = new HashMap<>();
        HashMap<String,Integer> idx = new HashMap<>();
        Arrays.sort(report);
        String before = "";
        
        for(int i=0;i<id_list.length;i++) {
            cnt.put(id_list[i],0);
            idx.put(id_list[i],i);
        }
        for(String r : report){
            if(before.equals(r)) continue;
            before = r;
            String[] re = r.split(" ");
            cnt.put(re[1],cnt.get(re[1])+1);
        }
        before = "";
        for(String r : report){
            if(before.equals(r)) continue;
            before = r;
            String[] re = r.split(" ");
            if(cnt.get(re[1]) >= k) answer[idx.get(re[0])] += 1;
        }
        return answer;
    }
}