dividend = int(input("Dividend: "))
divider = int(input("Divider: "))
rest = dividend
quotient = 0
while rest >= divider:
 rest = rest - divider
 quotient = quotient + 1
print("The quotient is", quotient, "and the rest is", rest)
