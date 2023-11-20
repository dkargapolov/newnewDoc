from .calculations import *

__all__ = ['main']

def main():

  '''main function that gives some interface for user

  A function asks user to choose action and operators.
  Then it calls calculate function and prints result.

  
  '''
  
  global __settings

  action = input('Введите действие: ')
  if (action == 'std_dev') or (action == 'medium') or (action == 'variance') or (action == 'median'):
      op1 = []
      op = 1
      while op != "":  # while True
          op = input("Введите операнд: ")
          if op == "":
              break
          else: 
              op = float(op)
              op1.append(op)
      op2 = 0

  elif action == 'precision':
      op1 = float(input('Введите precision(0.001): '))
      op2 = 0
      

  else:
      op1 = float(input('Введите операнд 1: '))
      op2 = float(input('Введите операнд 2: '))

  res = calculate(op1, op2, action)

  print(res)

