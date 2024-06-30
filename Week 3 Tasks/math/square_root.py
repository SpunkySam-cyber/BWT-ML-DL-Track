import math  # Import the built-in math module

def square_root(x):
  """Calculates the square root of a number using the built-in math.sqrt function.

  Args:
      x: The number to find the square root of.

  Returns:
      The square root of x.

  Raises:
      ValueError: If the input is negative.
  """
  if x < 0:
    raise ValueError("Square root of negative numbers is not supported.")
  return math.sqrt(x)
