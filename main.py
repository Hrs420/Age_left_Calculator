# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
int_age = int(age)
age_months = (90*12)-int(int_age*12)
age_weeks = (90*52)-int(int_age*52)
age_days = (90*365)-int(int_age*365)

print(f"You have {age_days} days, {age_weeks} weeks, and {age_months} months left.")



