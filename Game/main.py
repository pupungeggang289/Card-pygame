import pygame
import sys

import asset
import var
import const

import title

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.screen_size)
    pygame.display.set_caption('Card Game Sample')
    var.clock = pygame.time.Clock()

    load_font()
    load_image()

def load_font():
    pygame.font.init()
    const.Font.title = pygame.font.Font('Font/neodgm.ttf', 32)
    const.Font.main_1 = pygame.font.Font('Font/neodgm.ttf', 24)
    const.Font.main_2 = pygame.font.Font('Font/neodgm.ttf', 16)

def load_image():
    pass

def main():
    while True:
        input_handle()
        loop_scene()

def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def loop_scene():
    if var.scene == 'title':
        title.loop()

init()
main()