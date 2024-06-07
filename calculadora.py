from replit import clear

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
  num1 = int(input("What is the first number? "))
  num2 = int(input("What is the second number? "))
  for symbol in operations:
    print(symbol)

  operation_symbol = input("Pick an operation from the line above: ")
  calculation_function = operations[operation_symbol]
  answer = calculation_function(num1, num2)  
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  should_continue = True

  while should_continue:
      operation_symbol = input("Pick another operation: ")
      num3 = int(input("What is the next number? "))
      calculation_function = operations[operation_symbol]
      second_answer = calculation_function(answer, num3)
      print(f"{answer} {operation_symbol} {num3} = {second_answer}")
      if input("Deseja continuar digite 'y'. Deseja novo calculo digite 'n': ") == "y":
        answer = second_answer  
      else:
        should_continue = False
        clear()
        calculator()
          
calculator()
    
    
    