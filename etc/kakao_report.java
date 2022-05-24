import java.util.*;
import java.io.*;

public class kakao_report {
    public static void main(String[] args) throws Exception{
        String[] id_list = {"ryan", "con"};
        String[] report = {"ryan con"};
        int k = 0;

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
        for(String r : report){
            if(before.equals(r)) continue;
            before = r;
            String[] re = r.split(" ");
            if(cnt.get(re[1]) >= k) answer[idx.get(re[0])] += 1;
        }
        for(int i=0;i<answer.length;i++) {
            System.out.print(answer[i]);
            System.out.print(" ");
        }
    }
}
