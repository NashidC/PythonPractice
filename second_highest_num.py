#Find the second highest number in a list
#define function, convert list into set to remove duplicates, sort list, 
#retrieve second to last element

def main(nums):
    nums = list(set(nums))
    nums.sort()
    return nums[-2]

print(main([67,6,4,4,3,222,4]))