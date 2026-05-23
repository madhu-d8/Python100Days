# if condition:
#     if another condition:
#         do this
#     else:
#         do thid
# else:
#     do this

#
# print("welcome to rollercoster")
# height = int(input("enter your height in cm: "))
#
# if height >= 120:
#     print("you can ride")
#     age = int(input("enter your age: "))
#     if age <= 12:
#         print("please pay $5")
#     elif age <=18:
#         print("please pay $10")
#     else:
#         print("please pay $15")
# else:
#     print("you cannot ride")


print("BMI Calculator")
bmi = float(input("enter your bmi: "))
if bmi <18.5:
    print("underweight")
elif bmi >18.5 and bmi <25:
    print("normal")
else:
    print("overweight")

    weight = 85
    height = 1.85

    bmi = weight / (height ** 2)

    # 🚨 Do not modify the values above
    # Write your code below 👇
    if bmi < 18.5:
        print("underweight")
    elif bmi >= 18.5 and bmi < 25:
        print("normal weight")
    else:
        print("overweight")