Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> map(range,10)

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    map(range,10)
TypeError: argument 2 to map() must support iteration
>>> map(lambda,x:x*x,range(10))
SyntaxError: invalid syntax
>>> map(lambda x:x*x,range(10))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> reduce(lambda x,y:x+y,range(10))
45
>>> reduce(lambda x,y:x+y,range(10))
45
>>> l = [1,2,3,4,'raja',6,7,'krishna','anji']
>>> l[:3]
[1, 2, 3]
>>> l[3:]
[4, 'raja', 6, 7, 'krishna', 'anji']
>>> l*[10]

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    l*[10]
TypeError: can't multiply sequence by non-int of type 'list'
>>> 
>>> 
>>> 
>>> t = (1,2,3,4)
>>> list(t)
[1, 2, 3, 4]
>>> l.append(4)
>>> l
[1, 2, 3, 4, 'raja', 6, 7, 'krishna', 'anji', 4]
>>> tuple(l)
(1, 2, 3, 4, 'raja', 6, 7, 'krishna', 'anji', 4)
>>> 
