import java.util.*;

class Solution {
    ArrayList<String> answer = new ArrayList<>();
    
    public void set_answer(ArrayList<String> stack){
        for(int i=0;i<stack.size();i++)
            answer.set(i,stack.get(i));
    }
    
    public void search(int depth, HashMap<String,ArrayList<String>> dic, String now, ArrayList<String> stack){
        if (stack.size() == depth){
            if(answer.size() != 0){
                for(int i=0;i<depth;i++)
                    if(stack.get(i).compareTo(answer.get(i)) < 0)
                        set_answer(stack);
                    else if(stack.get(i).compareTo(answer.get(i)) > 0)
                        break;
            }else
                 for(String s : stack)
                    answer.add(s);
            return;
        }
        else if (dic.get(now) != null){
            for(int i=0;i<dic.get(now).size();i++){
                if(dic.get(now).get(i) != "-"){
                    String temp = dic.get(now).get(i);
                    dic.get(now).set(i,"-");
                    stack.add(temp);
                    search(depth,dic,temp,stack);
                    stack.remove(stack.size()-1);
                    dic.get(now).set(i,temp);
                }
            }
        }
    }
    
    public String[] solution(String[][] tickets) {
        ArrayList<String> stack = new ArrayList<>();
        HashMap<String,ArrayList<String>> dic = new HashMap<>();
        for (String[] ticket : tickets){
            if(dic.get(ticket[0]) == null){
                ArrayList<String> end = new ArrayList<>();
                dic.put(ticket[0],end);
            }
            dic.get(ticket[0]).add(ticket[1]);
        }
        stack.add("ICN");
        search(tickets.length+1,dic,"ICN",stack);
        String[] result = new String[tickets.length+1];
        for(int i=0;i<tickets.length+1;i++)
            result[i] = answer.get(i);
        return result;        
    }
}