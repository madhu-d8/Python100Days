import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbols = ['!','@','#','$','%','^','&','*']

print("welcome to the pypassward generator")
ps_letter = int(input("how many letters would you like in your passward?\n"))
ps_symbols = int(input("how many symbols would you like in your passward?\n"))
ps_number = int(input("how many letters would you like in your passward?\n"))

#easy level
# passward = ""
# #pr_number = 4
# for char in range(0, ps_letter):
#     #1-4
#     #random_char(letters)
#     #passward = passward+ramdom_char
#     #passward+= random_char
#     #print(passward)
#
#     random_char = random.choice(letters)
#     print(random_char)
# for char in range(0, ps_symbols):
#     passward += random.choice(symbols)
# for char in range(0 , ps_number):
#     passward += random.choice(numbers)
# print(passward)

passward_list = []
for char in range(0 , ps_letter):
    passward_list.append(random.choice(letters))
for char in range(0, ps_symbols):
    passward_list.append(random.choice(symbols))
for char in range(0 , ps_number):
    passward_list.append(random.choice(numbers))
print(passward_list)
random.shuffle(passward_list)
print(passward_list)

passward = ""
for char in passward_list:
    passward+= char
print(f"your passward is {passward}")
