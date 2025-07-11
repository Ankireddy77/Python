Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> num = 2.5
>>> type (num)
<class 'float'>
>>> num + 5
7.5
>>> num =5
>>> type (num)
<class 'int'>
>>> num = 6+9j
>>> type (num)
<class 'complex'>
>>> a=5.6
>>> type (a)
<class 'float'>
>>> b = int (a)
>>> type (b)
<class 'int'>
>>> type (a)
<class 'float'>
>>> b
5
>>> k = 6
>>> k = float (b)
>>> k
5.0
>>> k = 6
>>> c = complex (b,k)
>>> c
(5+6j)
>>> type (c)
<class 'complex'>
>>> b>k
False
>>> bool = b>k
>>> bool
False
