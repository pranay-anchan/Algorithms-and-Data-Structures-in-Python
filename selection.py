
def selection_sort(nums):

	for i in range(len(nums)-1):
		index = i
		
		for j in range(i+1,len(nums),1):
			if nums[j] < nums[index]:
				index = j
				
		if index != i:
			swap(nums, index, i)
			
	return nums
	
def swap(nums,i,j):
	temps = nums[i]
	nums[i] = nums[j]
	nums[j] = temps
	
if __name__ == "__main__":

	nums = [5,2,1,7,6,8,8,0]
	
	print(selection_sort(nums))