# ======== Calculator =========
#ADD
def add(n1, n2):
  return n1 + n2

#SUBTRACT
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2


operations = {}    # dictionary for operators and corresponding functions
operations["+"] = add
operations["-"] = subtract
operations["*"] = multiply
operations["/"] = divide

def calculator():
  num1 = float(input("whats the first number?: "))
  for key in operations:  # for printing all operators
    print(key)
  
  continue_calc = 'y'
  while continue_calc == 'y':
    operation_symbol = input("Pick an operation: ")   
    num2 = float(input("whats the next number?: "))
    function = operations[operation_symbol]  #fetching desired function from dictionary
  
    answer = function(num1, num2)    #function call
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    if (input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")) == "y":
      num1 = answer
    else:
      continue_calc = "n"
      calculator()

calculator()