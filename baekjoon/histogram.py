import sys

input = sys.stdin.readline

def histogram(line):
	result = 0
	stack = []
	before = 0
	for i in range(1,len(line)):
		if len(stack) == 0:
			stack.append(line[i])
		else:
			if stack[-1] > line[i]:
				length = 1
				area = 0
				now = 0
				while stack:
					now = stack.pop()
					if area < now*length:
						area = now*length
						before = now
					length += 1
				if now == before:
					result += area
				elif area > result:
					result = area
			else:
				stack.append(line[i])
		print(stack,before,result)
	if len(stack) != 0:
		length = 1
		area = 0
		now = 0
		while stack:
			now = stack.pop()
			if area < now*length:
				area = now * length
				before = now
			length += 1
		if now == before:
			result += area
		elif area > result:
			result = area

	return result

if __name__ == "__main__":
	while True:
		line = list(map(int,input().split()))
		if line[0] == 0:
			break
		print(histogram(line))