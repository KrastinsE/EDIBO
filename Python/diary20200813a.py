Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> int
<class 'int'>
>>> a
10
>>> type a
SyntaxError: invalid syntax
>>> 10 == int
False
>>> type(a) == int
True
>>> int(False)
0
>>> int(True)
1
>>> 'aaa'**10
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    'aaa'**10
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> a
10
>>> type(a)
<class 'int'>
>>> type(a) == int
True
>>> if type(a) == int:
	print("labi")

	
labi
>>> if type(a) == int:
	print("labi")

	
labi
>>> if type(a) == int:
	print("labi")
else:
	print("slikti")

	
labi
>>> if type(a) == int:
	print("Labi")
elif type(a) == float:
	print("arī labi")
else:
	print("Slikti")

	
Labi
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
labi
>>> a = 5.5.
SyntaxError: invalid syntax
>>> a = 5.5
>>> if type(a) == int:
	print("Labi")
elif type(a) == float:
	print("arī labi")
else:
	print("Slikti")

	
arī labi
>>> a = 5
>>> if type(a) == int:
	print("Labi")
elif type(a) == float:
	print("arī labi")
else:
	print("Slikti")

	
Labi
>>> a = abc
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a = abc
NameError: name 'abc' is not defined
>>> a = "sasds"
>>> if type(a) == int:
	print("Labi")
elif type(a) == float:
	print("arī labi")
else:
	print("Slikti")

	
Slikti
>>> if type(a) == int:
	print("Labi")
elif type(a) == float:
	print("arī labi")
elif type(a) == int:
	print("ir jau labi - bet šo tektstu neviens nekad neredzēs")
else:
	print("Slikti")

	
Slikti
>>> a = 2
>>> if type(a) == int:
	print("Labi")
elif type(a) == float:
	print("arī labi")
elif type(a) == int:
	print("ir jau labi - bet šo tektstu neviens nekad neredzēs")
else:
	print("Slikti")

	
Labi
>>> a = "qwerty"
>>> if type(a) == int:
	print("Labi")
elif type(a) == float:
	print("arī labi")
elif type(a) == int:
	print("ir jau labi - bet šo tektstu neviens nekad neredzēs")
else:
	print("Slikti")

	
Slikti
>>> a = 5.5
>>> if type(a) == int:
	print("Labi")
elif type(a) == float:
	print("arī labi")
elif type(a) == int:
	print("ir jau labi - bet šo tektstu neviens nekad neredzēs")
else:
	print("Slikti")

	
arī labi
>>> print("aaa\n bbb\n")
aaa
 bbb

>>> 
