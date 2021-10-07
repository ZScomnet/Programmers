import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
	N = int(input())
	for _ in range(N):
		doc,idx = map(int,input().split())
		q_idx = deque([i for i in range(doc)])
		q_doc = deque(list(map(int,input().split())))
		stack_doc = sorted(q_doc)
		cnt = 0
		while q_idx:
			if q_doc[0] == stack_doc[-1]:
				cnt += 1
				q_doc.popleft()
				stack_doc.pop()
				if idx == q_idx.popleft():
					print(cnt)
					break
			else:
				q_doc.append(q_doc.popleft())
				q_idx.append(q_idx.popleft())