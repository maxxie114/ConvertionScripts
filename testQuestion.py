def isEven(num):
  result = []
  for i in range(len(num)):
    if num[i] % 2 == 0:
      result.insert(0, True) 
    else:
      result.insert(0, False) 
  return result
lst = [1,3,5,8,6]
print(isEven(lst))
