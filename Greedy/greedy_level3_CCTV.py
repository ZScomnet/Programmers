def solution(routes):
	routes = sorted(routes, key=lambda route: route[1])
	CCTV = [routes[0][1]]

	for i in routes:
		start,end = i[0],i[1]
		non_CCTV = True
		for camera in CCTV:
			if start <= camera and camera <= end:
				non_CCTV = False
				break
		if non_CCTV:
			CCTV.append(end)
	return len(CCTV)

print(solution([[-20,15],[-14,-5],[-18,-13],[-5,-3]]))