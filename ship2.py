import pgzrun
from random import randint
import itertools


WIDTH = 800
HEIGHT = 800


block_positions = [(775, 25), (775, 775), (25, 775), (25, 25)]
block_path = itertools.cycle(block_positions)


block = Actor("block.png", center=(100, 100))
ship = Actor("ship.png", center=(100, 100))


collision_happened = False

def draw():
    screen.clear()
    

    block.draw()
    ship.draw()

    if collision_happened:
        fire_rect = Rect((block.x - 25, block.y - 25), (50, 50))
        screen.draw.filled_rect(fire_rect, "red")

def move_block():
    animate(block, tween='bounce_end', duration=1.5, pos=next(block_path))

clock.schedule_interval(move_block, 2.5)

def next_target():
    x = randint(0, 800)
    y = randint(0, 800)
    ship.target = (x, y)

    target_angle = ship.angle_to(ship.target)
    target_angle += 360 * ((ship.angle - target_angle + 180) // 360)

    animate(ship, angle=target_angle, duration=0.5, on_finished=move_ship)

def move_ship():
    animate(ship, tween='accel_decel', pos=ship.target, duration=0.5, on_finished=check_collision)

def check_collision():
    global collision_happened

    if ship.colliderect(block):
        collision_happened = True
    else:
        collision_happened = False
    
    
    next_target()

move_block()
next_target()

pgzrun.go()
