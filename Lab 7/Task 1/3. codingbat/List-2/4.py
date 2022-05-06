def sum13(nums):
	a=0
	b=0
	while b<len(nums):
		if nums[b]==13:
			b+=1
		else:
			a+=nums[b]
		b+=1
	return a