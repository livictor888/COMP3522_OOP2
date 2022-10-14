# dict = {'A': 'def A', 'B': 'def B'}
#
# new_dict = { k.lower(): v for k, v in dict.items()}
# print(new_dict)

# replaced = [x if x % 2 == 0 else 'x' for x in range(0,10)]
# print(replaced)

#import this
#
# flatten_matrix = []
# matrix = [[1,2,3], [4,5], [6,7,8]]
#
# for sublist in matrix:
#     for val in sublist:
#         flatten_matrix.append(val)
#
# print(flatten_matrix)
#
# flatten_matrix2 = [val
#                    for sublist in matrix
#                    for val in sublist
#                     ]
# print(flatten_matrix2)

# class Wallet:
#     def __init__(self):
#         self._money = 999;
#     def remove(self, x):
#         self._money -= x
#
# class Customer:
#     def __init__(self):
#         self.wallet = Wallet()
#     def getWallet(self):
#         return self.wallet
#
# class Cashier:
#     def __init__(self):
#         self._money = 0
#
#     def getMoneyFrom(self, other, x):
#         other.getWallet().remove(x)
#         self._money += x;
#
# cashier = Cashier()
# customer = Customer()
# cashier.getMoneyFrom(customer, 100);
import enum
from enum import auto
class FileType(enum.Enum):
    JSON = auto()
    TXT = auto()

file_names = ['birds.json', 'cats.txt', 'dogs.txt']
types_list = [FileType.JSON if '.json' in x else FileType.TXT for x in file_names]
print(types_list)