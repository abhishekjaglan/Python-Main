import logging
from venv import logger

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log'), # file operations handler
        logging.StreamHandler() ## stream of logs to file handler
    ]
)

logger = logging.getLogger('ArithmeticApp')
#logger.setLevel(logging.DEBUG)

def add(a,b):
    result = a+b
    logger.debug(f'Adding {a}+{b}: {result}')
    return result

def subtract(a,b):
    result = a-b
    logger.debug(f'Subtracting {a}-{b}: {result}')
    return result

def multiply(a,b):
    result = a*b
    logger.debug(f'Multiplying {a}*{b}: {result}')
    return result

def divide(a,b):
    try:    
        result = a/b
        logger.debug(f'Dividing {a}/{b}: {result}')
        return result
    except ZeroDivisionError as ze:
        logger.error(f'Division by zero error: {ze}')
        return None

add(5,9)
subtract(987,324)
multiply(234,64)
divide(45,15)
divide(234,0)