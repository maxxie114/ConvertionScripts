number = int(input("please enter a number: "))
r = 1
ans = 1
result = []
ans = number
while int(ans) > 0:
  r = ans % 2
  ans = ans / 2
  # print("r: " , int(r))
  # print("q: ", int(ans))
  result.insert(0,int(r))
res = ''.join([str(i) for i in result])
print(res)
