def myfunc(a,b):
    return sum((a,b)) * 0.05

# you noticed that to work on multiple arguments we have to pass it as a tuple
# But what if we want to pass more arguments

def myfunc1(*args):    # *args treats it as a tuple
    return sum(args) * 0.05   # it can be any word just prefix is '*'


print(myfunc1(40,60,100,1,34))


# '**' use of two astericks makes it treat the argumenst as dictionaries

def myfunc2(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))

    else:
        print('I did not find any fruit')

print(myfunc2(fruit ='apple',veggie = 'lettuce'))


# *args and **kwargs together:
def myfunc3(*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))

print(myfunc3(10,20,30, fruit='orange',food = 'eggs',animal = 'dog'))