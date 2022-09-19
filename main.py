import turtle

#all the turtle settings & set up settings
wn = turtle.Screen()
wn.bgcolor("light pink")
wn.title("Turtle")
sal = turtle.Turtle()
sal.shape("turtle")
fin= 3
sal.pensize(fin)
sal.fillcolor('red')

#shape drawing functions
def circles(numOfCircles):
 x = numOfCircles
 while x >= 0:
    sal.circle(60)
    x = x-1
    sal.left(100)

def pentagon(num):
    i = 1
    for i in range(num):
     for i in range(5):
       sal.right(72)
       sal.forward(100)
     sal.left(30)
    i+1

#lol this was an accident, but works!
def coolStar(num):
    i = 1
    for i in range(num):
     for i in range(5):
       sal.right(72)
       sal.forward(100)
       sal.right(72)
       sal.back(10)
     sal.left(70)
    i+1

def hexagon(num):
    i = 1
    for i in range(num):
     for i in range(6):
       sal.right(60)
       sal.forward(100)
     sal.left(30)
    i+1

def triangle(num):
 for i in range(num):
  for i in range(3):
    sal.right(60)
    sal.forward(100)
    sal.right(60)
  sal.left(70)

def decagon(num):
    for i in range(num):
        for i in range(10):
            sal.right(36)
            sal.forward(100)
           # sal.right(36)
        sal.left(70)

def starOfDavid(num):
    for i in range(num):
        for i in range(7):
            sal.right(51.42)
            sal.forward(100)
            sal.right(51.42)
        sal.left(70)

def heptagon(num):
    for i in range(num):
        for i in range(7):
            sal.right(51.42)
            sal.forward(100)
        sal.left(70)

newInp = ""
coolInp = ""

#asks users initially for the shape they'd want
userInp = input("what do you want to draw?"
                "\nA. Circle"
                "\nB. Pentagon"
                "\nC. A cool star"
                "\nD. Hexagon"
                "\nE. Triangle"
                "\nF. Heptagon"
                "\nG. Star of david"
                "\nH. Decagon")
#circles!!
if userInp.lower() == "a":
    newInp = input("How many circles would you like to be drawn?"
                "\n1"
                "\n3"
                "\n5"
                "\n7"
                "\n9"
                "\n11")
    options = ["1", "3", "5", "7", "9", "11"]
    # check if element in list
    if newInp in options:
        circles(int(newInp))
    else:
        print("You typed something random or invalid!")
     #if newInp == "1":

    #        circles(1)
    #        print("drawing right now")
    # elif newInp =="3":
    #        circles(3)
    # elif newInp =="5":
    #        circles(5)
    # elif newInp =="7":
    #        circles(7)
    # elif newInp =="9":
    #        circles(9)
    # elif newInp =="11":
    #        circles(11)

#pentagon
elif userInp.lower() == "b":
    coolInp = input("How many would pentagons you like to be drawn?"
                "\n1"
                "\n3"
                "\n5"
                "\n7"
                "\n9"
                "\n11")
    optionsp = ["1", "3", "5", "7", "9", "12","15"]
    # check if element in list
    if coolInp in optionsp:
        pentagon(int(coolInp))
    else:
        print("You typed something random or invalid!")
    '''
    if coolInp == "1":
           print("drawing right now")
           pentagon(1)
    elif coolInp =="3":
           print("drawing right now")
           pentagon(3)
    elif coolInp =="5":
           print("drawing right now")
           pentagon(5)
    elif coolInp =="7":
           print("drawing right now")
           pentagon(7)
    elif coolInp =="9":
           print("drawing right now")
           pentagon(9)
    elif coolInp =="11":
           print("drawing right now")
           pentagon(11)
'''

elif userInp.lower() == "c":
#a cool star!!
    pewInp = input("How many cool stars would you like to be drawn?"
                "\n1"
                "\n3"
                "\n6"
                "\n9"
                "\n12"
                "\n15")
    optionsc = ["1", "3", "6", "9", "12", "15"]
# check if element in list
    if pewInp in optionsc:
     coolStar(int(pewInp))
    else:
     print("You typed something random or invalid!")
elif userInp.lower() == "d":
    qewInp = input("How many hexagons would you like to be drawn?"
                "\n1"
                "\n3"
                "\n6"
                "\n9"
                "\n12"
                "\n15")
    optionh = ["1", "3", "6", "9", "12", "15"]
    if qewInp in optionh:
        hexagon(int(qewInp))
    else:
        print("You typed something random or invalid!")
elif userInp.lower() == "e":
    wewInp = input("How many triangles would you like to be drawn?"
                "\n1"
                "\n3"
                "\n6"
                "\n9"
                "\n12"
                "\n15")
    optiont = ["1", "3", "6", "9", "12", "15"]
    if wewInp in optiont:
        triangle(int(wewInp))
    else:
        print("You typed something random or invalid!")
elif userInp.lower() == "f":
    eewInp = input("How many heptagons would you like to be drawn?"
                "\n1"
                "\n3"
                "\n6"
                "\n9"
                "\n12"
                "\n15")
    optionhe = ["1", "3", "6", "9", "12", "15"]
    if eewInp in optionhe:
        heptagon(int(eewInp))
    else:
        print("You typed something random or invalid!")
elif userInp.lower() == "g":
    rewInp = input("How many Stars of David would you like to be drawn?"
                "\n1"
                "\n3"
                "\n6"
                "\n9"
                "\n12"
                "\n15")
    optionsd = ["1", "3", "6", "9", "12", "15"]
    if rewInp in optionsd:
        starOfDavid(int(rewInp))
    else:
        print("You typed something random or invalid!")
elif userInp.lower() == "h":
    tewInp = input("How many decagons would you like to be drawn?"
                "\n1"
                "\n3"
                "\n6"
                "\n9"
                "\n12"
                "\n15")
    optionde = ["1", "3", "6", "9", "12", "15"]
    if tewInp in optionde:
        decagon(int(tewInp))
    else:
        print("You typed something random or invalid!")




