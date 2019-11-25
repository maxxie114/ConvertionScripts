import math
a, sizeLst, size = input(), ["","B","KB","MB","GB"], [2**(10*i) for i in range(4)]
for i in range(4):
     if float(a) < size[i]:
         print(str(math.floor(float(a)/size[i-1])) + " " + sizeLst[i])
         exit()
print(str(math.floor(float(a)/size[3])) + " " + sizeLst[4])
