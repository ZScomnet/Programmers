//import java.util.*;
//import java.io.*;
//
//class Solution {
//    public static String timeToString(int year,int month,int day,int hour,int min, double sec){
//        String start = ""+year+"-";
//        if(month < 10) start += "0"+month+"-"; else start += month+"-";
//        if(day < 10) start += "0"+day+" "; else start += day+" ";
//        if(hour < 10) start += "0"+hour+":"; else start += hour+":";
//        if(min < 10) start += "0"+min+":"; else start += min+":";
//        if(sec < 10) start += "0"+sec; else start += sec;
//        return start;
//    }
//
//    public static String startTime(String[] log){
//        String[] date = log[0].split("-");
//        int year=Integer.parseInt(date[0]),month=Integer.parseInt(date[1]),day=Integer.parseInt(date[2]);
//        String[] time = log[1].split(":");
//        int hour=Integer.parseInt(time[0]),min=Integer.parseInt(time[1]);
//        double sec=Double.parseDouble(time[2]);
//        String[] cost = log[2].split("s");
//        double csec=Double.parseDouble(cost[0]) - 0.001;
//        sec -= csec;
//        if(sec < 0){ sec += 60;  min -= 1; }
//        if(min < 0){ min += 60;  hour -= 1;}
//        if (hour < 0){ hour += 24;  day -= 1;}
//        if(day < 0){
//            month -= 1;
//            if(month == 2) day += 28;
//            else if (month == 4 || month == 6 || month == 9 || month == 11) day += 30;
//            else day += 31;
//        }
//        if(month < 0){ month += 13; year -= 1;}
//        return timeToString(year,month,day,hour,min,sec);
//
//    }
//    public String oneSecond(String t){
//        String[] log = t.split(" ");
//        String[] date = log[0].split("-");
//        int year=Integer.parseInt(date[0]),month=Integer.parseInt(date[1]),day=Integer.parseInt(date[2]);
//        String[] time = log[1].split(":");
//        int hour=Integer.parseInt(time[0]),min=Integer.parseInt(time[1]);
//        double sec=Double.parseDouble(time[2]);
//        sec += 0.999;
//        if(sec > 60) {sec -= 60; min += 1; sec = Math.floor(sec * 1000) / 1000.0;}
//        if(min > 60) {min -= 60; hour += 1;}
//        if(hour > 24) {hour -= 24; day += 1;}
//        if(month == 2 && day > 28) {month += 1; day -= 28;}
//        else if((month == 4 || month == 6 || month == 9 || month == 11) && day > 30) {month += 1; day -= 30;}
//        else if(day > 31) {month += 1; day -= 31;}
//        if(month > 12) {month -= 12; year += 1;}
//
//        return timeToString(year,month,day,hour,min,sec);
//
//    }
//
//    public static boolean compare(String start,String end,String s,String e){
//        if(start.compareTo(s) > 0 && start.compareTo(e) > 0) return false;
//        else if(end.compareTo(s) < 0 && end.compareTo(e) < 0) return false;
//        else return true;
//    }
//
//    public int solution(String[] lines) {
//        String[] start = new String[lines.length];
//        String[] end = new String[lines.length];
//        int answer = 0;
//        for(int i=0;i<lines.length;i++){
//            String[] log = lines[i].split(" ");
//            start[i] = startTime(log);
//            end[i] = log[0]+" "+log[1];
//        }
//        for(int i=0;i<start.length;i++){
//            int cnt = 1;
//            for(int j=i+1;j<start.length;j++)
//                if(compare(start[i],oneSecond(start[i]),start[j],end[j])) cnt++;
//
//            answer = Math.max(answer,cnt);
//            cnt = 1;
//            for(int j=i+1;j<start.length;j++)
//                if(compare(end[i],oneSecond(end[i]),start[j],end[j])) cnt++;
//
//            answer = Math.max(answer,cnt);
//        }
//        return answer;
//    }
//}