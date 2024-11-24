from logger import logging

def add(a,b):
    logging.info(f'Entered values are {a} and {b}')
    logging.debug(f'Addition has started')
    return a+b

sum = add(5,11)
logging.info(f'Sum after function call is {sum}')