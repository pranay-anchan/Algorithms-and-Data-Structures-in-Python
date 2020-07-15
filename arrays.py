numbers = [10,20,30,40,50];

# random indexing --> O(1)
#print (numbers[4]);

#for num in numbers:
#	print(num);

#for i in range(len(numbers)):
#	print(numbers[i]);

#print(numbers[:-2]);

maximum = numbers[0];
for num in numbers:
	if num > maximum:
		maximum = num;

print(maximum);