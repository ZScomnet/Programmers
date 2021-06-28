def solution(answers):
    p1,p2,p3 = [1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5,]
    score = [0,0,0]
    for i in range(len(answers)):
        if p1[i%5] == answers[i]:
            score[0] += 1
        if p2[i%8] == answers[i]:
            score[1] += 1
        if p3[i%10] == answers[i]:
            score[2] += 1
    answer = []
    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i+1)

    return answer

print(solution([1,2,3,4,5]))