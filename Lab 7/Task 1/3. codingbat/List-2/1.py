def count_evens(nums):
  d=[1 for i in nums if i%2==0]
  return len(d)