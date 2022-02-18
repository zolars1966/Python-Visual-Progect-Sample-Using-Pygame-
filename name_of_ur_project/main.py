import pygame as pg
import random as rand
import math
import sys


def left_click():
    global l_press
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1 and not l_press:
            l_press = True
            return True
    elif event.type == pg.MOUSEBUTTONUP:
        if event.button == 1:
            l_press = False
    return False


def right_click():
    global r_press
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 3 and not r_press:
            r_press = True
            return True
    elif event.type == pg.MOUSEBUTTONUP:
        if event.button == 3:
            r_press = False
    return False


# global references
try:
    WIDTH, HEIGHT = int(sys.argv[1]), int(sys.argv[2])
except IndexError:
    WIDTH, HEIGHT = 1280, 720
TICK_RATE = 5
l_press, r_press = False, False

if __name__ == "__main__":
    # creating a pygame window
    screen = pg.display.set_mode((WIDTH, HEIGHT), vsync=1)
    clock = pg.time.Clock()

    # creating the game logic / environment sample

    upd_ticks = pg.time.get_ticks()

    # main cycle
    while True:
        # surfaces cleaning
        screen.fill((140, 140, 140))
        
        # checking for keyboard, window, mouse inputs or events
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_u:
                    TICK_RATE -= 1
                    upd_ticks = pg.time.get_ticks()
                if event.key == pg.K_i:
                    TICK_RATE += 1
                    upd_ticks = pg.time.get_ticks()
        
        if left_click():
            # do something
            pass
        
        if right_click():
            # do something
            pass

        # game Assets/UI/elements drawing

        # game environment updating
        if 0 <= pg.time.get_ticks() - upd_ticks - (1000 / TICK_RATE):
            upd_ticks = pg.time.get_ticks()
            # calling for game environment to update

        pg.display.set_caption("$~NameOfUrProject ~fps: " + str(round(clock.get_fps(), 2)) + " ~tickrate: " + str(TICK_RATE))

        pg.display.flip()
        clock.tick()
