Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d = {'anki':'Iphone','Anil':'Samsung','Kiran':'Oneplus'}
d
{'anki': 'Iphone', 'Anil': 'Samsung', 'Kiran': 'Oneplus'}
d.keys
<built-in method keys of dict object at 0x000001A92E972400>
d.keys()
dict_keys(['anki', 'Anil', 'Kiran'])
d.values()
dict_values(['Iphone', 'Samsung', 'Oneplus'])
d.get()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d.get()
TypeError: get expected at least 1 argument, got 0
d.get ('anki')
'Iphone'
d.get ('Anki')
x =5
y =6
x+y
11
x * y
30
>>> x / y
0.8333333333333334
>>> x//y
0
>>> x= x+2
>>> x
7
>>> x +=2
>>> x
9
>>> X *=5
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    X *=5
NameError: name 'X' is not defined. Did you mean: 'x'?
>>> x *=5
>>> x
45
>>> x>y
True
>>> X<y
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    X<y
NameError: name 'X' is not defined. Did you mean: 'x'?
>>> x<y
False
>>> x<=y
False
>>> x>=
SyntaxError: invalid syntax
>>> x>=y
True
>>> x>4 and y<5
False
>>> x>4 or y<4
True
>>> x= True
>>> notx
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    notx
NameError: name 'notx' is not defined
not x
False
x
True
x= not x
x
False
