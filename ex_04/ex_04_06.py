def computepay(hours, rate):
  print("In computepay", hours, rate)
  if hours > 40:
    reg = hours * rate
    otp = (hours - 40.0) * (rate * 0.5)
    pay = reg + otp
  else:
    pay = hours * rate
  print("Returning",pay)
  return pay
xh = (input("Enter Hours: "))
xr = (input("Enter Rate: "))
xh = float(xh)
xr = float(xr)
xp = computepay(xh, xr)