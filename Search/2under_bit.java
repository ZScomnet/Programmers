import java.util.*;

class Solution {
    public long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];
        for(int i=0;i<numbers.length;i++){
            if(numbers[i] == 0){
                answer[i] = 1;
                continue;
            }
            long number = numbers[i];
            List<Long> num = new ArrayList<>();
            
            while(number >= 1){
                num.add(number%2);
                number /= 2;
            }
            num.add(Long.valueOf(0));
            for(int j=0;j<num.size()-1;j++){
                if(j == 0 && num.get(0) == 0){
                    num.set(0,Long.valueOf(1));
                    break;
                }
                if(num.get(j) == 1 && num.get(j+1) == 0){
                    num.set(j,Long.valueOf(0));
                    num.set(j+1,Long.valueOf(1));
                    break;
                }
            }
            long result = 0;
            for(int j=0;j<num.size();j++) result += Math.pow(2,j) * num.get(j);
            answer[i] = result;
        }
        return answer;
    }
}