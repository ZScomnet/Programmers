import java.util.*;
import java.io.*;

class Solution {
    public int solution(String s) {
        String answer = "";
        String num = "";
        HashMap<String,Integer> number = new HashMap<>();
        number.put("one",1);
        number.put("two",2);
        number.put("three",3);
        number.put("four",4);
        number.put("five",5);
        number.put("six",6);
        number.put("seven",7);
        number.put("eight",8);
        number.put("nine",9);
        number.put("zero",0);

        for(int i=0;i<s.length();i++) {
            if ('0' <= s.charAt(i) && s.charAt(i) <= '9') {
                if (!num.equals("")) answer += number.get(num);
                num = "";
                answer += s.charAt(i);
            } else{
                num += s.charAt(i);
                if(number.containsKey(num)){
                    answer += number.get(num);
                    num = "";
                }
            }
        }
        return Integer.parseInt(answer);
    }
}