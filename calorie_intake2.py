m_cal = input("Enter Michael's daily calorie intake (typically 2600 calories): ")
m_cal = float(m_cal)
l_cal = input("Enter Lisset's daily calorie intake (typically 2000 calories): ")
l_cal = float(l_cal)
c_cal = input("Enter Caleb's daily calorie intake (typically 2000 calories): ")
c_cal = float(c_cal)
a_cal = input("Enter Aidan's daily calorie intake (typically 2000 calories): ")
a_cal = float(a_cal)
tot_days = input("Enter Days for expected family calorie intake: ")
tot_days = float(tot_days)
tot_cal = m_cal + l_cal + c_cal + a_cal
fam_cal = float(tot_cal * tot_days)
print(f"Total calories required for {tot_days} day(s): ",fam_cal)
em_food = input("Enter calories per emergency food kit: ")
em_food = float(em_food)
em_food_kit = fam_cal/em_food
print(f"{em_food_kit} emergency food kit(s) required to supplement {fam_cal} calories for {tot_days} days.")