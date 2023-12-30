x = 5
y = "hello"
a = [1,2,3]
try:
    print("Test1")
    print(a[0])
    z = x + y
    print("Test2")
except TypeError:
    print("Error: cannot add an int and a str")
except IndexError:
    print("Error1")
except:
    print("Error2")
#Test1
#1
#Error: cannot add an int and a str
#######################################
x = 5
y = "hello"
a = [1,2,3]
try:
    print("Test1")
    print(a[3])
    z = x + y
    print("Test2")
except TypeError:
    print("Error: cannot add an int and a str")
except IndexError:
    print("Error1")
except:
    print("Error2")
#Test1
#Error1

#######################################
x = 5
y = "hello"
try:
 z = x + y
except TypeError:
 print("Error: cannot add an int and a str")
#######################################
a = [1, 2, 3]
try:
 print ("Second element = %d" %(a[1]))
 print ("Fourth element = %d" %(a[3]))
except:
 print ("An error occurred")

##Second element = 2
##An error occurred
######################################
def fun(a):
    if a < 4:
        b = a / (a - 3)
    print("Value of b = ", b)

try:
    fun(5)
    fun(3)
    ##fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")##ZeroDivisionError Occurred and Handled =>in case of fun(3) call first
except NameError:
    print("NameError Occurred and Handled")##NameError Occurred and Handled =>in case of fun(5) call first
##########################################
try:
 k = 5//0
 print(k)
except ZeroDivisionError:
 print("Can't divide by zero")
finally:
 print('This is always executed')
#Can't divide by zero
#This is always executed
#############################
try:
 raise NameError("Hi there")
except NameError:
 print ("An exception")
 raise##NameError: Hi there becouse we raise exaption again
################################
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except Exception as e:
        # By this way we can know about the type of error occurring
        print("The error is: ", e)
divide(3, "GFG")##The error is:  unsupported operand type(s) for //: 'int' and 'str'
divide(3, 0)##The error is:  integer division or modulo by zero
########################
if(a<3):
print("gfg") ###IndentationError
######################
# try for unsafe code
try:
    amount = 1999
    if amount < 2999:

        # raise the ValueError
        raise ValueError("please add money in your account")
    else:
        print("You are eligible to purchase DSA Self Paced course")

    # if false then raise the value error
except ValueError as e:
    print(e)
###please add money in your account
#####################################
try:
    a = 10/0
    print (a)
except ArithmeticError:
        print ("This statement is raising an arithmetic exception.")
else:
    print ("Success.")

#############################
try:
	a = [1, 2, 3]
	print (a[3])
except LookupError:
	print ("Index out of bound error.")
else:
	print ("Success")

###############################
class Attributes(object):
    pass


object = Attributes()
print(object.attribute)#AttributeError
######################################
while True:
    data = input('Enter name : ')
    print ('Hello  ', data)
#Enter Name :Hello Aditi
#Enter Name :Traceback (most recent call last):
  #File "exceptions_EOFError.py", line 13, in
   # data = raw_input('Enter name :')
#EOFError: EOF when reading a line
########################################
import math

print(math.exp(1000))#FloatingPointError
###########################
def my_generator():
	try:
		for i in range(5):
			print ('Yielding', i)
			yield i
	except GeneratorExit:
		print ('Exiting early')

g = my_generator()
print (g.next())
g.close()
#Yielding 0
#0
#Exiting early

##################################
try:
    print ('Press Return or Ctrl-C:',)
    ignored = input()
except [Exception,err]:
 print ('Caught exception:', err)
except [KeyboardInterrupt,err]:
 print ('Caught KeyboardInterrupt')
else:
    print ('No exception')
###Press Return or Ctrl-C: ^CCaught KeyboardInterrupt
########################################
def fact(a):
	factors = []
	for i in range(1, a+1):
		if a%i == 0:
			factors.append(i)
	return factors

num = 600851475143
print (fact(num))#MemoryError
##############################





