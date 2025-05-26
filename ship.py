import pgzrun
from random import randint
import itertools 
WIDTH = 800
HEIGHT = 800
blockpos = [(775,25),(775, 775), (25,775), (25,25)]
finpos = itertools.cycle(blockpos)

block = Actor("block.png", center = (100, 100))
ship = Actor("ship.png", center= (100,100))
blockspeed = 7
shipspeed = 5

def draw():
    screen.clear()
    #screen.blit("bg.jpg", (0, 0))
    block.draw()
    ship.draw()


def moveblock():
    animate(block, "bounce_end", duration = 1.5, pos = next(finpos))


moveblock()

clock.schedule_interval(moveblock, 2.5)

def nexttarget():
    x = randint(200,600)
    y = randint(200,600)
    ship.target = x,y
    targetangle = ship.angle_to(ship.target)
    targetangle += 360 * ((ship.angle - targetangle + 180) // 360)
    animate(ship, angle = targetangle, duration = 0.5, on_finished = moveship)

def moveship():
    animate(ship,tween = 'accel_decel', pos = ship.target, duration = 0.5, on_finished = nexttarget )

nexttarget()
pgzrun.go()