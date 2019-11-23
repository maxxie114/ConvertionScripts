a = input("input a binary number(4 digit max): ")
dlst = list(a)
result = int(a[0]) * 8 + int(a[1]) * 4 + int(a[2]) * 2 + int(a[3]) * 1
hexlst = ["NA","A","B","C","D","E","F"]
if result > 9:
  result = hexlst[result-9]
print("hex: " + str(result))
