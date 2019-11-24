import sys

a = sys.argv[1]
b = sys.argv[2]

if not (len(a) == len(b)):
  print("two binary numbers must have the same length")
  exit()

c = ""
result = ""
for i in range(len(a)):
  c = int(a[i]) or int(b[i])
  result += str(c)

print("firstNumber:", a)
print("secondNumber", b)
print("finalResult:", result)
