import turtle
import math
#from tkinter import *

print("----------------------------- STILL IS PROTOTYPE ------------------------------")
print("-------------------------------------------------------------------------------")

#------------------------
t = turtle.Turtle()
t.hideturtle()

one = turtle.Turtle()
one.hideturtle()

two = turtle.Turtle()
two.hideturtle()

three = turtle.Turtle()
three.hideturtle()

four = turtle.Turtle()
four.hideturtle()

five = turtle.Turtle()
five.hideturtle()

six = turtle.Turtle()
six.hideturtle()

seven = turtle.Turtle()
seven.hideturtle()

eight = turtle.Turtle()
eight.hideturtle()

nine = turtle.Turtle()
nine.hideturtle()

era = turtle.Turtle()
era.hideturtle()

ten = turtle.Turtle()
ten.hideturtle()

eq = turtle.Turtle()
eq.hideturtle()

plus = turtle.Turtle()
plus.hideturtle()

minus = turtle.Turtle()
minus.hideturtle()

multiply = turtle.Turtle()
multiply.hideturtle()

divide = turtle.Turtle()
divide.hideturtle()

sin = turtle.Turtle()
sin.hideturtle()

cos = turtle.Turtle()
cos.hideturtle()

tan = turtle.Turtle()
tan.hideturtle()

b = turtle.Turtle()
b.hideturtle()


#------------------------

t.speed(0)
t.up()
t.width(4)
t.down()

#_________Main Square_________x

t.up()
t.forward(-100)
t.left(90)
t.forward(15)
t.right(90)
t.down()
'''for i in range(2):
   t.forward(270 + 300)
   t.right(45)
   t.forward(10)
   t.right(45)
   t.forward(280)
   t.right(45)
   t.forward(10)
   t.right(45)'''

t.goto(275, 14)
t.right(45)
t.forward(10)
t.right(45)
t.forward(280)
t.right(45)
t.forward(10)
t.right(45)
t.goto(-111 - 155, -281)
t.right(45)
t.forward(10)
t.right(45)
t.forward(281)
t.right(45)
t.forward(10)
t.right(45)
t.forward(300)

t.width(2)
t.goto(121,14)
t.right(90)
t.up()
t.forward(15)
t.down()
t.forward(260)
t.up()
t.right(90)
t.forward(231)
t.right(90)
t.down()
t.forward(260)

#-------------------------------------------------#
one.up()
one.width(3)
one.speed(0)
one.down()

two.up()
two.width(3)
two.speed(0)
two.down()

three.up()
three.width(3)
three.speed(0)
three.down()

four.up()
four.width(3)
four.speed(0)
four.down()

five.up()
five.width(3)
five.speed(0)
five.down()

six.up()
six.width(3)
six.speed(0)
six.down()

seven.up()
seven.width(3)
seven.speed(0)
seven.down()

eight.up()
eight.width(3)
eight.speed(0)
eight.down()


nine.up()
nine.width(3)
nine.speed(0)
nine.down()

era.up()
era.width(3)
era.speed(0)
era.down()

ten.up()
ten.width(3)
ten.speed(0)
ten.down()

eq.up()
eq.width(3)
eq.speed(0)
eq.down()

plus.up()
plus.width(3)
plus.speed(0)
plus.down()

minus.up()
minus.width(3)
minus.speed(0)
minus.down()

multiply.up()
multiply.width(3)
multiply.speed(0)
multiply.down()

divide.up()
divide.width(3)
divide.speed(0)
divide.down()

sin.up()
sin.width(3)
sin.speed(0)
sin.down()

cos.up()
cos.width(3)
cos.speed(0)
cos.down()

tan.up()
tan.width(3)
tan.speed(0)
tan.down()

b.up()
b.width(3)
b.speed(0)
b.down()


#-------------------------------------------------#

#-------------------SCREEN SAVES-------------------#

l = turtle.Turtle()
l.speed(0)
l.width(5)
l.hideturtle()
l.up()
l.goto(-108.0, 125.0)
l.down()

a = turtle.Turtle()
a.speed(0)
a.width(5)
a.hideturtle()
a.up()
a.goto(-108.0, 125.0)
a.down()

