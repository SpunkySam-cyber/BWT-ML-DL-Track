from math.addition import my_add
from math.subtract import subtract
from math.divide import divide
from math.modulus import modulus
from math.square_root import square_root
from math.multiply import multiply

# Basic arithmetic operations
result = my_add(5, 3)
print(f"Addition: {result}")

result = subtract(10, 2)
print(f"Subtraction: {result}")

result = multiply(4, 6)
print(f"Multiplication: {result}")

try:
  result = divide(12, 0)  # Simulate division by zero error
except ZeroDivisionError as e:
  print(f"Division Error: {e}")

result = modulus(17, 5)
print(f"Modulus: {result}")

# Advanced operation with error handling
try:
  result = square_root(-9)  # Simulate negative input error
except ValueError as e:
  print(f"Square Root Error: {e}")
else:
  print(f"Square Root: {result}")
