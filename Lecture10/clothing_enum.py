import enum
from enum import auto


class ClothingId(enum.Enum):
    shoeBegin = shoe1 = auto()  # 1
    shoe2 = auto()  # 2
    shoe3 = auto()  # 3
    shoeEnd = pantBegin = pant1 = auto()  # 4
    pant2 = auto()  # 5
    pant3 = auto()  # 6
    pant4 = auto()  # 7
    pant5 = auto()  # 8
    pantEnd = numClothes = auto()  # 9


for x in range(ClothingId.shoeBegin.value, ClothingId.shoeEnd.value):
    print("shoe id:", x)
print("Number of Shoes ", ClothingId.shoeEnd.value - ClothingId.shoeBegin.value)

for y in range(ClothingId.pantBegin.value, ClothingId.pantEnd.value):
    print("pantId id:", y)
print("Number of Pants", ClothingId.pantEnd.value - ClothingId.pantBegin.value)

print("Number of Clothes:", ClothingId.numClothes.value - 1)
