number_list = [5, 1, 20, 10, 15]
print(number_list)

number_list.append(50)
print(number_list)

number_list.insert(1, 30)
print(number_list)

number_list.remove(1)
print(number_list)

number_list.sort()
print(number_list)

number_list.reverse()
print(number_list)

# boolean expression
print(10 in number_list)
print(90 in number_list)

#find repeated elements
print(number_list.count(30))
print(number_list.count(45))

#find the index of an element
print(number_list.index(20))
print(number_list.index(5))

#copy the entire list
number_list_2 = number_list.copy()
print(number_list_2)

#pop the last element of the list
number_list.pop()
print(number_list)

#clear the entire list
number_list_2.clear()
print(number_list_2)
