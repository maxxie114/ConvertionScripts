# file size start at 0, each file increase by two bytes in size, 
# how many files in total can I store in a 1KB area according to this pattern? 
"""
This function will return the number of files in that 1KB can store

a - the initial file size
b - the amount of files that it can store
c - total file size
"""
def recursive(fileSize,i = 0, totalSize = 0):
    if(totalSize > 2**10):
        return i
    else:
        # print("recursion", a,c)
        return recursive(fileSize+2,i+1,totalSize+fileSize)
print("recursion", recursive(0))

# loop
i,totalSize,filesize = 0,0,0
while totalSize < 2**10:
    # print("loop", filesize, totalSize)
    i += 1
    filesize += 2
    totalSize += filesize
print("loop", i+1)

