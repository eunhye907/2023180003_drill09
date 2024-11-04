from pico2d import *

import game_world
from grass import Grass
from boy import Boy
from grass_1 import Grass1
# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():
    global running
    global boy

    running = True

    grass = Grass()
    game_world.add_object(grass, depth=0)

    boy = Boy()
    game_world.add_object(boy, depth=1)


    grass_1 = Grass1()
    game_world.add_object(grass_1, depth =2)

def update_world():
    game_world.update()
    pass


def render_world():
    clear_canvas()
    game_world. render()
    update_canvas()


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
