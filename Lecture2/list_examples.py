# student_data = ['A022343234', [99,70,85.0], 'P']
#
# print(student_data[0]) #access first element in list
# print(student_data[-1]) #access last element in list
# print(len(student_data)) #length of list
#
# student_data.append(10) #adds 10 to send of list
# print(student_data)
#
# p_value = student_data.pop(2) # gets 'P' from list and removes from list
# print(student_data)
# print(p_value)
#
# del student_data[0]
# # student_data.remove('A022343234') # only removes object with value from list
# print(student_data)
#
# new_list = list('hello') #create new list with characters in string
# print(new_list)
#
# new_list[0] = 'j'
# print(new_list)
#
# del new_list[-1] #-1 is last value in list
# print(new_list)

# next slide!

list_name = ['amy', 'jeff', 'eric', 'emily', 'jacq', 'zack', 'barry']
print(list_name)

#.methods operate on the list itself
list_name.sort()
print('sorted', list_name)

list_name.reverse()
print('reversed: ', list_name)

#built in functions create a new list after the operation
new_sorted_list_name = sorted(list_name)
print('new sorted list: ', new_sorted_list_name)
print('original list: ', list_name)

print(dir(new_sorted_list_name)) #return list of valid attributes for object