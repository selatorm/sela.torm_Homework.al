# Q1: Convert this tree to Python.
x=0
y=0
z=0
if x==5:
    if y<6:
        if z<=11:
            print("northing")
        else:
            print(2)
    else:
        print(1)
else:
    if y>3:
        print(3)
    else:
        print("northing")
# Q2: Converts this tree to Python.
x=0
y=0
if x>4:
    if x<2:
        print(1)
    else:
        print("northing")
else:
    if y>3:
        print(2)
    else:
        print("northing")
#  Create variable name “nbRepeat” and set the values to 5.
#  Print « Hello World » following variable « nbRepeate » times.
# Q1: What will be the output?
Repeat_number=5
for i in range(Repeat_number):
    print("Hello world")
#  Input a number in the console.
#  As long as when the number still greater than 5, print it.
#  Decrement the number of -2.
# Q1: What will be the result for these outputs?
n=13
while n>5:
    print(n)
    n-=2
# Q4: To find the bug, test this code and check if the output is correct.
number = int(input())
while number != 5:
    print(number)
    number = number - 2
# Input a username (string) and its age (integer) in the console.
#  You shall write the value of those 2 variables with some text, as show on the result.
Name="Ronan"
age=28
print("my nam is",Name,"i am ",age,"years old")
# Get the number entered from keyboard and store it into a variable userMessage
#  If the userMessage is lower than 0, display “Negative Number!”
#  Else display “Positive Number”
number=10
if number>0:
    print("positive")
else:
    print("negative")
# Example: To see &quot;Dog&quot; number must be in the range: ] –infinity, 25[
number = 31
if number < 25 :
    print("Dog")
elif number <= 30 :
    print("Cat")
else :
    print("Cow")
#  Q1: What will be print if value equal to 10?
value=10
if value >= 5:
    print("Apple")
elif value <= 10:
    print("Banana")

value=10
if value > 10:
    print("Red")
if value <= 10:
    print("Blue")

# Function to print length of text times of the character "X"
def print_x_based_on_length(text):
    length = len(text)
    print("X" * length)
text = input("Enter a string: ")
print_x_based_on_length(text)

# Function to evaluate the conditions and print the appropriate message

while True:
    word = input("Enter a word: ")
    n = int(input("Enter a number: "))
    if word == "good" and 7 <= n <= 15:
        print("It’s good")
    elif word == "bad" and (n < 7 or n > 15):
        print("It’s bad")