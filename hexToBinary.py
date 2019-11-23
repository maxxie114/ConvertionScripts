def convertToBinary(num):
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
  # make sure it is 4 bit
  zero = ""
  if len(res) < 4:
    for i in range(4-len(res)):
      zero += "0"
  return zero + res

while 1:
  a = input("please input hex value (do not include 0x): ")
  hexVal = {
    "A":10,
    "B":11,
    "C":12,
    "D":13,
    "E":14,
    "F":15
  }
  finalResult = ''
  for i in range(len(a)):
    num = 0
    if a[i].isnumeric():
      num = int(a[i])
    else:
      num = hexVal[a[i]]
    finalResult += str(convertToBinary(num))

  print("decimal: ", str(int(a,16)))
  print("binary: ", finalResult)
