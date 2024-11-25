{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-25 09:15:53 - ArithmeticApp - DEBUG - Adding 5+9: 14\n",
      "2024-11-25 09:15:53 - ArithmeticApp - DEBUG - Subtracting 987-324: 663\n",
      "2024-11-25 09:15:53 - ArithmeticApp - DEBUG - Multiplying 234*64: 14976\n",
      "2024-11-25 09:15:53 - ArithmeticApp - DEBUG - Dividing 45/15: 3.0\n",
      "2024-11-25 09:15:53 - ArithmeticApp - ERROR - Division by zero error: division by zero\n"
     ]
    }
   ],
   "source": [
    "from ast import Sub\n",
    "import logging\n",
    "from unittest import result\n",
    "from venv import logger\n",
    "from xml.sax import handler\n",
    "\n",
    "logging.basicConfig(\n",
    "    level=logging.DEBUG,\n",
    "    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',\n",
    "    datefmt='%Y-%m-%d %H:%M:%S',\n",
    "    handlers=[\n",
    "        logging.FileHandler('app.log'), # file operations handler\n",
    "        logging.StreamHandler() ## stream of logs to file handler\n",
    "    ]\n",
    ")\n",
    "\n",
    "logger = logging.getLogger('ArithmeticApp')\n",
    "logger.setLevel(logging.DEBUG)\n",
    "\n",
    "def add(a,b):\n",
    "    result = a+b\n",
    "    logger.debug(f'Adding {a}+{b}: {result}')\n",
    "    return result\n",
    "\n",
    "def subtract(a,b):\n",
    "    result = a-b\n",
    "    logger.debug(f'Subtracting {a}-{b}: {result}')\n",
    "    return result\n",
    "\n",
    "def multiply(a,b):\n",
    "    result = a*b\n",
    "    logger.debug(f'Multiplying {a}*{b}: {result}')\n",
    "    return result\n",
    "\n",
    "def divide(a,b):\n",
    "    try:    \n",
    "        result = a/b\n",
    "        logger.debug(f'Dividing {a}/{b}: {result}')\n",
    "        return result\n",
    "    except ZeroDivisionError as ze:\n",
    "        logger.error(f'Division by zero error: {ze}')\n",
    "        return None\n",
    "\n",
    "add(5,9)\n",
    "subtract(987,324)\n",
    "multiply(234,64)\n",
    "divide(45,15)\n",
    "divide(234,0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "python-main-venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
