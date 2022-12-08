# import json
#
# person_dict = {1 : 3, 2 : 2}
#
# with open('person3.json', 'w') as json_file:
#     # json_data = json.dumps(person_dict)
#     # json_file.write(json_data)
#     json.dump(person_dict, json_file) #same as above 2 lines

import enum
from enum import auto

class ClothingId(enum.Enum):
    shoe1 = auto() #1
    shoe2 = auto() #2
    shoe3 = auto() #3

for x in ClothingId:
    # print(x)
    if(x == ClothingId.shoe1):
        print("shoe1 variable exists")
    if(x.name == 'shoe1'):
        print("shoe1 variable name exists")
    if(x.value == 1):
        print("1 value exists")
    print(x.name)
    print(x.value)


# for x in range(ClothingId.shoeBegin.value, ClothingId.shoeEnd.value):
#     print("shoe id:", x)
# print("Number of Shoes ", ClothingId.shoeEnd.value - ClothingId.shoeBegin.value)
#
# for y in range(ClothingId.pantBegin.value, ClothingId.pantEnd.value):
#     print("pantId id:", y)
# print("Number of Pants", ClothingId.pantEnd.value - ClothingId.pantBegin.value)
#
# print("Number of Clothes:", ClothingId.numClothes.value - 1)