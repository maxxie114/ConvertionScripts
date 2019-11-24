def binToDeci(a):
  return str(int(a,2))

def unBias127(biasInt):
  return (int(biasInt) - 127)

def rightOfDeciSeperatorToDeci(a):
  """This function only convert value at the right side of decimal seperator to decimal"""
  deciNum = 0
  for i in range(len(a)):
    deciNum += (int(a[i]))*2**-(i+1)
  return deciNum

def fpBinToDeci(a):
  """This function convert floating point binary number to decimal"""
  # split the string into two parts
  # integer part
  # and fp part
  newBinFpStr = str(newBinFp)
  newBinFpLst = newBinFpStr.split('.')
  # process left side of decimal seperator
  left = binToDeci(newBinFpLst[0])
  # process right side of decimal seperator
  right = rightOfDeciSeperatorToDeci(newBinFpLst[1])
  result = float(left) + right
  return str(result)

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

a = input("please input hex value : ")
if a[0:2] == "0x":
  a = a[2:len(a)]

if len(a) > 8:
  print("Hex should only be 4 byte, 32 bit long")
  exit()
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

# print("decimal: ", str(int(a,16)))
# print("binary: ", finalResult)
signbit = finalResult[0]
exponent = finalResult[1:9]
mantissa = finalResult[9:32]
print("sign bit:", signbit)
print("exponent:", exponent)
print("mantissa:", mantissa)
# calculate unbiased exponent
biasedExp = binToDeci(exponent)
print("biased exponent:", biasedExp)
# check infinite
if int(biasedExp) == 255 and int(binToDeci(mantissa)) == 0:
  if signbit == "1":
    print("-Inf")
  else:
    print("+Inf")
  exit()

# check NaN
if int(biasedExp) == 255 and int(binToDeci(mantissa)) > 0:
  print("NaN")
  exit()

unbiasedExp = unBias127(biasedExp)
print("unbiased exponent:", unbiasedExp)

# determine if the hidden bit is 0 or 1
newMantissa = mantissa

newMantissa = "1." + mantissa

binaryFp = float(newMantissa)
newBinFp = binaryFp * 10 ** unbiasedExp
print("binaryFp:", str(newBinFp))

# process the final result of the convertion
finalFpResult = fpBinToDeci(newBinFp)
# check sign
if signbit == "1":
  finalFpResult = "-" + finalFpResult
print("final convertion result:", finalFpResult)

