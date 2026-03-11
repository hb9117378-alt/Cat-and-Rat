import pgzrun
from random import randint
WIDTH = 600
HEIGHT = 500
TITLE = "Catrat Game"
score = 0
game_over = False
cat = Actor("cat")
cat.pos = 290, 450
rat.pos = 250, 100
def draw():
    screen.blit("background",(0,0))
    cat.draw()
    screen.draw.text("Score:"+str(score),color="black",topleft=(10,10),fontsize=30)
pgzrun.go()