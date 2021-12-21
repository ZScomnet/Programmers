def gcd(w,h):
	r = 0
	while h != 0:
		r = w%h
		w = h
		h = r
	return w
	
def solution(w,h):
	divide = gcd(w,h)
	cut = w+h-divide
	return w*h-cut

if __name__ == "__main__":
	w = int(input())
	h = int(input())
	print(solution(w,h))