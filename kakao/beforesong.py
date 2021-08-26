def solution(m,musicinfos):
	answer = "(None)"
	time = 0
	dic = {"C" : 1,"C#" : 2, "D": 3,"D#" : 4,"E":5,"E#":6,
	"F":7,"F#":8,"G":9,"G#":10,"A":11,"A#":12,"B":13,"B#":14}
	m_stack = []
	for i in range(len(m)):
		if i != len(m)-1:
			if m[i+1] == '#':
				m_stack.append(dic[m[i:i+2]])
			elif m[i] != '#':
				m_stack.append(dic[m[i]])
		elif m[i] != '#':
			m_stack.append(dic[m[i]])
	for music in musicinfos:
		start,end,name,melody = music.split(',')
		full_time = int(end[:2]) * 60 + int(end[3:5]) - int(start[:2]) * 60 - int(start[3:5])

		music_stack = []
		for i in range(len(melody)):
			if i != len(melody)-1:
				if melody[i+1] == '#':
					music_stack.append(dic[melody[i:i+2]])
				elif melody[i] != '#':
					music_stack.append(dic[melody[i]])
			elif melody[i] != '#':
				music_stack.append(dic[melody[i]])
		if full_time > len(music_stack):
			index = 0
			while full_time > len(music_stack):
				music_stack.append(music_stack[index])
				index += 1
		elif full_time < len(music_stack):
			while full_time < len(music_stack):
				music_stack.pop()

		for i in range(len(music_stack)-len(m_stack)+1):
			if m_stack == music_stack[i:i+len(m_stack)]:
				if time < full_time:
					answer = name
					time = full_time
				break
	return answer

if __name__ == "__main__":
	print(solution("AAA",["12:00,12:14,HELLO,ABCDEFG", "13:00,13:15,WORLD,AAA"]))