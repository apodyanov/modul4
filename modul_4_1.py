# Задача "А как делить?"

from true_math import divide as divt
from fake_math import divide as divf


result1 = divf(69, 3)
result2 = divf(3, 0)
result3 = divt(49, 7)
result4 = divt(15, 0)


print(result1)
print(result2)
print(result3)
print(result4)