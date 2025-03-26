# Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
def main(num1,num2):
	product = num1*num2
	if (product <=1000):
		return product
	return num1+num2
	
print(main(20,30))		
print(main(40,30))