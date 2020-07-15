def duplicates(nums):

	for num in nums:
		if nums[abs(num)] >=0:
			nums[abs(num)] = -nums[abs(num)]
		else:
			print("Repetition found: ", abs(num))
			
if __name__ == "__main__":

	nums = [2,6,5,1,4,3,2,3]
	duplicates(nums)