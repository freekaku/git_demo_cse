a = 10
b = 5

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
  if y == 0:
    return "Cannot divide by 0"
  return x / y

if __name__ == "__main__":
  print("Calculator App")
  print(f"Addition of {a} and {b} = {add(a, b)}")
  print(f"Subtraction of {a} and {b} = {sub(a, b)}")
  print(f"Multiplication of {a} and {b} = {mul(a, b)}")
  print(f"Division of {a} and {b} = {div(a, b)}")
