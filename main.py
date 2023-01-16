def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

def ops():
  for operation in operations:
    print(operation)

operations = {
  "+": add,
  "-":subtract,
  "*": multiply,
  "/":divide
}

def calculate():
  continue_claculating = False
  num1 = float(input("What's the first number?: "))
  
  while not continue_claculating:
    ops()
    op = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))

    answer = operations[op](num1,num2)
    print(f"{num1} {op} {num2} = {answer}")

    yes = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start .: ")
    if yes == 'y':
     num1 = answer
    else:
      continue_claculating = True
      calculate()

calculate()