import turtle
import random
import math
import time

#Set background and border
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("SNAKE")
wn.bgpic("backgr_snake.gif")
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-200,-200)
border_pen.pendown()
border_pen.pensize(3)
for side in range(2):
    border_pen.fd(400)
    border_pen.lt(90)
    border_pen.fd(400)
    border_pen.lt(90)
border_pen.hideturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#Draw the score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.shapesize(0.1,0.1)
score_pen.penup()
score_pen.setposition(-200,200)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left",font=("Arial", 14, "normal"))

#High score
highest = open("highscore.txt","r")
last_score = highest.readline()
highest.close()

#Set food
food = turtle.Turtle()
food.color("red")
food.shape("square")
food.penup()
food.speed(0)
food.shapesize(0.9,0.9)
def food_creator():
    x = random.randint(-190,190)
    y = random.randint(-190,190)
    food.setposition(x,y)
food_creator()

#Credits and gameover pen
gameover_pen = turtle.Turtle()
gameover_pen.speed(0)
gameover_pen.color("orange")
gameover_pen.penup()
gameover_pen.setposition(200,-220)
creditstring = "Developed by REBASoftware"
gameover_pen.write(creditstring, False, align="right",font=("Arial", 10, "bold"))
gameover_pen.hideturtle()

#Set head
player = turtle.Turtle()
player.color("yellow")
player.shape("square")
player.penup()
player.speed(0)
player.shapesize(1,1)
player.setposition(-100,100)

def change_left(x):
    if x.heading() != 0:
        x.setheading(180)
def change_right(x):
    if x.heading() != 180:
        x.setheading(0)
def change_up(x):
     if x.heading() != 270:
        x.setheading(90)
def change_down(x):
     if x.heading() != 90:
        x.setheading(270)

wn.onkey(lambda: change_left(player),"Left")
wn.onkey(lambda: change_right(player),"Right")
wn.onkey(lambda: change_up(player),"Up")
wn.onkey(lambda: change_down(player),"Down")
wn.listen()

player_list = [player]

def player_creator(x):
    player_list.append(turtle.Turtle())
    player_list[x+1].color("yellow")
    player_list[x+1].shape("square")
    player_list[x+1].penup()
    player_list[x+1].speed(0)
    player_list[x+1].shapesize(1,1)
    t = player_list[x].xcor()
    y = player_list[x].ycor()
    player_list[x].setposition(t, y)

#Snake collision checker
def isCollision2(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 6:
        return True
    else:
        return False

coordinate_listx = []
coordinate_listy = []
food_counter = 0
end_check = 1
while end_check:
    if food_counter < 3:
        time.sleep(1/(30*(food_counter+1)))
    for i in player_list:
        coordinate_listx.append(i.xcor())
        coordinate_listy.append(i.ycor())
    if end_check:
        player.forward(5)
        player.forward(5)
    for i in range(len(player_list)-1):
        player_list[i+1].setposition(coordinate_listx[i],coordinate_listy[i])

    playerx = player.xcor()
    playery = player.ycor()
    if -210 < playerx < -194:
        end_check = 0
    if 194 < playerx < 210:
        end_check = 0
    if -210 < playery < -194:
        end_check = 0
    if 194 < playery < 210:
        end_check = 0
    if isCollision(player,food):
        player_creator(food_counter)
        food_counter +=1
        food_creator()
        score += 1000
        scorestring = "Score: %s" %score
        score_pen.clear()
        score_pen.write(scorestring, False, align="left",font=("Arial", 14, "normal"))

    for i in range(len(player_list)-1):
        if isCollision2(player_list[i+1],player):
            end_check = 0

    coordinate_listx = []
    coordinate_listy = []


print("game over")

time.sleep(1)
for j in player_list:
    j.hideturtle()
food.hideturtle()

score_pen.clear()
score_pen.penup()
gameover_pen.clear()
gameover_pen.penup()
gameover_pen.setposition(0,0)
if score>int(last_score):
    print(score)
    new_score = open("highscore.txt","w")
    new_score.write(str(score))
    new_score.close()
creditstring = "       GAME OVER\n Your Score:%s\n Last High Score:%s" %(score, last_score)
gameover_pen.write(creditstring, False, align="center",font=("Arial", 20, "bold"))
gameover_pen.hideturtle()
endcheck = 0



wn.mainloop()

