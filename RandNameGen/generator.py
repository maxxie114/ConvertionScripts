# Copyright 2019 Max Xie

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial 
# portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT 
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# This program will resequence the list of name randomly, to get a sequence of random names

import random
import time

def getNoneRepeatedName(name_list, used_name):
    """ This function return a random name from a list of names"""
    list_length = len(name_list)
    while 1:
        name = name_list[random.randint(0,list_length-1)]
        if not name in used_name:
            return name
        


filename = open("nameList.txt")
name_list = filename.read().splitlines()
used_name = []

for i in range(len(name_list)):
    name = getNoneRepeatedName(name_list, used_name)
    used_name.append(name)
    print(str(i+1) + " " + name)
    time.sleep(1)
