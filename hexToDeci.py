a = input("Please input a hex sequence: ")
sequenceLst = list(a)
hexLst = {
 "0":0,
 "1":1,
 "2":2,
 "3":3,
 "4":4,
 "5":5,
 "6":6,
 "7":7,
 "8":8,
 "9":9,
 "A":10,
 "B":11,
 "C":12,
 "D":13,
 "E":14,
 "F":15
}
result = 0
for i in range(len(sequenceLst)):
  result += hexLst[sequenceLst[i]] * (16 ** (len(sequenceLst)-i-1))
  # print("debug: " + str(len(sequenceLst)-i-1))
print("result: " + str(result))
