mode = input("select mode: \n a: encrypt \n b: decrypt\n")
if mode == "a":
  modekey = "encrypt"
elif mode == "b":
  modekey = "decrypt"
else:
  print("invalid mode")
  exit(0)
in_a = input(f"input string to {modekey}:")
in_b = input("input encrypt char key:")
result = ""
for i in in_a:
  result += chr(ord(i) ^ ord(in_b))
print("encrypted string:", result)
