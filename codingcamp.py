# Write your code here :-)
from random import randint

WIDTH = 800
HEIGHT = 600

zeppelin = Actor("zeppelin")
zeppelin.pos = 400,300


enemy = Actor("enemy-up")
enemy.pos = randint(800,1600), randint(10,200)

cave = Actor("cave")
cave.pos = randint(800,1600), 460


tree = Actor("tree")
tree.post = randint(800,1600), 450

enemy_up = True
up = False;
game_over = False
score = 0
number_of_updates = 0


scores = []
def update_high_score():
    global score, scores
    filename = r"C:\Users\wendi\Documents\high-score.txt"
    scores = []
    with open(filename, "r") as file:
        line = file.readline()
        high_scores = line.split()
        for high_score in high_scores:
            if(score > int(high_score)):
                scores.append(str(score)+ " ")
                score = int(high_score)
            else:
                scores.append(str(high_score)+ " ")
    with open(filename, "w") as file:
        for high_score in scores:
            file.write(high_score)


def display_high_score():
    screen.draw.text("HIGH SCORES", (350,150), color="black")
    for high_score in scores:
        screen.draw.text(str(high_score), (390, 175), color="black")

def draw():
    screen.blit("background", (0,0))
    if not game_over:
        zeppelin.draw()
        enemy.draw()
        cave.draw()
        tree.draw()
        tree.draw()
        screen.draw.text("Score : " + str(score), (700, 5), color="black")
    else:
        display_high_score()


def on_mouse_down():
    global up
    up = True
    zeppelin.y -= 50

def on_mouse_up():
    global up
    up = False

def flap():
    global enemy_up
    if enemy_up:
        enemy.image = "enemy-down"
        enemy_up = False
    else:
        enemy.image = "enemy-up"
        enemy_up = True

def update():
    global game_over, score, number_of_updates
    if not game_over:
        if not up:
            zeppelin.y += 1
        if enemy.x > 0:
            enemy.x -= 4
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates +=1
        else:
            enemy.x = randint(800,1600)
            enemy.y = randint(10,200)
            score += 1
            number_of_updates = 0

        if cave.right > 0:
            cave.x -= 2
        else:
            cave.x = randint(800, 1600)
            score += 1

        if tree.right > 0:
            tree.x -= 2
        else:
            tree.x = randint(800,1600)
            score +=1

        if zeppelin.top < 0 or zeppelin.bottom> 560:
            game_over = True
            update_high_score()

        if(zeppelin.collidepoint(enemy.x, enemy.y) or zeppelin.collidepoint(cave.x, cave.y) or zeppelin.collidepoint(tree.x, tree.y)) :
            game_over = True
            update_high_score()
