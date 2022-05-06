def centered_average(nums):
  a=sum(nums)-min(nums)-max(nums)
  return a/(len(nums)-2)