public class lottos {
    public static int[] Solution(int[] lottos, int[] win_nums){
        int[] answer = {7,7};
        for(int i=0;i<6;i++)
            for(int j=0;j<6;j++)
                if(lottos[i] == win_nums[j]){
                    answer[0]--;
                    answer[1]--;
                    break;
                }else if(lottos[i] == 0){
                    answer[0]--;
                    break;
                }
        if(answer[0] == 7) answer[0] = 6;
        if(answer[0] == 7) answer[1] = 6;
        return answer;
    }

    public static void main(String[] args) throws Exception{
        int[] lottos = {0,0,0,0,0,0};
        int[] win_nums = {1,2,3,4,5,6};
        System.out.println(Solution(lottos,win_nums));

    }
}
