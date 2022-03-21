import sys
from collections import deque
input = sys.stdin.readline

room = []
dist = [[0,0]]
dist_length = []
d = [(-1,0),(0,1),(1,0),(0,-1)]
answer = [1e9]

def bfs(R,C,dist_idx):
	start = dist[dist_idx]
	room_cnt = [[0]*C for _ in range(R)]
	room_cnt[start[0]][start[1]] = 1e9
	q = deque([start+[0]])
	while q:
		row,col,cnt = q.popleft()
		for i in d:
			drow,dcol = i
			r,c = row+drow,col+dcol
			if 0 <= r < R and 0 <= c < C:
				if room[r][c] == '.' and room_cnt[r][c] == 0:
					room_cnt[r][c] = cnt+1
					q.append([r,c,cnt+1])
				elif room[r][c] == 'x' or room[r][c] == '.':
					continue
				elif 0 <= room[r][c] < len(dist) and room_cnt[r][c] == 0:
					room_cnt[r][c] = cnt+1
					q.append([r,c,cnt+1])
					dist_length[dist_idx][room[r][c]] = cnt+1
					dist_length[room[r][c]][dist_idx] = cnt+1

def search(depth,now_idx,idx,length):
	if depth == len(dist)-1:
		answer[0] = min(answer[0],length)
	else:
		for i in range(len(idx)):
			if idx[i] == 0:
				idx[i] = 1
				search(depth+1,i,idx,length+dist_length[now_idx][i])
				idx[i] = 0


def solution(R,C):
	for i in range(len(dist)):
		bfs(R,C,i)
	search(0,0,[1]+[0]*(len(dist)-1),0)

	return answer[0]

if __name__ == "__main__":
	while True:
		C,R = map(int,input().split())
		room = []
		dist = [[0,0]]
		answer[0] = 1e9
		for _ in range(R):
			room.append(list(input()))
		dist_cnt = 1
		for row in range(R):
			for col in range(C):
				if room[row][col] == '*':
					dist.append([row,col])
					room[row][col] = dist_cnt
					dist_cnt += 1
				elif room[row][col] == 'o':
					dist[0] = [row,col]
					room[row][col] = 0
		dist_length = [[1e9] * len(dist) for _ in range(len(dist))]
		print(solution(R,C))