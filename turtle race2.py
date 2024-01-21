import turtle, random, time
from random import randint

turtle.bgcolor("lightgreen")

turt = turtle.Turtle()
turt.speed(10)
turt.shape("turtle")
turt.turtlesize(randint(1,5),randint(1,5),randint(1,5))
turt.color("blue")
turt.penup()
turt.setpos(-430,-1000)
turt.pendown()
turt.left(90)

turt.speed(randint(1,5))

tim = turtle.Turtle()
tim.speed(10)
tim.shape("turtle")
tim.turtlesize(randint(1,5),randint(1,5),randint(1,5))
tim.color("red")
tim.penup()
tim.setpos(-230,-1000)
tim.pendown()
tim.left(90)

tim.speed(randint(1,5))

terry = turtle.Turtle()
terry.speed(10)
terry.shape("turtle")
terry.turtlesize(randint(1,5),randint(1,5),randint(1,5))
terry.color("green")
terry.penup()
terry.setpos(-30,-1000)
terry.pendown()
terry.left(90)

terry.speed(randint(1,5))

tron= turtle.Turtle()
tron.speed(10)
tron.shape("turtle")
tron.turtlesize(randint(1,5),randint(1,5),randint(1,5))
tron.color("purple")
tron.penup()
tron.setpos(170,-1000)
tron.pendown()
tron.left(90)

tron.speed(randint(1,5))

tres = turtle.Turtle()
tres.speed(10)
tres.shape("turtle")
tres.turtlesize(randint(3,5),randint(3,5),randint(3,5))
tres.color("orange")
tres.penup()
tres.setpos(370,-1000)
tres.pendown()
tres.left(90)

tres.speed(randint(1,5))

x=0

if x == 0:
	a = time.time()
	turt.speed(randint(1,5))
	turt.forward(2000)
	b = time.time()
	ab = b-a
	
	c = time.time()
	tim.speed(randint(1,5))
	tim.forward(2000)
	d = time.time()
	cd = d-c
	
	e = time.time()
	terry.speed(randint(1,5))
	terry.forward(2000)
	f = time.time()
	ef = f-e
	
	g = time.time()
	tron.speed(randint(1,5))
	tron.forward(2000)
	h = time.time()
	gh = h-g
	
	i = time.time()
	tres.speed(randint(1,5))
	tres.forward(2000)
	j = time.time()
	ij = j-i

l = [ab,cd,ef,gh,ij]

l.sort()

if ab == l[0]:
	turtle.write("\n\n\n\nblue is 1st\n\n\n\n",move=True,align="right",font=("ariel",10))
	
elif cd == l[0]:
	turtle.write("\n\n\n\nred is 1st\n\n\n\n",move=True,align="right",font=("ariel",10,"normal"))
	
elif ef == l[0]:
	turtle.write("\n\n\n\ngreen is 1st\n\n\n\n",move=True,align="right",font=("ariel",10,"normal"))
	
elif gh == l[0]:
	turtle.write("\n\n\n\npurple is 1st\n\n\n\n",move=True,align="right",font=("ariel",10))
	e
elif ij == l[0]:
	turtle.write("\n\n\n\norange is 1st\n\n\n\n",move=True,align="right",font=("ariel",10))
	
	
	
if ab == l[1]:
	turtle.write("\n\n\nblue is 2nd\n\n\n",move=True,align="right",font=("ariel",10))
	
elif cd == l[1]:
	turtle.write("\n\n\nred is 2nd\n\n\n",move=True,align="right",font=("ariel",10,"normal"))
	
elif ef == l[1]:
	turtle.write("\n\n\ngreen is 2nd\n\n\n",move=True,align="right",font=("ariel",10,"normal"))
	
elif gh == l[1]:
	turtle.write("\n\n\npurple is 2nd\n\n\n",move=True,align="right",font=("ariel",10))
	
elif ij == l[1]:
	turtle.write("\n\n\norange is 2nd\n\n\n",move=True,align="right",font=("ariel",10))
	


if ab == l[2]:
	turtle.write("\n\nblue is 3rd\n\n",move=True,align="right",font=("ariel",10))
	
elif cd == l[2]:
	turtle.write("\n\nred is 3rd\n\n",move=True,align="right",font=("ariel",10,"normal"))
	
elif ef == l[2]:
	turtle.write("\n\ngreen is 3rd\n\n",move=True,align="right",font=("ariel",10,"normal"))
	
elif gh == l[2]:
	turtle.write("\n\npurple is 3rd\n\n",move=True,align="right",font=("ariel",10))
	
elif ij == l[2]:
	turtle.write("\n\norange is 3rd\n\n",move=True,align="right",font=("ariel",10))


if ab == l[3]:
	turtle.write("\nblue is 4th\n",move=True,align="right",font=("ariel",10))
	
elif cd == l[3]:
	turtle.write("\nred is 4th\n",move=True,align="right",font=("ariel",10,"normal"))
	
elif ef == l[3]:
	turtle.write("\ngreen is 4th\n",move=True,align="right",font=("ariel",10,"normal"))
	
elif gh == l[3]:
	turtle.write("\npurple is 4th\n",move=True,align="right",font=("ariel",10))
	
elif ij == l[3]:
	turtle.write("\norange is 4th\n",move=True,align="right",font=("ariel",10))
	

if ab == l[4]:
	turtle.write("\nblue is 5th",move=True,align="right",font=("ariel",10))
	
elif cd == l[4]:
	turtle.write("red is 5th",move=True,align="right",font=("ariel",10,"normal"))
	
elif ef == l[4]:
	turtle.write("green is 5th",move=True,align="right",font=("ariel",10,"normal"))
	
elif gh == l[4]:
	turtle.write("purple is 5th",move=True,align="right",font=("ariel",10))
	
elif ij == l[4]:
	turtle.write("orange is 5th",move=True,align="right",font=("ariel",10))	

turtle.exitonclick()