
__all__ = ['convert_precision', 'std_dev', 'medium', 'variance', 'median', 'calculate']

import math
import statistics

__settings = {'precision': 0.00000001}



def convert_precision(precision='0.001'):

    '''shows a number of digits after point

    A function that return a number of digits after point. 
    Usually using for 'round()' function to make a result
    more comfortable for user.

    Args:
      precision (float): scientific error value

    Return:
      n (int): number of digits after point
    
    '''
  
    precision = float(precision)
    n = 0
    while precision < 1:
      n += 1
      precision *= 10
    return n


def std_dev(op1):

  '''counts the standard deviation of a list of numbers

  A function that takes a list of numbers and counts 
  the standard deviation. 

  Args:
    op1 (list): list of numbers

  Return:
    result (float): standard deviation of a list of numbers

  '''
  
  result = 0
  average = 0
  for i in range(0, len(op1)):
    average += op1[i]
  average = average / (len(op1))
  for i in range(0, len(op1)):
    result += (op1[i] - average)**2
  result /= (len(op1))
  result = math.sqrt(result)
  return result

def medium(op1):

  '''counts the simple medium.

  A function takes a list of numbers and divide sum of these numbers on their amount. 

  Args:
    op1 (list): list of numbers

  Return:
    result (float): standard medium

  '''
  
  return sum(op1)/len(op1)

def variance(op1):

  '''function that counts variance

  A function takes a list of numbers and does some
  calculations for variance.

  Args:
    op1 (list): list of numbers

  Return:
    result (float): standard variance

  '''
  
  mid = medium(op1)
  var_res = sum((xi - mid) ** 2 for xi in op1) / len(op1)

  return var_res

def median(op1):

  '''counts the median.

  A function use statistics library to make a calculations for median.

  Args:
    op1 (list): list of numbers

  Return:
    result (float): standard median

  '''
  
  return statistics.median(op1)

def calculate(op1, op2, action):

  '''multi-functions that have a lot of options to count something.

  A function takes two operators and one action and counts something.

  Args:
    op1 (int, float): the first operator.
    op2 (int, float): the second operator.
    action (str): some word or char that define action.

  Return:
    result (float): result of logic decision and calculations.

  '''
  
  global __settings

  if action == '+':
      result = op1 + op2
  elif action == '-':
      result = op1 - op2
  elif action == '*':
      result = op1 * op2
  elif action == '/':
      result = op1 / op2
  elif action == '**':
      result = op1 ** op2
  elif action == '%':
      result = op1 % op2
  elif action == 'std_dev':
      result = std_dev(op1)
  elif action == 'precision':
      result = convert_precision(op1)
  elif action == 'medium':
      result = medium(op1)
  elif action == 'variance':
      result = variance(op1)
  elif action == 'median':
      result = median(op1)

  return round(result, convert_precision(__settings.get('precision')))

