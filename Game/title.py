import pygame

import asset
import const
import var
import lang
import UI

import physics

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    var.screen.blit(const.Font.title.render(lang.lang[var.lang]['game_title'], True, const.Color.black), UI.title_text)
    pygame.draw.rect(var.screen, const.Color.black, UI.Title.button_start, 2)
    var.screen.blit(const.Font.title.render(lang.lang[var.lang]['start'], True, const.Color.black), UI.Title.text_start)
    pygame.draw.rect(var.screen, const.Color.black, UI.Title.button_lang, 2)
    var.screen.blit(const.Font.title.render(lang.lang[var.lang]['lang'], True, const.Color.black), UI.Title.text_lang)
    pygame.display.flip()

def mouse_up(x, y, button):
    if button == 1:
        if var.state == '':
            if physics.point_inside_rect_array(x, y, UI.Title.button_lang):
                if var.lang == 'en':
                    var.lang = 'ko'
                elif var.lang == 'ko':
                    var.lang = 'en'

            if physics.point_inside_rect_array(x, y, UI.Title.button_start):
                var.scene = 'save'
                var.state = ''
