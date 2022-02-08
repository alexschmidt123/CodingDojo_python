from os import access


num1 = 42
num2 = 2.3
#data type: Numbers

boolean = True
#data type: Boolean

string = 'Hello World'
#data type: Strings

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#data type: List

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#data type: Dictionary

fruit = ('blueberry', 'strawberry', 'banana')
#data type: Tuples

print(type(fruit))
# type check

print(pizza_toppings[1])
# access value

pizza_toppings.append('Mushrooms')
# add value


print(person['name'])
#access value

person['name'] = 'George'
#change value

person['eye_color'] = 'blue'
# add value

print(fruit[2])
#access value



if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#conditional


if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#conditional


for x in range(5):
    print(x)
#for loop: 0,1,2,3,4; [0,5), interval is 1

for x in range(2,5):
    print(x)
#for loop: 2,3,4; [2,5), interval is 1

for x in range(2,10,3):
    print(x)
#for loop: 2,5,8; [2,10), interval is 3



x = 0
while(x < 5):
    print(x)
    x += 1
#while loop, output is 0,1,2,3,4

pizza_toppings.pop()
#delete the last value

pizza_toppings.pop(1)
#delete the second value

print(person)
person.pop('eye_color')
print(person)
#delete the value whose key is 'eye_color'

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#data type: List
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')
print_hello_ten_times()
# function: print 'Hello' 10 times


def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
print_hello_x_times(4)
# function: function: print 'Hello' x times（x=4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
print_hello_x_or_ten_times()
print(" ")
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

print(num3)
num3 = 72
# NameError: name <variable name> is not defined

fruit[0] = 'cranberry'
# TypeError: 'tuple' object does not support item assignment

print(person['favorite_team'])
# KeyError: 'favorite_team'

print(pizza_toppings[7])
# IndexError: list index out of range

boolean = True
print(boolean)

fruit = ('blueberry', 'strawberry', 'banana')
fruit.append('raspberry')
fruit.pop(1)
# AttributeError: 'tuple' object has no attribute 'pop'
# AttributeError: 'tuple' object has no attribute 'append'