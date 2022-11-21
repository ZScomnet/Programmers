import sys
input = sys.stdin.readline

# def solution():
#     s1 = input().strip()
#     s2 = input().strip()
#     start,end = 0,1
#     answer = 0
#     while start < len(s1):
#         s = s1[start:end]
#         if s in s2:
#             answer = max(answer,len(s))
#             end += 1
#             if end > len(s1):
#                 break
#         else:
#             start += 1
#             if start == end:
#                 end += 1
#     return answer

def solution():
    s1 = input().strip()
    s2 = input().strip()
    answer = 0
    dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                answer = max(answer,dp[i][j])

    return answer

if __name__ == "__main__":
    print(solution())