from enum import Enum

class Category(Enum):
    CATEGORY_1 = 'TECH'
    CATEGORY_2 = 'COOKING'
    CATEGORY_3 = 'TOYS'

print([(tag, tag.value) for tag in Category])