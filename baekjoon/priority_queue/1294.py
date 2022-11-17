import sys
import heapq

input = sys.stdin.readline

class string:
	def __init__(self,s):
		self.s = s

	def __lt__(self,other):
		if self.s + other.s < other.s + self.s:
			return True
		else:
			return False

	def getString(self):
		return self.s

def solution():
	answer = ""
	words = []
	for _ in range(int(input())):
		# heapq.heappush(words,string('A'*1000))
		heapq.heappush(words,string(input().strip()))
	while words:
		s = heapq.heappop(words).getString()
		answer += s[0]
		if len(s) > 1:
			heapq.heappush(words,string(s[1:]))
		
	return answer

if __name__ == "__main__":
	print(solution())