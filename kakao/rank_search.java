import java.util.*;

class Solution {
    private static Map<String,ArrayList<Integer>> dic;
    private static ArrayList<Integer> value;
    public void saveInfo(String[] info, int depth, String key){
        if(depth == 4){
            if(!dic.containsKey(key)) {
                value = new ArrayList<>();
                value.add(Integer.parseInt(info[4]));
                dic.put(key,value);
            }else{
                dic.get(key).add(Integer.parseInt(info[4]));
            }
            return;
        }else{
            saveInfo(info,depth+1,key+"-");
            saveInfo(info,depth+1,key+info[depth]);
        }
    }
    
    public void sortScore(){
        List<String> keys = new ArrayList<>(dic.keySet());
        for(String key : keys)
            Collections.sort(dic.get(key));
    }   
    
    public int getQueryResult(String[] query){
        String getKey = query[0] + query[2] + query[4] + query[6];
        if(!dic.containsKey(getKey)) return 0;
        List<Integer> scores = dic.get(getKey);
        int score = Integer.parseInt(query[7]); 
        int left=0,right= dic.get(getKey).size()-1;
        int mid = (left+right) / 2;
        while(left <= right){
            mid = (left+right) / 2;
            if(scores.get(mid) < score) left = mid+1;
            else right = mid-1;
        }
        return scores.size()-left;
    }
    
    public int[] solution(String[] info, String[] query) {
        int[] answer = new int[query.length];
        dic = new HashMap<>();
        for(String s : info) saveInfo(s.split(" "),0,"");
        sortScore();
        for(int i=0;i<query.length;i++){
            String[] q = query[i].split(" ");
            answer[i] = getQueryResult(q);
        }
        return answer;
    }
}