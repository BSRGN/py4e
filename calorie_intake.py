m_cal = 2600
l_cal = 2000
c_cal = 2000
a_cal = 2000
fam_cal = m_cal + l_cal + c_cal + a_cal
tot_cal = input("Enter Days for expected family calorie intake: ")
tot_cal = float(tot_cal)
print(f"Total calories required for {tot_cal} day(s): ",fam_cal * tot_cal)
