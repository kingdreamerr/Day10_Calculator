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