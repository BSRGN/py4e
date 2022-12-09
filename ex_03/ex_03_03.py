try:
	grade = None
	score = float(input("Enter Score 0-1.0:"))
	if score < 0 or score < 1.0:
		print("Error: input must be between 0.0 - 1.0.")
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
	
except:
	print("Error: Please enter numerical number 0.0 - 1.0.")