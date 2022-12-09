def computegrade(score):
    print("In computegrade", score)
    grade = "F"
    if score < 0 or score > 1.0:
      print("Bad score")
    elif score >= 0.9:
      grade = "A"
    elif score >= 0.8:
      grade = "B"
    elif score >= 0.7:
      grade = "C"
    elif score >= 0.6:
      grade = "D"
    elif score < 0.6:
      grade = "F"
    print(grade)
    return(grade)
try:
  score = (input("Enter Score 0-1.0:"))
  score = float(score)
  final_grade = computegrade(score)
except:
  print("Please enter a number between 0-1.0.")

