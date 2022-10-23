import sys
input = sys.stdin.readline

def solution():
	n = int(input())
	line = list(map(int,input().split()))
	s_min,s_max = [line[0],line[1],line[2]],[line[0],line[1],line[2]]
	for i in range(1,n):
		line = list(map(int,input().split()))
		next_min = [0,0,0]
		next_min[0] = min(s_min[0]+line[0],s_min[1]+line[0])
		next_min[1] = min(s_min[0]+line[1],s_min[1]+line[1],s_min[2]+line[1])
		next_min[2] = min(s_min[1]+line[2],s_min[2]+line[2])
		s_min = next_min

		next_max = [0,0,0]
		next_max[0] = max(s_max[0]+line[0],s_max[1]+line[0])
		next_max[1] = max(s_max[0]+line[1],s_max[1]+line[1],s_max[2]+line[1])
		next_max[2] = max(s_max[1]+line[2],s_max[2]+line[2])
		s_max = next_max

	print(max(s_max),min(s_min))

if __name__ == "__main__":
	solution()