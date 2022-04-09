# Functions
A function is a block of code which only runs when it is called. A function can be parametrized. To define a function, use a keyword `def` followed by the name of your function (it can be anything, but should make sense):
```
def print_first_char(word):
	print(word[0])	# prints first character of a word

print_first_char("Hello") # prints 'H'
```
Functions always returns something when it finishes execution. By default, it returns None, but can be controlled with a keyword `return`:
```
def return_none():
	pass

def sqr_number(x):
	return x ** 2

a = return_none()
b = sqr_number(3)
print(a)	# prints 'None'
print(b)	# prints 9
```

## Arguments 
Arguments (or args) are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

```
def greet_person(first_name, surname):
	print("Hello {first_name} {surname}")
	print("Have a nice day")

greet_person("John", "Smith")
```