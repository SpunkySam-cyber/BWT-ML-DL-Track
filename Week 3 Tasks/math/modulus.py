def modulus(x, y):
  """Calculates the modulus (remainder) of dividing x by y.

  Args:
      x: The dividend.
      y: The divisor.

  Returns:
      The remainder of x divided by y.

  Raises:
      ZeroDivisionError: If the divisor (y) is zero.
  """
  if y == 0:
    raise ZeroDivisionError("Division by zero is not allowed.")
  return x % y
