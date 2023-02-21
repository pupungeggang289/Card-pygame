import pygame

import asset
import const
import var
import lang
import physics

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    pygame.display.flip()

def mouse_up(x, y, button):
    pass