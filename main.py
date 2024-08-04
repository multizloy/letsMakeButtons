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

    def process(self):
        mouse_pos = pygame.mouse.get_pos()
        self.button_surface.fill(self.fill_colors["normal"])
        if self.button_rect.collidepoint(mouse_pos):
            self.button_surface.fill(self.fill_colors["hover"])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.button_surface.fill(self.fill_colors["pressed"])
                if self.one_press:
                    self.onclick_function()
                elif not self.already_pressed:
                    self.onclick_function()
                    self.already_pressed = True
            else:
                self.already_pressed = False

        self.button_surface.blit(
            self.button_surf,
            [
                self.button_rect.width / 2 - self.button_surf.get_rect().width / 2,
                self.button_rect.height / 2 - self.button_surf.get_rect().height / 2,
            ],
        )
        screen.blit(self.button_surface, self.button_rect)


def my_Function():
    print("Button Pressed")


Button(30, 30, 400, 100, "Button One (onePress)", my_Function)
Button(30, 140, 400, 100, "Button Two (multiPress)", my_Function, True)

while True:
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for object in objects:
        object.process()
    pygame.display.flip()
    fps_Clock.tick(fps)
