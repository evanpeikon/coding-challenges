# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.
# Assume that each input would have exactly one solution, and you may not use the same element twice
# You can return the answer in any order. 
# Example: if the inputs are nums = [2,7,11,15] and target = 9, the output should be [0,1] since nums[0]+nums[1]==9. 

def twoSum(nums, target):
  solution =[]
  while len(solution)<=2:
    for x in range(0,len(nums)):
      for y in range(0,len(nums)):
        if nums[x]+nums[y]==target and x!=y:
          solution.append(x)
          solution.append(y)
  solution = set(solution)
  return solution
