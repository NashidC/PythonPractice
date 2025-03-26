#Write a function to reverse a given list

def reversed(str):
	#base case if empty:
	if str == '':
		return str
	return str[::-1]
print(reversed('hello'))   