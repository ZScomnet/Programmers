def solution(balance, transaction, abnormal):
    answer = 0
    ban = [0] * 101
    for i in abnormal:
        ban[i] = 1
    stack = [[[i+1,balance[i]]] for i in range(len(balance))]
    for i in transaction:
        fr,to,cost = i
        fr,to = fr-1,to-1
        total = 0
        while total != cost:
            user,money = stack[fr].pop()
            if total+money <= cost:
                stack[to].append([user,money])
                total+=money
            else:
                stack[to].append([user,cost-total])
                stack[fr].append([user,money-(cost-total)])
                total += cost-total
    answer = [0] * len(balance)
    for i in range(len(stack)):
        for part in stack[i]:
            user,money = part
            if ban[user] != 1:
                answer[i] += money
    return answer
print(solution([30, 30, 30, 30],[[1, 2, 10], [2, 3, 20], [3, 4, 5], [3, 4, 30]],[2,3]))