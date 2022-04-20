def solution(a,b,g,s,w,t):
	left, right = 1, int(1e9 * 2 * 1e5 * 2) # time
	mid = (left+right) // 2
	while left < right:
		gold,silver,move_metal = 0,0,0
		mid = (left+right) // 2
		# print(left,mid,right)
		for dg,ds,dw,dt in zip(g,s,w,t):
			 time = mid // (2*dt) + (mid % (2*dt)) // dt
			 total = dw*time
			 # print(dw,time)
			 if dg < total:
			 	gold += dg
			 else:
			 	gold += total

			 if ds < total:
			 	silver += ds
			 else:
			 	silver += total

			 if dg+ds < total:
			 	move_metal += dg+ds
			 else:
			 	move_metal += total
		# print(a,b,gold_max,silver_min,gold_min,silver_max,all_metal)
		if a <= gold and b <= silver and a+b <= move_metal:
			right = mid
		else:
			left = mid+1
	# print(left,mid,right)
	return left

if __name__ == "__main__":
	print(solution(10,10,[5,5],[5,5],[2,2],[3,3]))