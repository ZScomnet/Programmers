import java.util.*;
import java.io.*;

public class strzip {
    public static int solution(String s) {
        int answer = s.length();
        for(int size=1;size<s.length()/2+1;size++){
            String result = "";
            String before = s.substring(0,size);
            int cnt = 0;
            for(int idx=0;idx<s.length();idx+=size){
                String next="";
                if(idx+size <s.length()) next = s.substring(idx,idx+size);
                else next = s.substring(idx,s.length());
                if(before.equals(next))
                    cnt++;
                else{
                    if(cnt > 1) result += cnt;
                    result += before;
                    before = next;
                    cnt = 1;
                }
            }
            if(cnt > 1) result += cnt;
            result += before;
            answer = Math.min(result.length(),answer);
        }
        return answer;
    }
    public static void main(String[] args){
        System.out.println(solution("abcabcdede"));
    }
}
