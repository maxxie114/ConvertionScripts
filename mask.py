# This program will convert both IP address and mask to binary and then get the network address
def deciToBinary(num):
  r = 1
  ans = 1
  result = []
  ans = num
  while int(ans) > 0:
    r = ans % 2
    ans = ans / 2
    # print(int(r))
    result.insert(0,int(r))
  res = ''.join([str(i) for i in result])
  return res

ip = input("Please enter IP")
mask = input("Please enter mask")

ipLst = ip.split(".")
maskLst = mask.split(".")

# converting IP to binary
ipInBinary = []
for i in ipLst:
  ipInBinary.append(deciToBinary(i))

# converting mask to binary
maskInBinary = []
for i in maskLst:
  maskInBinary.append(deciToBinary(i))


