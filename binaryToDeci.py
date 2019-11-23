a = input("input a binary number: ")
dlst = list(a)
# This part is to generate a binary sequence list that have the size of 100
binaryNum = 1
binaryLst = []
for i in range(100):
  binaryLst.append(binaryNum)
  binaryNum = binaryNum * 2
# binaryLst = [1,2,4,8,16,32,64,128,256,512]
# print(binaryLst)
result = 0
if len(dlst) < 2:
  result = dlst[0]
else:
  for i in range(len(dlst)):
    result = result + int(dlst[i]) * binaryLst[len(dlst)-i-1]
print(result)
