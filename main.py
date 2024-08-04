# imports

import sys
import pygame

# configuration

pygame.init()
fps = 60
fps_Clock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont("Arial", 40)

objects = []


class Button:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        button_text="Button",
        onclick_function=None,
        one_press=False,
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclick_function = onclick_function
        self.one_press = one_press
        self.already_pressed = False

        self.fill_colors = {
            "normal": "#ffffff",
            "hover": "#666666",
            "pressed": "#333333",
        }

        self.button_surface = pygame.Surface((self.width, self.height))
        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.button_surf = font.render(button_text, True, (20, 20, 20))

        objects.append(self)
