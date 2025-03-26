def sum_of_elements(lst):
    if not lst:
        return 'Empty List'
    total_sum = 0
    for item in lst:
        if isinstance(item,(int,float)):
            total_sum += item
        else:
            return 'Invalid list'
    return total_sum

x = [1,2,3,4,5,6,7,8,9]        
print("Sum of elements:", sum_of_elements(x))
# Test with an empty list
print("Sum of elements:", sum_of_elements([]))

# Test with a list containing non-numeric values
print("Sum of elements:", sum_of_elements([1, 'a', 3, 4]))