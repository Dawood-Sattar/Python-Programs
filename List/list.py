# LIST 
''' 
1. list is mutable
2. list allows duplicate values
3. list is ordered collection of items
4. list can store heterogeneous data types

'''
lst=[1,2,3]

# LIST METHODS

''' 1. append() = adds an element at the end of the list'''
lst.append(4)
print("After Append:", lst)

''' 2. extend() = adds multiple elements at the end of the list'''
lst.extend([5,6,7])
print("After Extend:", lst)

''' 3. insert() = adds an element at the specified index'''
lst.insert(0,0) # inserts 0 at index 0
print("After Insert:", lst)

''' 4. remove() = removes the first occurrence of the specified element'''
lst.remove(3) # removes 3 from the list
print("After Remove:", lst)

''' 5. pop() = removes and returns the element at the specified index'''
popped_element = lst.pop(2) # removes and returns element at index 2
print("Popped Element:", popped_element)

''' 6. index() = returns the index of the first occurrence of the specified element'''
index_of_5 = lst.index(5)
print("Index of 5:", index_of_5)

''' 7. count() = returns the number of occurrences of the specified element'''
count_of_2 = lst.count(2)
print("Count of 2:", count_of_2)

''' 8. sort() = sorts the list in ascending order'''
lst.sort()
print("Sorted List:", lst)

''' 9. reverse() = reverses the order of the list'''
lst.reverse()

print("Reversed List:", lst)

''' 10. clear() = removes all elements from the list'''
lst.clear()
print("Cleared List:", lst)

