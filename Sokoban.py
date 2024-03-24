import pygame
from pygame.locals import *
import constants as SOKOBAN
from game import *

class Menu:
    def __init__(self):
        self.image = pygame.image.load('assets/images/menu.png').convert_alpha()
        self.new_game_txt = "New Game"
        self.load_game_txt = "Continue"
        self.quit_game_txt = "Quit"
        self.font = pygame.font.Font('assets/fonts/FreeSansBold.ttf', 30)

    def click(self, click_pos, window):
        x = click_pos[0]
        y = click_pos[1]

        if x > self.new_game_txt_position[0] and x < self.new_game_txt_position[0] + self.new_game_txt_surface.get_width() \
        and y > 300 and y < 300 + self.new_game_txt_surface.get_height():
            sokoban = Game(window)
            sokoban.start()
        elif x > self.load_game_txt_position[0] and x < self.load_game_txt_position[0] + self.load_game_txt_surface.get_width() \
        and y > 370 and y < 370 + self.load_game_txt_surface.get_height():
            sokoban = Game(window)
            sokoban.scores.load()
        elif x > self.quit_game_txt_position[0] and x < self.quit_game_txt_position[0] + self.quit_game_txt_surface.get_width() \
        and y > 440 and y < 440 + self.quit_game_txt_surface.get_height():
            return False

        return True

    def render(self, window):
        window.blit(self.image, (0,0))

        self.new_game_txt_surface = self.font.render(self.new_game_txt, True, SOKOBAN.BLACK, SOKOBAN.WHITE)
        self.new_game_txt_position = ((SOKOBAN.WINDOW_WIDTH / 2) - (self.new_game_txt_surface.get_width() / 2), 300)
        window.blit(self.new_game_txt_surface, self.new_game_txt_position)

        self.load_game_txt_surface = self.font.render(self.load_game_txt, True, SOKOBAN.BLACK, SOKOBAN.WHITE)
        self.load_game_txt_position = ((SOKOBAN.WINDOW_WIDTH / 2) - (self.load_game_txt_surface.get_width() / 2), 370)
        window.blit(self.load_game_txt_surface, self.load_game_txt_position)

        self.quit_game_txt_surface = self.font.render(self.quit_game_txt, True, SOKOBAN.BLACK, SOKOBAN.WHITE)
        self.quit_game_txt_position = ((SOKOBAN.WINDOW_WIDTH / 2) - (self.quit_game_txt_surface.get_width() / 2), 440)
        window.blit(self.quit_game_txt_surface, self.quit_game_txt_position)


def main():
    pygame.init()
    pygame.key.set_repeat(SOKOBAN.REPEAT_PARAM, 100)
    pygame.display.set_caption("Sokoban Game")
    window = pygame.display.set_mode((SOKOBAN.WINDOW_WIDTH, SOKOBAN.WINDOW_HEIGHT))
    menu = Menu()

    run = True
    while run:
        event = pygame.event.wait()
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_j:
                sokoban = Game(window)
                sokoban.start()
            elif event.key == K_c:
                sokoban = Game(window)
                sokoban.scores.load()
            elif event.key == K_ESCAPE:
                run = False
        if event.type == MOUSEBUTTONUP:
            run = menu.click(event.pos, window)

        pygame.draw.rect(window, SOKOBAN.WHITE, (0,0,SOKOBAN.WINDOW_WIDTH,SOKOBAN.WINDOW_HEIGHT))
        menu.render(window)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
