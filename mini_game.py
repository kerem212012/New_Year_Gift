import random
import pgzrun


WIDTH = 600
HEIGHT = 450

TITLE = "New Year Gift"
FPS = 30

ship = Actor("doctor-1", (300, 400))
space = Actor("bg")

bullets = []
enemies = []
meteors = []
count = 0
mode = 'menu'
type1 = Actor("doctor-1", (100, 250))
type2 = Actor("doctor-2", (300, 250))
type3 = Actor("doctor-3", (500, 250))

for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    color = random.randint(1, 2)
    if color == 1:
        enemy = Actor("virus-1", (x, y))
        enemy.speed = random.randint(2, 8)
        enemies.append(enemy)
    elif color == 2:
        enemy = Actor("virus-2", (x, y))
        enemy.speed = random.randint(2, 8)
        enemies.append(enemy)
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    meteor = Actor("man", (x, y))
    meteor.speed = random.randint(2, 6)
    meteors.append(meteor)


def draw():
    global mode
    global ship
    global space
    global count
    global enemies
    global enemy
    global bullets
    global meteors
    if mode == 'menu':
        space.draw()
        screen.draw.text('CHOOSE YOUR DOCTOR', center=(300, 100), color="white", fontsize=36)
        type1.draw()
        type2.draw()
        type3.draw()
    if mode == 'game':
        space.draw()
        screen.draw.text(f'{count}', pos=(10, 10), color='black', fontsize=36)
        for i in range(len(meteors)):
            meteors[i].draw()
        ship.draw()
        for i in range(len(enemies)):
            enemies[i].draw()
        for i in range(len(bullets)):
            bullets[i].draw()
    elif mode == 'end':
        space.draw()
        screen.draw.text(f"GAME OVER\n{count}\nPRESS 'ENTER' FOR PLAY AGAIN", center=(300, 200), color="black",
                         fontsize=36)
        if keyboard.RETURN:
            mode = 'menu'
            ship = Actor("doctor-1", (300, 400))
            space = Actor("bg")
            enemies = []
            bullets = []
            meteors = []
            count = 0

            for i in range(5):
                x = random.randint(0, 600)
                y = random.randint(-450, -50)
                color = random.randint(1, 2)
                if color == 1:
                    enemy = Actor("virus-1", (x, y))
                    enemy.speed = random.randint(2, 8)
                    enemies.append(enemy)
                elif color == 2:
                    enemy = Actor("virus-2", (x, y))
                    enemy.speed = random.randint(2, 8)
                    enemies.append(enemy)
            for i in range(5):
                x = random.randint(0, 600)
                y = random.randint(-450, -50)
                meteor = Actor("man", (x, y))
                meteor.speed = random.randint(2, 6)
                meteors.append(meteor)



def on_mouse_move(pos):
    ship.pos = pos


def new_enemy():
    x = random.randint(0, 400)
    y = -50
    color = random.randint(1, 2)
    if color == 1:
        enemy = Actor("virus-1", (x, y))
        enemy.speed = random.randint(2, 8)
        enemies.append(enemy)
    elif color == 2:
        enemy = Actor("virus-2", (x, y))
        enemy.speed = random.randint(2, 8)
        enemies.append(enemy)


def enemy_ship():
    for i in range(len(enemies)):
        if enemies[i].y < 650:
            enemies[i].y = enemies[i].y + enemies[i].speed
        else:
            enemies.pop(i)
            new_enemy()


def meteorites():
    for i in range(len(meteors)):
        if meteors[i].y < 450:
            meteors[i].y = meteors[i].y + meteors[i].speed
        else:
            meteors[i].x = random.randint(0, 600)
            meteors[i].y = -20
            meteors[i].speed = random.randint(2, 10)


def collisions():
    global mode
    global count
    for m in range(len(enemies)):
        if ship.colliderect(enemies[m]):
            mode = 'end'
        for j in range(len(bullets)):
            if bullets[j].colliderect(enemies[m]):
                enemies.pop(m)
                bullets.pop(j)
                count += 1
                new_enemy()
                break


def update(dt):
    if mode == 'game':
        enemy_ship()
        ship.y = 400
        collisions()
        meteorites()
        for i in range(len(bullets)):
            if bullets[i].y < 0:
                bullets.pop(i)
                break
            else:
                bullets[i].y = bullets[i].y - 10

def on_mouse_down(button, pos):
    global mode
    global ship
    if mode == 'menu' and type1.collidepoint(pos):
        ship.image = "doctor-1"
        mode = 'game'
    elif mode == 'menu' and type2.collidepoint(pos):
        ship.image = "doctor-2"
        mode = 'game'
    elif mode == 'menu' and type3.collidepoint(pos):
        ship.image = "doctor-3"
        mode = 'game'

    elif mode == 'game' and button == mouse.LEFT:
        bullet = Actor("antivirus-1")
        bullet.pos = ship.pos
        bullets.append(bullet)
    elif mode == 'game' and button == mouse.RIGHT:
        bullet = Actor("antivirus-2")
        bullet.pos = ship.pos
        bullets.append(bullet)
pgzrun.go()