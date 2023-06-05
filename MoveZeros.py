nums = [0,1,0,3,12]

l=0
for r in range(len(nums)):
    if nums[r]:
        nums[r],nums[l]=nums[l],nums[r]
        l+=1 

print(nums)

