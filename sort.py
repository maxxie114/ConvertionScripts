#############################################################################
# This is an implementation of selection sort                               #
#############################################################################
def min(lst):
  """
   This function will return the index of the smallest item in a list
  """
  if(len(lst) == 0):
    return 0
  min = lst[0]
  minIndex = 0
  for i in range(len(lst)):
    if min > lst[i]:
      min = lst[i]
      minIndex = i
  return minIndex

def swap(lst, index1, index2):
  """This function will swap two items in a list and return the new list"""
  val1 = lst[index1]
  val2 = lst[index2]
  # swap index1 with index2
  lst[index1] = val2
  # swap index2 with index1
  lst[index2] = val1
  return lst

# original list
lst = [1,2,5,25,3,6,3,6,7,3,6]

newLst = lst
print("original",lst)
for i in range(len(lst)):
  minIndex = min(newLst[i:len(newLst)])
  newLst = swap(newLst,i,i+minIndex)

print("sorted  ",newLst)
