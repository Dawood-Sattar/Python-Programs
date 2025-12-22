test_List=[1,2,3,4,5,6,7,8,9,10]

# 1. [start:end:step] - slicing with step 
# 2. When I do not provide start, it starts from index 0
# 3. When I do not provide end, it goes up to the last index

print("Printing Even from list: ",test_List[::2])

# 4. Printing Odd from list
print("Printing Odd from list: ",test_List[1::2])

# 5. printing Original Lists last 5 elements with possitive indexing
print("Printing last 5 elements with possitive indexing: ",test_List[5:])

# 6. printing Original Lists last 5 elements with negative indexing
print("Printing last 5 elements with negative indexing: ",test_List[-5:])

# 7. printing Middle 2 elements of the list
print("Printing Middle 2 elements of the list: ",test_List[4:-4])

# 8. printing the list in reverse order
print("Printing the list in reverse order: ",test_List[::-1])