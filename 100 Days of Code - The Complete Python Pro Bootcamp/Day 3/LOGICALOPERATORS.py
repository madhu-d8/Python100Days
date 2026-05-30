print("welcome to rollocoster")
height = int(input("what is your height? "))
bill = 0

if height >=120:
    print("you can ride rollcoster")
    age = int(input("what is your age? "))
    if age <12:
        bill = 5
        print("child tickets are $5.")
    elif age <=18:
        bill = 7
        print("youth tickets are $7.")
    else:
        bill = 12
        print("adult tickets are $12.")

    wants_photo = input("do you want a photo? Y or N. ")
    if wants_photo == "Y":
        bill+=3
    print(f"your final bill is ${bill}")
else:
    print("you cannot ride")