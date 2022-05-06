def make_chocolate(small,big,goal):
	a=5*big
	if goal>=a:
		b=goal-a
	else:
		b=goal%5
	if b<=small:
		return b
	return -1