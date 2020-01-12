# This cipher method work by adding the integer of the two number
# together and then convert the new number back into string using ascii

# these are test message and key
# testMsg = "hello this is max"
# key = "thisisthekey"

# since some keys doesn't work, the system will generate keys that work
import base64

def strToInt(text):
  """
  This function convert a string to an integer by combining every
  integer unicode value of each item together, with the number of
  digits and a padding of 0 in front so that the decoder know how
  to decode the number back to string

  format: <length> + <padding of 0> + <integer value>
  the result will always be a number with length 8

  text - the text to input
  """
  result = ""
  for i in text:
    # determine the length of the integer value
    length = len(str(ord(i)))
    totalLen = len(str(length) + str(ord(i)))
    paddingLen = 0
    if totalLen < 8:
      paddingLen = 8-totalLen
    result += str(length) + '0'*paddingLen + str(ord(i))
  return int(result)

def intToStr(num):
  """
  This function work by first converting the entire number into string data type
  and then cut the string into 8 characters each
  and then it use the length value to cut out the last n digit of the number
  finally evaluate that number using chr()

  num - the number to be converted
  """
  strNum = str(num)
  numLst = []
  index = 0
  result = ""
  # split string into sets of 8
  for i in range(int(len(strNum)/8)):
    numLst.append(strNum[index:index+8])
    index += 8

  # convert the 8 digit number to string
  for i in numLst:
    len_of_val = int(i[0])*-1
    uni_val = i[len_of_val:]
    result += chr(int(uni_val))

  return result

def encrypt(text,key):
  """
  This function encode the text by adding two integer, and return an encrypted string that is achieved using outputStr 
  function

  if the integer length of the key is too short compare to the message, then it will be extended to len(message)-1 using a
  padding of the first character of the key

  text - the text to be encrypted
  key - the key to encrypt and decrypt the message
  """
  keyStr = key[0]
  while len(key) < len(text)-1:
    key += keyStr
    # print(f"{len(key) < len(text)-1}, {key}") # debug
  intText = strToInt(text)
  intKey = strToInt(key)
  encrypted = intText + intKey
  # print(f"debug: {len(text)}, {len(key)}") # debug
  result = intToStr(encrypted)
  base64byte = base64.standard_b64encode(result.encode(encoding='utf-8'))
  return base64byte.decode('ascii')

def decrypt(base64text, key):
  """
  This function decode a text by first calling outputInt to convert a string back into int, and then divide the text int by the key
  int

  base64text - the text to be decrypted
  key - the key to encrypt and decrypt the message
  """

  # first decrypt the base64
  text = base64.standard_b64decode(base64text)
  text = text.decode(encoding='utf-8')
  keyStr = key[0]
  while len(key) < len(text)-1:
    key += keyStr
    # print(f"{len(key) < len(text)-1}, {key}") # debug
  intText = strToInt(text)
  intKey = strToInt(key)
  # print(f"debug: {len(text)}, {len(key)}") # debug
  decrypted = intText - intKey
  # print(decrypted)
  return intToStr(int(decrypted))

def isascii(text):
  return all(ord(char) < 128 for char in text)

def main():
  # these are test message and key
  mode = input("1 for encrypt, 2 for decrypt:")
  msg = input("please input message:")
  key = input("please input the key\nkey should only contains lowercase english letters\nexcept a,b,c and the key should not contains space:")
  # prevent key from exceed the length of the message
  if len(key) > len(msg)-1:
    print("key length must be at most 1 less than the length of the actual message")
    exit(0)
  # prevent keys with special characters, [a,b,c], or uppercase letter
  errorMsg = "key should only contains lowercase english letters, but it should not include a,b,c, and the key should not contains space"
  # check not special characters (first check ascii, then check alpha)
  # this prevent Chinese characters being recognized as alphabet
  if key.isascii():
    if key.isalpha():
      # check not [a,b,c]
      if not 'a' in key and not 'b' in key and not 'c' in key:
        print(key[0])
        # check not uppercase
        if not key.isupper():
          if mode == "1":
            encrypted = encrypt(msg,key)
            print(f"encrypted: {encrypted}")
            exit(0)
          elif mode == "2":
            decrypted = decrypt(msg,key)
            print(f"decrypted: {decrypted}")
            exit(0)
          else:
            print("invalid mode")
            exit(0)
  print(errorMsg)

def testKey():
  # test key result
  # no special characters, no numbers, no uppercase, no space, no a,b,c, anything else all good
  import random
  msg = "hello this is a test"
  choices = "defghijklmnopqrstuvwxyz"
  keyStr = []
  for i in range(100):
    randStr = ""
    for i in range(len(msg)-1):
      randStr += choices[random.randint(0,len(choices)-1)]
    keyStr.append(randStr)
  # random generate 100 three character key string
  for key in keyStr:
    encrypted = encrypt(msg,key)
    decrypted = decrypt(encrypted,key)
    print(f"{key}, {decrypted == msg}, {decrypted}")

if __name__ == '__main__':
  main()
  # testKey()
