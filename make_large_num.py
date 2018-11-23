'''
Arrange a list of numbers such that the number resulting by joining them is the largest possible.
'''
from functional import seq

l = [78, 789, 9, 998, 989, 0]
result = seq(sorted(l, key=(lambda x: list(str(x))), reverse=True)).reduce(lambda x, y: str(x)+str(y))
print ("Result = ", result)
