def is_anagram(str1, str2):
	
	if len(str1) != len(str2):
		return False
		
	str1 = sorted(str1)
	str2 = sorted(str2)
	
	print(str1)
	print(str2)
	
	for i in range(0, len(str1)):
		if str1[i] != str2[i]:
			return False
			
	return True
	
if __name__ == "__main__":

	str1 = 'restful'
	str2 = 'fluster'
	
	print(is_anagram(str1, str2))
	