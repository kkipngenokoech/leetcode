# OOP

this is called object oriented programming, using functions and methods this we call procudure oriented programming

with OOP you can incoporate your data and functionality inside your code. all this is wrapped into an object.

classes and objects are two main aspects of object oriented programming. A class creates a new type where objects are instances of the class.

functions that are found inside a class is called a method.

the variables found inside a class are called `field`

Collectively, the fields and methods can be referred to as the attributes of that class.

fields are of two types:

1. instance/object fields/variables
2. class fields/variables

## class Variables

they can be accessed by all instances of the class.

There is only one copy of the class variable and when any one object makes a change to a class variable, that change will be seen by all the other instances.

let say you want to keep track of all henry ford cars despite the fact that there are different brands which include:

1. sedans
2. Suvs
3. trucks
4. ford-mustang
5. ford explorer
6. ford escape
7. ford Ranger
8. ford fusion

to give this different types a unique identifier which incirements you use class variables:

```python
class Ford:
    unique = hex(0000)
    def __init__(self, name):
        self.name = name
        Ford.unique += hex(1)
    def getFord(self):
        print("ford {}: id {}".format(self.name, self.unique))

```

the above method will give each ford created a unique number

## instance variables

are owned by each individual object/instance of the class. In this case, each object has its own copy of the field i.e. they are not shared and are not related in any way to the field by the same name in a different instance

A class is created using the `class` keyword.

## self

Class methods have only one specific difference from ordinary functions - they must have an extra first name that has to be added to the beginning of the parameter list, but you do not give a value for this parameter when you call the method, Python will provide it.

This particular variable refers to the object itself, and by convention, it is given the name self.

```python
class MyClass:
    variable = 'variable'

    def (self, name):
        pass
    def sayHi(self):
        print('hello multiverse')
```

## __init__ method

this method is run as soon as an object of a class is instantiated, this passes initial values to an object

i.e

```python
class Multiverse:
    def __init__(self, name):
        king = name
    def sayHi(self):
        print('hello multiverse this is {} speaking',king)
```

We do not explicitly call the __init__ method. This is the special significance of this method.
