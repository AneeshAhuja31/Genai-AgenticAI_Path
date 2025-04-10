from logger import logging

def add(a,b):
    logging.debug("The addition operation is taking place")
    return a+b

logging.debug("The logging function in called")
add(1,2)