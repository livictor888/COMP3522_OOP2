# dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
# keys = dishes.keys()
# values = dishes.values()
# # print(keys)
# print(values)
#
# # Use a view for iteration
# n = 0
# for val in values: #values contains (2, 1, 1, 500)
#     n += val
# print(n)

# for (name,age) in [("James", 22), ("Danica", 35), ("Rohit",28)]:
#     if age > 30:
#         print("Name: {0}, Age: {1}".format(name, age))
#         break

for val in "string":
    if val == "i":
        continue
    print(val, end='')
print("\nThe end")
