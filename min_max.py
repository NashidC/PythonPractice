#Find the Maximum and Minimum Element in a List: Write a function to find the maximum and minimum elements in a list.
#O (n log n) due to sorting
def minMax(elementList):
    elementList = sorted(list(set(elementList)))
    newArr = [elementList[0], elementList[-1]]
    return newArr
print(minMax([3,5,66,78,9,8765]))


#o(n) due to iterating over list
def MinMax2(lst):
    if not lst:
        return 'Empty list'
    # Initialize min and max with the first element of the list
    min_element = lst[0]
    max_element = lst[0]
    for item in lst:
        if isinstance(item, (int, float)):
            if item < min_element:
                min_element = item
            if item > max_element:
                max_element = item
        else:
            return 'Invalid list elements, Non-numeric list'
    return min_element,max_element

list_a = [10,20,30,40,12,31,8,7,11]
min_element, max_element = MinMax2(list_a)
print("Minimum element of the given list is ",min_element)
print("Maximum element of the given list is ",max_element)

