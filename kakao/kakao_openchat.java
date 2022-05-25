import java.util.*;
import java.io.*;

class Solution {
    public String[] solution(String[] record) {
        HashMap<String,String> user = new HashMap<>();
        HashMap<String,Boolean> is_chat = new HashMap<>();
        List<String> result = new ArrayList<>();

        for(String r : record){
            String[] command = r.split(" ");
            if(command[0].equals("Enter")){
                user.put(command[1],command[2]);
                is_chat.put(command[1],true);
                result.add(r);
            }else if(command[0].equals("Leave")){
                is_chat.put(command[1],false);
                result.add(r);
            }else{
                user.put(command[1],command[2]);
            }
        }
        String[] answer = new String[result.size()];

        for(int i=0;i<result.size();i++){
            String[] command = result.get(i).split(" ");
            if(command[0].equals("Enter"))
                answer[i] = user.get(command[1])+"님이 들어왔습니다.";
            else
                answer[i] = user.get(command[1])+"님이 나갔습니다.";
        }
        return answer;
    }
}