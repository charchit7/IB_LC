arr = [3,0,1,0,4]

def rain_trapped(arr):
	lo = 0
	hi = len(arr) - 1

	left_max = 0
	right_max = 0

	res = 0
	while lo < hi:
		if arr[lo] <= arr[hi]:
			if arr[lo] > left_max:
				left_max = arr[lo]
			else:
				res += left_max - arr[lo]
			lo += 1
		else:
			if arr[hi] > right_max:
				right_max = arr[hi]
			else:
				res += right_max - arr[hi]
			hi += 1
	return res

print(rain_trapped(arr))
		