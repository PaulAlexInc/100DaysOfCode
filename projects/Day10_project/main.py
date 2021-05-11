#Calculator
from art import logo

def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2

operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
def calculator():
  print(logo)
  num1 = float(input("What is the first number?: "))
  for op in operations:
    print(op)
  calc_continue=True
  while calc_continue:
    operation_choice=input("Pick an operation:\n ")
    num2 = float(input("What is the next number?: "))
    operation_func=operations[operation_choice]
    answer=operation_func(num1,num2)

    print(f"{num1} {operation_choice} {num2} = {answer}")
    choice=input(f"Type 'y' to continue calculating with {answer}, or type 'n' start a new calculation.: ").lower()

    if choice=='y':
      num1=answer
    else:
      calc_continue=False
      calculator()#To start the calculator from the beginning. For a recursive function to call itself, make sure there is some condition, to prevent infinite loops

calculator()#we need to call the function first for it to start the calculator

