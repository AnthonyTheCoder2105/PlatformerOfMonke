from pygame import *
from player import PlayerSprite
from maps import plats as platforms

WIDTH, HEIGHT = 800, 960
window = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()

p1 = PlayerSprite('dude.png', (300,200), (64,64,),(8, 20))

while not event.peek(QUIT):
    window.fill('black')
    
    offset = Vector2(0, 0)
    if p1.rect.right >= WIDTH-200 and p1.speed.x > 0:
        p1.rect.right = WIDTH-200
        offset = Vector2(-p1.speed.x, 0)
    elif p1.rect.left <= 200 and p1.speed.x < 0:
        p1.rect.left = 200
        offset = Vector2(-p1.speed.x, 0)


    platforms.update(offset)
    platforms.draw(window)

    p1.update(platforms)
    p1.draw(window)

    if p1.rect.bottom >= HEIGHT:
        break

    display.update()
    clock.tick(60)