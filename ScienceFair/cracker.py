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


# Import modules
import time
import random
import hashlib
import logging

# Logging
logging.basicConfig(filename='result.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())

# Functions
def common_password_cracker(start_time, given_password_hash, common_password_1, common_password_2, common_password_3):
    """ 
    This is the first method to crack password

    It loop over three different lists of common password and see if any of them matches the given password

    return a boolean value, and log the plain text password and time used into a log file
    """
    content_lst = [common_password_1,common_password_2,common_password_3]
    for h in range(3):
        content = content_lst[h].read().splitlines()
        #content_lst[h].close()
        for i in content:
            byte_pwd = i.encode('utf-8')
            hashed_pwd = hashlib.sha256(byte_pwd).hexdigest()
            if hashed_pwd == given_password_hash:
                end_time = time.time()
                time_used = count_time_used(start_time, end_time)
                logging.getLogger().info("password: " + given_password_hash + ", plain text result: " + str(i) + 
                    " cracked by common_password_cracker, time used: " + str(time_used) + " seconds")
                return True
        logging.getLogger().debug("Password Hash: " + given_password_hash + " failed, h = " + str(h))
    logging.getLogger().debug("Password Hash: " + given_password_hash + " method 1 failed")
    return False





def number_password_cracker(start_time, given_password_hash):
    """ 
    This function crack password by looping throught number 1000 to 100,000,000,000,000 and compare it with the original password

    log the result and return a boolean value
    """
    least = 1000
    most = 10000000000
    k = ""
    for i in range(5):
        for j in range(int(least), int(most)):
            l = k + str(j)
            byte_pwd = l.encode('utf-8')
            hashed_pwd = hashlib.sha256(byte_pwd).hexdigest()
            if hashed_pwd == given_password_hash:
                end_time = time.time()
                time_used = count_time_used(start_time, end_time)
                logging.getLogger().info("password: " + given_password_hash + ", plain text result: " + str(i) + 
                    " cracked by number_password_cracker, time used: " + str(time_used) + " seconds")
                return True
        least /= 10
        most /= 10
        k += "0"
        logging.getLogger().debug("Password Hash: " + given_password_hash + " failed, i = " + str(i))
    logging.getLogger().debug("Password Hash: " + given_password_hash + " method 2 failed")
    return False

def word_password_cracker(start_time, given_password_hash, word_list):
    """
    This function crack password by looping through a word list

    return boolean
    log result
    """
    content = word_list.read().splitlines()
    for i in content:
        lower_case_pwd = i.lower()
        byte_pwd = lower_case_pwd.encode('utf-8')
        hashed_pwd = hashlib.sha256(byte_pwd).hexdigest()
        if hashed_pwd == given_password_hash:
            end_time = time.time()
            time_used = count_time_used(start_time, end_time)
            logging.getLogger().info("password: " + given_password_hash + ", plain text result: " + str(i) + 
                    " cracked by word_password_cracker, time used: " + str(time_used) + " seconds")
            return True
    logging.getLogger().debug("Password Hash: " + given_password_hash + " method 2 failed")
    return False


def mix_case_password_cracker(start_time,given_password_hash):
    """This method crack password by random generating mixed case password"""

    list_of_chars = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
    password = ""
    found = False
    while(found == False):
        try:
            for _ in range(0, random.randint(4, 11)):
                password += list_of_chars[random.randint(0,51)]
        except IndexError:
            logging.getLogger().exception("Error Occurred")
        byte_pwd = password.encode('utf-8')
        hashed_pwd = hashlib.sha256(byte_pwd).hexdigest()
        if hashed_pwd == given_password_hash:
            end_time = time.time()
            time_used = count_time_used(start_time, end_time)
            logging.getLogger().info("password: " + given_password_hash + ", plain text result: " + str(password) + 
                    " cracked by number_password_cracker, time used: " + str(time_used) + " seconds")
            return True
        else:
            end_time = time.time()
            time_used = count_time_used(start_time, end_time)
            if time_used >= 3600:
                return False

def complex_password_cracker(start_time,given_password_hash):
    """This method crack the password by using random generated password"""
    list_of_chars = "1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM!@#$%^&*()-_=+"
    password = ""
    found = False
    while(found == False):
        try:
            for _ in range(0, random.randint(4, 11)):
                password += list_of_chars[random.randint(0,75)]
        except IndexError:
            logging.getLogger().exception("Error Occurred")
        byte_pwd = password.encode('utf-8')
        hashed_pwd = hashlib.sha256(byte_pwd).hexdigest()
        if hashed_pwd == given_password_hash:
            end_time = time.time()
            time_used = count_time_used(start_time, end_time)
            logging.getLogger().info("password: " + given_password_hash + ", plain text result: " + str(password) + 
                    " cracked by number_password_cracker, time used: " + str(time_used) + " seconds")
            return True
        else:
            end_time = time.time()
            time_used = count_time_used(start_time, end_time)
            if time_used >= 3600:
                return False


def count_time_used(start_time, end_time):
    """ This function will calculate the total amount of time used and return the time in seconds """

    return (end_time - start_time)

def count_hour_used(time_used):
    """ 
    This function will return the total amount of hours used using the imput time_used in seconds
    
    """
    return (time_used/60/60)



# Main
def main():
    """This is the main method"""
    # Declear variables
    password_list = open("passwordList.txt")
    word_list = open("wordList.txt")
    common_password_1 = open("commonPW1.txt")
    common_password_2 = open("commonPW2.txt")
    common_password_3 = open("commonPW3.txt")
    start_time = time.time()
    # Might be useless
    # is_success = false
    password_lst = password_list.read().splitlines()
    password_list.close()
    for i in password_lst:
        # Run method 1
        if common_password_cracker(start_time, i, common_password_1, common_password_2, common_password_3):
            start_time = time.time()
        # Run method 2
        elif number_password_cracker(start_time, i):
            start_time = time.time()
        # Run method 3
        elif word_password_cracker(start_time, i, word_list):
            start_time = time.time()
        # Run method 4
        elif mix_case_password_cracker(start_time,i):
            start_time = time.time()
        # Run method 5
        elif complex_password_cracker(start_time,i):
            start_time = time.time()
        # Log fail
        else:
            logging.getLogger().info("failed to crack password: " + i)
# Run the main method
main()
