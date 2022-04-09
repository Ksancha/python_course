# Data types
# String
In very simple terms - string is just a text. 
More generally, -  strings in Python are arrays of bytes representing unicode characters

## Initiation
To create a string, use single or double quotes
```
"MyString"
'MyString'
```
## Concatenation
Strings can be concatenated 
```
"Hello" + ' ' + "world"  # returns "Hello world" 
"5" + "3"		 # returns "53"
```
## Length 
Each string has a length. Use `len` function to find it
```
len("Hello")	# returns 5
```
## Indexing
Strings support indexing, meaning all elements (characters) of a string have an index, and we can access each one of them individually. 
```
"Life is good"[0]	# returns "L"
"Music[-1]"		# returns "c"
```
**_NOTE:_**  The first element has index 0

## Slicing
You can return a range of characters by using the slice syntax:
```
"slicing"[start:end:step]
```
```
“Good job”[2:5]		# returns "od "
“Good job”[2:]		# returns "od job"
“Good job”[-3:]		# returns "job"
“Good job”[2::2]	# returns "o o"
```
## Methods
Strings support various methods, just to name few:
```
“String”.lower()		# returns "string"
“string”.upper()		# returns "STRING"
“string”.capitalize()		# returns "String"
“StRiNg”.swapcase()		# returns "sTrInG"
```

# Numeric
Python supports standard mathematical operations:
|       Operator         |Name                        |Example|
|----------------|-------------------------------|-----------------------------|
|+|Addition|x + y    |
|-|Subtraction |x - y    |
|*|Multiplication|x * y|
|/|Division|x / y    |
|%|Modulus|x % y    |
|**|Exponentiation|x ** y|
|//|Floor division|x // y|
```
5 + 5		# 10
7 - 2		# 2
2 * 3		# 6
8 / 4		# 2
5 % 3		# 2
6 ** 2     	# 36
13 // 4     	# 3
```
# Booleans
Boolean is a special type and represents either `True` or `False`. Booleans are usually used to control a code flow.
```
a = 15
if a > 10:	# a > 10 evaluates to a boolean True
    print(f"{a} is greater than 10")
``` 
To evaluate an expression to a boolean, you can use `bool()`function:
```
print(bool("Hello"))  	  # True
print(bool(15))		  # True
print(bool([1, 2, 3]))	  # False
```
**_NOTE:_**  Python considers `0`, empty string, and empty list to be False when converting them to a boolean
```
print(bool("")) 	  # False
print(bool(0))		  # False
print(bool([]))		  # False
```
# Null
`NoneType` is a special type in Python. To create one, use a keyword `None`:
```
empty_var = None
```
