# Add a layer of base64 encryption on top so that the encryption
# result will all be readable characters
import base64
mode = input("select mode: \n a: encrypt \n b: decrypt\n")
if mode == "a":
  modekey = "encrypt"
elif mode == "b":
  modekey = "decrypt"
else:
  print("invalid mode")
  exit(0)
in_a = input(f"input string to {modekey}:")
if modekey == "decrypt":
  in_a = base64.standard_b64decode(in_a).decode('utf-8')
in_b = input("input encrypt char key:")
result = ""
for i in in_a:
  result += chr(ord(i) ^ ord(in_b))
if modekey == "encrypt":
  result = base64.standard_b64encode(result.encode('utf-8'))
print(f"{modekey}ed string: {result}")
