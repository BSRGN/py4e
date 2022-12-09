# Hours Worked * Hourly Rate = Total Pay
try:
  xh = float(input("Enter Hours: "))
  xr = float(input("Enter Rate: "))
  if xh <= 40:
    xp = xh * xr
    print("Pay:", xp)
  elif xh > 40:
    ot = xh - 40
    xp = (40 * xr) + (ot * xr) * 1.5 #made a mistake here by entering xh instead of 40.
    print("Regular Pay:", xh * xr)
    print("Overtime Pay:", (ot * xr) * 1.5)
    print("Total Pay:", xp)
except:
  print("Please enter a number")