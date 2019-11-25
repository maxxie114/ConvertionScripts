# This script take three hex arguments
# convert them to integer
# and sort them
# and print the result out as hex
a = input()
argLst = a.split(" ")

if len(argLst) > 3:
  print("Please only input 3 arguments")
  exit()
elif len(argLst) < 3:
  print("Please do not enter less than three arguments")
  exit()

newLst = []
for i in argLst:
  newLst.append(int(i,16))

# sort
# This algorithm have a problem
sortedLst = []
min = newLst[0]
for i in range(len(newLst)):
  if newLst[i] < min:
    min = newLst[i]

sortedLst.append(min)

if newLst[1] < newLst[2]:
  sortedLst.append(newLst[1])
  sortedLst.append(newLst[2])
else:
  sortedLst.append(newLst[2])
  sortedLst.append(newLst[1])

sortedLstHex = []
for i in range(len(sortedLst)):
  sortedLstHex.append(hex(sortedLst[i]))

print("orgLstHex:",argLst)
print("orgLstInt:",newLst)
print("sortedLst", sortedLst)
print("sortedLstHex:", sortedLstHex)
