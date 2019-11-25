import unittest
import hashlib
import time
import logging
import random

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
    most = 1000000000
    k = ""
    for i in range(5):
        for j in range(int(least), int(most)):
            l = k + str(j)
            byte_pwd = l.encode('utf-8')
            hashed_pwd = hashlib.sha256(byte_pwd).hexdigest()
            if j == 11983805:
                logging.getLogger().warning(j)
                logging.getLogger().warning(l)
                
                if hashed_pwd == given_password_hash:
                    end_time = time.time()
                    time_used = count_time_used(start_time, end_time)
                    logging.getLogger().info("password: " + given_password_hash + ", plain text result: " + str(i) + 
                    " cracked by number_password_cracker, time used: " + str(time_used) + " seconds")
                    return True
                break
            # logging.getLogger().warning(given_password_hash)
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
            if time_used >= 5:
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
            if time_used >= 5:
                return False


def count_time_used(start_time, end_time):
    """ This function will calculate the total amount of time used and return the time in seconds """

    return (end_time - start_time)

def count_hour_used(time_used):
    """ 
    This function will return the total amount of hours used using the imput time_used in seconds
    
    """
    return (time_used/60/60)


# Declear variables
password_list = open("passwordList.txt")
word_list = open("wordList.txt")
common_password_1 = open("commonPW1.txt")
common_password_2 = open("commonPW2.txt")
common_password_3 = open("commonPW3.txt")
start_time = time.time()
given_password_hash = "0603a9b952484f527e6dec6fd4ed1cf8c857b5f24c766fa641ab8018bf1d6712"


class MyTest(unittest.TestCase):
    def testNPC(self):
        self.assertTrue(number_password_cracker(start_time, given_password_hash))
    
    def testCPC(self):
        self.assertTrue(common_password_cracker(start_time, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
             common_password_1, common_password_2, common_password_3))

    def testWPC(self):
        self.assertTrue(word_password_cracker(start_time, "28bd9ba6c25f00d4f8dad0419540a3abbf189e818b414b503adae8a1f92eff82", word_list))

    def testMPC(self):
        self.assertFalse(mix_case_password_cracker(start_time,"7eb4c29da3d535e0689da32643c3487ed35d5dc2083377586db13a5009bc48ce"))

    def testCMPC(self):
        self.assertFalse(complex_password_cracker(start_time,"359a28e7c2c4f8313ce52d981947b69181a71c626c2e040cc1d91a8dcf13cfc9"))

if __name__ == '__main__':
    unittest.main()
# number_password_cracker(start_time, given_password_hash)

