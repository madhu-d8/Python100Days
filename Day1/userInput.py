
input("what is your name?")

print("Hello" + input("what is your name?"))

print("Hello " + input("what is your name?"))

# practise questions

print("Madhu Mitha")

a= input('enter your first name')
b= input('enter your second name')
print(a+b)

first_name = input("First name: ")
last_name = input("Last name: ")

full_name = first_name + " " + last_name

print(full_name)

a="python"
b="is"
c="fun"
print(a,b,c)

w1="python"
w2="is"
w3='fun'

sentence= w1+ " " + w2 + " " + w3
print(sentence)


color = input("enter your favourite color: ")
print("your favorite color is: " + color)

name = input('enter your name: ')
city = input('enter your city: ')
print("Hello " + name + " " + city)


name = input('enter your name: ')
city = input('enter your city: ')
print("Hello " + name + " from " + city)

string="python"
print(string[0])

text = input('enter a string')
print(text[0])

text = input('enter a string')
print(text[-1])

text = input('enter a string')
middle_index=len(text)//2
print(text[middle_index])



string=input("enter a string: ")
index=int(input("enter index: "))
print(string[index])



text = input('enter a string')
print(text[0:3])

text = input('enter a string')
print(text[-4:])

text = input('enter a string')
print(text[::2])

text = input("Enter a string: ")

reverse_text = text[::-1]

print(reverse_text)

text = input('enter a string')
print(text.upper())
text = input('enter a string')
print(text.lower())

name= "madhu"
print(name)

print(len(input("what is your name")))

name=input("Enter your name: ")
length =len(name)
print(length)

Name=input("Enter your name: ")
string=Name.count('a')
print(string)

text=input("enter text")
new_text=text.replace("python","java")
print(new_text)

char=input("enter a character")
print(char.startswith("p"))

firstname = input("Enter your first name: ")
middlename = input("Enter your middle name: ")
lastname = input("Enter your last name: ")
fullname = firstname+ " " + middlename + " " + lastname
print(fullname)

name="madhu"
domin="gmail.com"
output=name+"@" +domin
print(output)

print("hi" *5)

name="madhu"
course='python'
sen=name + " " + "is" + " " + "learning" + " "+ course
print(sen)

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

name="madhu"
age=25
print(name)
print(age)

a=10
b=20
sum=a+b
print(sum)

x=10
y=5.5
z="python"
print(type(x))
print(type(y))
print(type(z))

a,b,c=1,2,3
print(a)
print(b)
print(c)

length=10
breadth=5
area=length*breadth
print(area)

p=100
t=2
r=5
z=p*t*r/100
print(z)

celsius=25
F=9/5*celsius+32
print(F)

X=10
X=X+5
X=X*2
print(X)

name=input("Enter your name: ")
age=int(input("Enter your age: "))

print("my name is " , name, "and I am" ,age, "years old")


x = 100

def show():
    print(x)

show()

x = 10

def change():
    global x
    x = 50

change()
print(x)

def demo():
    a = 25
    print(a)

demo()

a = 10
b = 25
c = 15
print(max(a,b,c))


a = 20
b = 5
x= 20
y= 5
z=x+y
print(z)

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b

print("Addition =", addition)
print("Subtraction =", subtraction)
print("Multiplication =", multiplication)
print("Division =", division)


glass1="milk"
glass2="juice"
empty=glass1
glass1=glass2
glass2=empty
print(glass1)
print(glass2)

g1="milk"
g2="juice"
g1,g2=g2,g1
print(g1)
print(g2)