def letter_one():
   l.write("1",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_two():
   l.write("2",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()
   
def letter_three():
   l.write("3",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()
   l.down()

def letter_four():
   l.write("4",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()
   
def letter_five():
   l.write("5",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_six():
   l.write("6",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_seven():
   l.write("7",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_eight():
   l.write("8",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_nine():
   l.write("9",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()
   
def letter_ten():
   l.write("0",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_plus():
   l.write("+",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_minus():
   l.write("-",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_multiply():
   l.write("×",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_divide():
   l.write("÷",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

def letter_sin():
   l.write("sin(",font=("Courier",40,'bold'))
   l.up()
   l.forward(130)
   l.down()

def letter_cos():
   l.write("cos(",font=("Courier",40,'bold'))
   l.up()
   l.forward(130)
   l.down()

def letter_tan():
   l.write("tan(",font=("Courier",40,'bold'))
   l.up()
   l.forward(130)
   l.down()

def letter_b():
   l.write(")",font=("Courier",40,'bold'))
   l.up()
   l.forward(30)
   l.down()

#-------------------SCREEN SAVES-------------------#


def btn_click(item):
    global expression
    expression = expression + str(item)
    #print(expression)
# 'bt_clear' function :This is used to clear 
# the input field

def bt_clear(): 
    global expression 
    expression = "" 
    l.clear()
    a.clear()
    l.up()
    l.goto(-108.0, 125.0)
    l.down()

    
# 'bt_equal':This method calculates the expression 
# present in input field
 
def bt_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    print(result)
    expression = result
    a.clear()
    a.up()
    a.goto(-190 , 55.0) 
    #a.forward(350)
    #a.right(90)
    #a.forward(70)
    #a.right(-90)
    a.down()
    a.write(result,font=("Courier",30,'bold'))
    a.up()
    a.forward(30)
    a.down()
    
expression = ""

#-------------------KEYBOARD DEFS-------------------#  
   
#-------------- ONE --------------#
one.up()
one.forward(-90)
one.down()
for i in range(4):
    one.forward(50)
    one.right(45)
    one.forward(5)
    one.right(45)

one.up()
one.right(90)
one.forward(50)
one.left(90)
one.forward(17)
one.write("1",font=("Courier",25,'bold'))
one.hideturtle()
#-------------- ONE --------------#

#-------------- TWO --------------#
two.up()
two.forward(-20)
two.down()
for i in range(4):
    two.forward(50)
    two.right(45)
    two.forward(5)
    two.right(45)

two.up()
two.right(90)
two.forward(50)
two.left(90)
two.forward(17)
two.write("2",font=("Courier",25,'bold'))
two.hideturtle()
#-------------- TWO --------------#

#-------------- THREE --------------#
three.up()
three.forward(50)
three.down()
for i in range(4):
    three.forward(50)
    three.right(45)
    three.forward(5)
    three.right(45)

three.up()
three.right(90)
three.forward(50)
three.left(90)
three.forward(17)
three.write("3",font=("Courier",25,'bold'))
three.hideturtle()
#-------------- THREE --------------#

#-------------- FOUR --------------#
four.up()
four.forward(-90)
four.right(90)
four.forward(70-3)
four.right(-90)
four.down()
for i in range(4):
    four.forward(50)
    four.right(45)
    four.forward(5)
    four.right(45)

four.up()
four.right(90)
four.forward(50)
four.left(90)
four.forward(17)
four.write("4",font=("Courier",25,'bold'))
four.hideturtle()
#-------------- FOUR --------------#

#-------------- FIVE --------------#
five.up()
five.forward(-20)
five.right(90)
five.forward(70-3)
five.right(-90)
five.down()
for i in range(4):
    five.forward(50)
    five.right(45)
    five.forward(5)
    five.right(45)

five.up()
five.right(90)
five.forward(50)
five.left(90)
five.forward(17)
five.write("5",font=("Courier",25,'bold'))
five.hideturtle()
#-------------- FIVE --------------#

#-------------- SIX --------------#
six.up()
six.forward(50)
six.right(90)
six.forward(70-3)
six.right(-90)
six.down()
for i in range(4):
    six.forward(50)
    six.right(45)
    six.forward(5)
    six.right(45)

six.up()
six.right(90)
six.forward(50)
six.left(90)
six.forward(17)
six.write("6",font=("Courier",25,'bold'))
six.hideturtle()
#-------------- SIX --------------#

#-------------- SEVEN --------------#
seven.up()
seven.forward(-90)
seven.right(90)
seven.forward(140-3)
seven.right(-90)
seven.down()
for i in range(4):
    seven.forward(50)
    seven.right(45)
    seven.forward(5)
    seven.right(45)

seven.up()
seven.right(90)
seven.forward(50)
seven.left(90)
seven.forward(17)
seven.write("7",font=("Courier",25,'bold'))
seven.hideturtle()
#-------------- SEVEN --------------#

#-------------- EIGHT --------------#
eight.up()
eight.forward(-20)
eight.right(90)
eight.forward(140-3)
eight.right(-90)
eight.down()
for i in range(4):
    eight.forward(50)
    eight.right(45)
    eight.forward(5)
    eight.right(45)

eight.up()
eight.right(90)
eight.forward(50)
eight.left(90)
eight.forward(17)
eight.write("8",font=("Courier",25,'bold'))
eight.hideturtle()
#-------------- EIGHT --------------#

#-------------- NINE --------------#
nine.up()
nine.forward(50)
nine.right(90)
nine.forward(140-3)
nine.right(-90)
nine.down()
for i in range(4):
    nine.forward(50)
    nine.right(45)
    nine.forward(5)
    nine.right(45)

nine.up()
nine.right(90)
nine.forward(50)
nine.left(90)
nine.forward(17)
nine.write("9",font=("Courier",25,'bold'))
nine.hideturtle()
#-------------- NINE --------------#

#-------------- ERASE --------------#
era.up()
era.forward(-90)
era.right(90)
era.forward(210-3)
era.right(-90)
era.down()
for i in range(4):
    era.forward(50)
    era.right(45)
    era.forward(5)
    era.right(45)

era.up()
era.right(90)
era.forward(50)
era.left(90)
era.forward(17)
era.write("C",font=("Courier",25,'bold'))
era.hideturtle()
#-------------- ERASE --------------#

#-------------- TEN --------------#
ten.up()
ten.forward(-20)
ten.right(90)
ten.forward(210-3)
ten.right(-90)
ten.down()
for i in range(4):
    ten.forward(50)
    ten.right(45)
    ten.forward(5)
    ten.right(45)

ten.up()
ten.right(90)
ten.forward(50)
ten.left(90)
ten.forward(17)
ten.write("0",font=("Courier",25,'bold'))
ten.hideturtle()
#-------------- TEN --------------#

#-------------- EQUAL --------------#

eq.up()
eq.forward(50)
eq.right(90)
eq.forward(210-3)
eq.right(-90)
eq.down()
for i in range(4):
    eq.forward(50)
    eq.right(45)
    eq.forward(5)
    eq.right(45)

eq.up()
eq.right(90)
eq.forward(50)
eq.left(90)
eq.forward(17)
eq.write("=",font=("Courier",25,'bold'))
eq.hideturtle()

#-------------- EQUAL --------------#

#-------------- PLUS --------------#
plus.up()
plus.forward(140)
plus.down()
for i in range(4):
    plus.forward(50)
    plus.right(45)
    plus.forward(5)
    plus.right(45)

plus.up()
plus.right(90)
plus.forward(50)
plus.left(90)
plus.forward(17)
plus.write("+",font=("Courier",25,'bold'))
plus.hideturtle()
#-------------- PLUS --------------#

#-------------- MINUS --------------#
minus.up()
minus.forward(140)
minus.right(90)
minus.forward(70-3)
minus.right(-90)
minus.down()
for i in range(4):
    minus.forward(50)
    minus.right(45)
    minus.forward(5)
    minus.right(45)

minus.up()
minus.right(90)
minus.forward(50)
minus.left(90)
minus.forward(17)
minus.write("-",font=("Courier",25,'bold'))
minus.hideturtle()
#-------------- MINUS --------------#

#-------------- MULTIPLE --------------#
multiply.up()
multiply.forward(140)
multiply.right(90)
multiply.forward(140-3)
multiply.right(-90)
multiply.down()
for i in range(4):
    multiply.forward(50)
    multiply.right(45)
    multiply.forward(5)
    multiply.right(45)

multiply.up()
multiply.right(90)
multiply.forward(50)
multiply.left(90)
multiply.forward(17)
multiply.write("×",font=("Courier",25,'bold'))
multiply.hideturtle()
#-------------- MULTIPLE --------------#

#-------------- DIVIDE --------------#
divide.up()
divide.forward(140)
divide.right(90)
divide.forward(210-3)
divide.right(-90)
divide.down()
for i in range(4):
    divide.forward(50)
    divide.right(45)
    divide.forward(5)
    divide.right(45)

divide.up()
divide.right(90)
divide.forward(50)
divide.left(90)
divide.forward(17)
divide.write("÷",font=("Courier",25,'bold'))
divide.hideturtle()
#-------------- DIVIDE --------------#

#-------------- SIN --------------#
sin.up()
sin.forward(140 + 70)
sin.down()
for i in range(4):
    sin.forward(50)
    sin.right(45)
    sin.forward(5)
    sin.right(45)

sin.up()
sin.right(90)
sin.forward(45)
sin.left(90)
sin.forward(3)
sin.write("sin",font=("Courier",20,'bold'))
sin.hideturtle()
#-------------- SIN --------------#

#-------------- COS --------------#
cos.up()
cos.forward(140 + 70)
cos.right(90)
cos.forward(70-3)
cos.right(-90)
cos.down()
for i in range(4):
    cos.forward(50)
    cos.right(45)
    cos.forward(5)
    cos.right(45)

cos.up()
cos.right(90)
cos.forward(45)
cos.left(90)
cos.forward(3)
cos.write("cos",font=("Courier",20,'bold'))
cos.hideturtle()
#-------------- COS --------------#

#-------------- TAN --------------#
tan.up()
tan.forward(140 + 70)
tan.right(90)
tan.forward(140-3)
tan.right(-90)
tan.down()
for i in range(4):
    tan.forward(50)
    tan.right(45)
    tan.forward(5)
    tan.right(45)

tan.up()
tan.right(90)
tan.forward(45)
tan.left(90)
tan.forward(3)
tan.write("tan",font=("Courier",20,'bold'))
tan.hideturtle()
#-------------- TAN --------------#

#-------------- ) --------------#
b.up()
b.forward(140 + 70)
b.right(90)
b.forward(210-3)
b.right(-90)
b.down()
for i in range(4):
    b.forward(50)
    b.right(45)
    b.forward(5)
    b.right(45)

b.up()
b.right(90)
b.forward(45)
b.left(90)
b.forward(21)
b.write(")",font=("Courier",20,'bold'))
b.hideturtle()
#-------------- ) --------------#

#-------------------KEYBOARD DEFS-------------------#  

print("U can write now :) ")

print("-------------------------------------------------------------------------------")

def check_button(x,y):
      # ONE
   if (x > -94 and x < -36 and y > -58 and y < -1):
        #print("1", end=(" "))
        letter_one()
        btn_click(1) 
   
      # TWO
   if (x > -24 and x < 34 and y > -58 and y < -1):
        #print("2", end=(" "))
        letter_two()  
        btn_click(2)
   
      # THREE
   if (x > 46 and x < 105 and y > -58 and y < -1):
        #print("3", end=(" "))
        letter_three()
        btn_click(3)
      
      # FOUR
   if (x > -94 and x < -36 and y > -124 and y < -67):
        #print("4", end=(" "))
        letter_four()
        btn_click(4)
   
      # FIVE
   if (x > -24 and x < 34 and y > -124 and y < -67):
        #print("5", end=(" "))
        letter_five()
        btn_click(5)
   
      # SIX
   if (x > 46 and x < 105 and y > -124 and y < -67):
        #print("6", end=(" "))
        letter_six()
        btn_click(6)
        
      # SEVEN
   if (x > -94 and x < -36 and y > -197 and y < -137):
        #print("7", end=(" "))
        letter_seven()
        btn_click(7)
        
      # EIGHT
   if (x > -24 and x < 34 and y > -197 and y < -137):
        #print("8", end=(" "))
        letter_eight()
        btn_click(8)
        
      # NINE
   if (x > 46 and x < 105 and y > -197 and y < -137):
        #print("9", end=(" "))
        letter_nine()
        btn_click(9)

      # ERASE
   if (x > -94 and x < -36 and y > -265 and y < -207):
        #print("=", end=(" "))
        bt_clear()     

      # TEN
   if (x > -24 and x < 34 and y > -265 and y < -207):
        #print("0", end=(" "))
        letter_ten()
        btn_click(0)

      # EQUAL
   if (x > 46 and x < 105 and y > -265 and y < -207):
        #print("=", end=(" "))
        bt_equal()

      # PLUS
   if (x > 136 and x < 195 and y > -58 and y < -1):
        #print("+", end=(" "))
        letter_plus()
        btn_click("+")

      # MINUS
   if (x > 136 and x < 195 and y > -124 and y < -67):
        #print("-", end=(" "))
        letter_minus()
        btn_click("-")

      # MULTIPLY
   if (x > 136 and x < 195 and y > -197 and y < -137):
        #print("×", end=(" "))
        letter_multiply()
        btn_click("*")

      # DIVIDE
   if (x > 136 and x < 195 and y > -265 and y < -207):
        #print("÷", end=(" "))
        letter_divide()
        btn_click("/")

   if (x > 207 and x < 266 and y > -58 and y < -1): 
        #print("sin", end=(" "))
        letter_sin()
        btn_click("math.sin(")
        
   if (x > 207 and x < 266 and y > -124 and y < -67): 
        #print("sin", end=(" "))
        letter_cos()
        btn_click("math.cos(")

   if (x > 207 and x < 266 and y > -197 and y < -137): 
        #print("sin", end=(" "))
        letter_tan()
        btn_click("math.tan(")

   if (x > 207 and x < 266 and y > -265 and y < -207): 
        #print("sin", end=(" "))
        letter_b()
        btn_click(")")

   

print("Your Answer")

def get_mouse_coords(x,y):
   print(x,y)

#turtle.onscreenclick(get_mouse_coords)

turtle.onscreenclick(check_button)


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^KEYBOARD^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#____________________________SCREEN TIME_____________________________#


turtle.mainloop()