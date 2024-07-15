Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("welcome student")
welcome student
>>> print("hi");
hi
>>> name="Rohit"
>>> print(name)
Rohit
>>> #variable declaation & assignment
>>> a=20
>>> print(a)
20
>>> 1abc="raj"
SyntaxError: invalid decimal literal
>>> _ab2=80
>>> ABC=20
>>> #DATATYPE
>>> a=5
>>> print(a)
5
>>> print(type(a))
<class 'int'>
>>> a=10.6
>>> print(type(a))
<class 'float'>
>>> a=1+3j
>>> print(type(a))
<class 'complex'>
>>> a="Rajshri"
>>> print(a)
Rajshri
>>> a='Rajshri'
>>> print(a)
Rajshri
>>> list1=[1,2,"hi",10.4]
>>> print(list1)
[1, 2, 'hi', 10.4]
>>> print(type(list1))
<class 'list'>
>>> print(list1+list1)
[1, 2, 'hi', 10.4, 1, 2, 'hi', 10.4]
#list concatination using +operator
print(list1*3)
[1, 2, 'hi', 10.4, 1, 2, 'hi', 10.4, 1, 2, 'hi', 10.4]
print(list1*1)
[1, 2, 'hi', 10.4]
#list repetation using * opeartor
print(list1[3:])
[10.4]
print(list1[0:3])
[1, 2, 'hi']
t1=("abc",1.1,12)
print(type(t1))
<class 'tuple'>
print(t1)
('abc', 1.1, 12)
print(t1+t1)
('abc', 1.1, 12, 'abc', 1.1, 12)
('abc', 1.1, 12, 'abc', 1.1, 12)
('abc', 1.1, 12, 'abc', 1.1, 12)
print(t1*5)
('abc', 1.1, 12, 'abc', 1.1, 12, 'abc', 1.1, 12, 'abc', 1.1, 12, 'abc', 1.1, 12)
t[1]="rajshri"
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    t[1]="rajshri"
NameError: name 't' is not defined. Did you mean: 't1'?
t1[1]="rajshri"
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    t1[1]="rajshri"
TypeError: 'tuple' object does not support item assignment
d={101:'rohit',102:'mohit',103:'pranali'}
print(d)
{101: 'rohit', 102: 'mohit', 103: 'pranali'}
d={101:'rohit',101:'mohit',103:'pranali'}
d={101:'rohit',102:'mohit',103:'mohit'}
print(d)
{101: 'rohit', 102: 'mohit', 103: 'mohit'}
d={101:'rohit',101:'mohit',103:'pranali'}
print(d)
{101: 'mohit', 103: 'pranali'}
d[1]="ram"
print(d)
{101: 'mohit', 103: 'pranali', 1: 'ram'}
print(d[0])
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print(d[0])
KeyError: 0
d={1:10,2:20,3:30}
print(d)
{1: 10, 2: 20, 3: 30}
print(d[2])
20
print(d[4])
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(d[4])
KeyError: 4
print(d.keys())
dict_keys([1, 2, 3])
print(d.values())
dict_values([10, 20, 30])
print(type(false))
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(type(false))
NameError: name 'false' is not defined. Did you mean: 'False'?
print(type(False))
<class 'bool'>
print(type(True))
<class 'bool'>
s1=set()#empty set
print(s1)
set()
s1={1,1.3,'hiiii',56}
print(s1)
{56, 1.3, 'hiiii', 1}
s1.add(100)
print(s1)
{1.3, 1, 100, 56, 'hiiii'}
s1.remove(2)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s1.remove(2)
KeyError: 2
s1.remove(56)
print(s1)
{1.3, 1, 100, 'hiiii'}
