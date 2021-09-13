import sys

input = sys.stdin.readline

def histogram(line):
	memory = []
	minsquare = line[0]
	before = 1
	answer = 0
	mix = True
	for i in range(len(line)):
		if len(memory) == 0:
			memory.append(line[i])
		else:
			if minsquare > line[i]:
				minsquare = line[i]
			if memory[-1] <= line[i]:
				memory.append(line[i])
			else:
				cnt = 0
				area = 0
				now,after = 0,0

				print(memory,answer)
				while memory:
					now = memory.pop()
					cnt += 1
					if area < now*cnt:
						area = now*cnt
						after = now
				if now == after and answer != 0 and mix:
					if after == before:
						answer += area
						memory.append(line[i])
						continue
					elif after > before:
						if answer < answer+int(area*(before/after)):
							answer = answer+int(area*(before/after))
							mix = True
						elif answer < area:
							answer = area
							mix = True
						else:
							mix = False
					else:
						if answer < area+int(answer*(after/before)):
							answer = area+int(answer*(after/before))
							mix = True
						elif answer < area:
							answer = area
							mix = True
						else:
							mix = False
				else:
					if answer <= area:
						answer = area
				before = after
				memory.append(line[i])
	if memory:
		cnt = 0
		now = 0
		area = 0
		while memory:
			now = memory.pop()
			cnt += 1
			if area < now*cnt:
				area = now*cnt
				after = now
		if answer == 0:
			answer = area
		elif now == after and mix:
			if after == before:
				answer += area
			elif after > before:
				if answer < answer+int(area*(before/after)):
					answer = answer+int(area*(before/after))
				elif answer < area:
					answer = area
			else:
				if answer < area+int(answer*(after/before)):
					answer = area+int(answer*(after/before))
				elif answer < area:
					answer = area
		else:
			if answer < area:
				answer = area
	if minsquare*len(line) > answer:
		answer = minsquare*len(line)
	return answer

if __name__ == "__main__":
	while True:
		line = list(map(int,input().split()))
		if line[0] != 0:
			print(max(histogram(line[1:]),histogram(line[1:][::-1])))
		else:
			break
		