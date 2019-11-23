number = int(input("please enter a number: "))
base = int(input("please enter the base (2-16): "))
r = 1
ans = 1
result = []
ans = number
while int(ans) > 0:
  r = ans % base
  ans = ans / base
  # print(int(r))
  result.insert(0,int(r))
res = ''.join([str(i) for i in result])
print(res)
