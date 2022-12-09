#converting Celcius to Fahrenheit
inp_c_temp = input("Enter Celsius temperature:")
try:
  celc = float(inp_c_temp)
  f_temp_formula = (celc * 9/5 + 32)
  print(inp_c_temp, "degrees Celsius converts to",f_temp_formula,"degrees Fahrenheit.")
except:
  print("Please enter a number")