def division(x,y)
  """
  This code asks the user for a Dividend and a Divider, returning the quotient and solution's rest
  Requires:Two int numbers y>0
  Ensures: The quotient and the rest of the division
  """
  dividend = int(input("Dividend: "))
  divider = int(input("Divider: "))
  rest = dividend % divider
  quotient = dividend//divider
  while rest >= divider:
    rest = rest - divider
    quotient = quotient + 1
    print("The quotient is", quotient, "and the rest is", rest)
  return quotient
  return rest
