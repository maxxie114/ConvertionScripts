# Copyright Max Xie 2019
# This is a demo of the logging API
# You can find more info here: https://docs.python.org/3/library/logging.html
import logging

# Logging
logging.basicConfig(filename='result.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())

logging.getLogger().info("Hello world 1")
logging.getLogger().info("Hello world 2")
logging.getLogger().debug("Hello world 3")

lst = [1,2,3,4,5,6]
try:
    print(lst[6])
except:
    logging.getLogger().exception("Exception occurred:")



