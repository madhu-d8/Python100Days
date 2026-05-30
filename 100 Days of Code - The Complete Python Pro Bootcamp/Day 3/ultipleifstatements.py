#if/elif/else

# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do c

# multiple if
#
# if condition1:
#     do A
# if condition2:
#     do B
# if condition3:
#     do c

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height >=120:
    print("you can ride rollercoster")
    age = int(input("What is your age? "))
    if age <=12:
        bill = 5
        print("child tickets are $5.")
    elif age >18:
        bill = 7
        print("youth are $7.")
    else:
        bill = 12
        print("adult tickets are $12")
    want_photos = input("do you want to have a photo? type Y for yes and N for no")
    if want_photos == "Y":
        bill += 3
    print(f"your final bill is:  {bill}")
else:
    print("rou acnnot ride")