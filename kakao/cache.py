def solution(cacheSize,cities):
	cache = []
	answer = 0
	for city in cities:
		city = city.upper()
		if city in cache:
			answer += 1
			del cache[cache.index(city)]
		elif len(cache) < cacheSize:
			answer += 5
		else:
			answer += 5
			if len(cache) != 0:
				del cache[0]
		if len(cache) < cacheSize:
			cache.append(city)
	return answer
if __name__ == "__main__":
	print(solution(0,	["LA", "LA", "LA", "LA"]))