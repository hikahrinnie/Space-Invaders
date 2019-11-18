#------------ Space Invaders Game -------------#
import turtle
import os
import math
import random
import winsound

#create a start screen. "press start" to enter the game



#Set up the screen
mainscreen = turtle.Screen()
mainscreen.bgcolor("black")
mainscreen.title("Space Invaders")
mainscreen.bgpic("spacebackground.gif")

#background music
winsound.PlaySound("doctorwhotheme.wav", winsound.SND_ASYNC)

#register the shapes
turtle.register_shape("player.gif")
turtle.register_shape("spaceinvader.gif")

#Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("red")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#set the score to 0
score = 0

#draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,276)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.speed(0)
player.color("blue")
player.shape("player.gif")
player.penup()
player.setposition(0,-250)
player.setheading(90)

playerspeed = 20

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#Move the player
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
  

#move the bullet
def fire_bullet():
    #declare bulletstate as global in case it needs to change
    global bulletstate
    if bulletstate == "ready":
    #moves the bullet to just above the player
        winsound.PlaySound("shoot.wav", winsound.SND_ASYNC)
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#Create keyboard bindin
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")

#Number of enemies
number_of_enemies = 10
#enemies empty list
enemies = []
#adds enemies to list
for i in range(number_of_enemies):
    #Create the enemy turtle
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("spaceinvader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,250)
    y = random.randint(100,250)

    enemy.setposition(x,y)
enemyspeed = 2

#Create the bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 30

#Main game loop
while True:

    for enemy in enemies:
#Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

    #Move the enemy back and down
        if enemy.xcor() > 280:
            #moves all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #changes enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            #move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #changes enemy direction
            enemyspeed *= -1

        #check for a collision between the bullet and enemy
        if isCollision(bullet, enemy):
            winsound.PlaySound("invaderkilled.wav", winsound.SND_ASYNC)
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            #RESET THE ENEMY
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x,y)
            #update the score
            score +=10
            scorestring = "Score: %s" %score
            score_pen.clear() #clears previous score before updating
            score_pen.write(scorestring, False, align="left",font=("Arial",14,"normal"))


    if isCollision(player,enemy):
        winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break

#Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
#Check to see if bullet has gotten to top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

        
delay = raw_input("Press Enter to Quit")

