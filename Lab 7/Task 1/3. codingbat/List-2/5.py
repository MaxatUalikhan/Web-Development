def sum67(nums):
	a=0
	b=False
	for i in range(len(nums)):
		if nums[i]==6:
			b=True
		if not b:
			a+=nums[i]
		if nums[i]==7 and b:
			b=False
	return a