import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500
TITLE = "Catrat Game"

score = 0
game_over = False

cat = Actor("cat")
cat.pos = 290, 450

rat = Actor("rat")
rat.pos = 250, 100

def draw():
    screen.blit("background",(0,0))
    cat.draw()
    rat.draw()
    screen.draw.text("Score:"+str(score), color="black", topleft=(10,10), fontsize=30)

    if game_over:
        screen.fill("white")
        screen.draw.text("time is up Your Score is: " + str(score),
                         center=(300,250), fontsize=50, color="black")

def place_rat():
    rat.x=randint(20,580)
    rat.y=randint(20,210)

def update():
    global score 
    if keyboard.left:
        cat.x=cat.x-2
    if keyboard.right:
        cat.x=cat.x+2
    if keyboard.up:
        cat.y=cat.y-2
    if keyboard.down:
        cat.y=cat.y+2

    rattouched=cat.colliderect(rat)
    if rattouched:
        score=score+10
        place_rat()

def times_up():
    global game_over
    game_over=True

clock.schedule(times_up,10.0)  

pgzrun.go()









