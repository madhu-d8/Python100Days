print("welcome to the pizza hub")
size = input("what size of pizza do you want? S, M OR L")
pepperoni = input("do you need pepperoni? Y OR N")
chees = input("do you need cheese? Y OR N")

bill = 100
if size == "S":
    bill+=15
elif size == "M":
    bill+=20
elif size == "L":
    bill+=25
else:
    print("you typed wrong input")
if pepperoni == "Y":
    if size == "S":
        bill+= 2
    else:
        bill+= 3
if chees == "Y":
    bill+= 1
print(f" your final bill is: ${bill}. ")