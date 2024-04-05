def intToDecimal(amount, decimals):
  """Converts an integer amount of a currency to a decimal string.

  Args:
    amount: The amount in the smallest denomination of the currency.
    decimals: The number of decimal places to include in the result.

  Returns:
    A string representing the amount in decimal format.
  """

  if decimals < 0:
    raise ValueError("decimals must be non-negative")

  factor = 10 ** decimals
  return "{}.{:0>{decimals}}".format(amount // factor, amount % factor, decimals=decimals)
