# Find Duplicates from a List: Write a function to Find duplicates from a list
def find_dupes(lst):
	#checks if list is empty
    if not lst:
        return 'Empty List'
    #stores elements that are duplicates but only once    
    non_duplicate_list = []
    #iterates through each element of the list 
    for i in range(len(lst)):
    	#starts from the next element after i and goes to end list this ensures that each pair of elements is checked only once
        for j in range(i+1,len(lst)):
        	#checks if i and j are the same and if they are add it to new list
            if lst[i] == lst[j] and lst[i] not in non_duplicate_list:
                non_duplicate_list.append(lst[i])
    return non_duplicate_list
my_duplicate_list = ['Apple','mango','Apple','CR7','CR7','CR7']
print("Duplicate Elements in the given list :", find_dupes(my_duplicate_list))