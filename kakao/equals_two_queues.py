from collections import deque

def solution(queue1, queue2):
	queue1 = deque(queue1)
	queue2 = deque(queue2)
	sq1,sq2 = sum(queue1),sum(queue2)
	total = sq1+sq2
	size = len(queue1) + len(queue2)
	for cnt in range(size*2):
		if sq1 > sq2:
			num = queue1.popleft()
			sq1 -= num
			sq2 += num
			queue2.append(num)
		elif sq2 > sq1:
			num = queue2.popleft()
			sq1 += num
			sq2 -= num
			queue1.append(num)
		else:
			return cnt
	return -1

if __name__ == "__main__":
	print(solution([1],[100]))