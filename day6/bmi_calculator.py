# wrtite a programe to calculate BMI and show the BMI
# BMI = WEIGHT / HEIGHT^2
weight =  float(input("please enter your weight(kg) : "))
height =  float(input("please enter your height(mtr) : "))
print(f"you have enter your weight is {weight} kg and your height is {height} m")
BMI = weight/height**2
print(f"your bmi is {BMI}")
if 18.5 <= BMI <= 25:
    print("you are a normal you have to juts maintain budy")
elif BMI > 25 :
    print("oops you are  overweight you have to loose budy")
elif BMI < 18.5 :
    print("  oops you are underweight you have to grow budy ")