import pygame
from pygame.locals import *
import constants as SOKOBAN
from copy import deepcopy
import time

class Player:
    def __init__(self, level):
        self.pos = level.position_player
        self.direction = SOKOBAN.DOWN

    def move(self, direction, level, interface):
        x = self.pos[0]
        y = self.pos[1]

        levelHasChanged = False
        previous_level_structure = deepcopy(level.structure)
        previous_player_pos = [x,y]

        if direction == K_LEFT or direction == K_q:
            self.direction = SOKOBAN.LEFT
            if x > 0 and level.structure[y][x - 1] in [SOKOBAN.AIR, SOKOBAN.TARGET]:
                # Player just move on an empty case to the left
                self.pos[0] -= 1
            elif x > 1 and level.structure[y][x - 1] in [SOKOBAN.BOX, SOKOBAN.TARGET_FILLED] and level.structure[y][x - 2] in [SOKOBAN.AIR, SOKOBAN.TARGET]:
                # Player is trying to push a box to the left
                levelHasChanged = True
                if level.structure[y][x - 1] == SOKOBAN.TARGET_FILLED:
                    level.structure[y][x - 1] = SOKOBAN.TARGET
                else:
                    level.structure[y][x - 1] = SOKOBAN.AIR

                if level.structure[y][x - 2] == SOKOBAN.TARGET_FILLED:
                    level.structure[y][x - 2] = SOKOBAN.TARGET
                elif level.structure[y][x - 2] == SOKOBAN.TARGET:
                    level.structure[y][x - 2] = SOKOBAN.TARGET_FILLED
                else:
                    level.structure[y][x - 2] = SOKOBAN.BOX

                self.pos[0] -= 1

        if direction == K_RIGHT or direction == K_d:
            self.direction = SOKOBAN.RIGHT
            if level.structure[y][x + 1] in [SOKOBAN.AIR, SOKOBAN.TARGET]:
                self.pos[0] += 1
            elif level.structure[y][x + 1] in [SOKOBAN.BOX, SOKOBAN.TARGET_FILLED] and level.structure[y][x + 2] in [SOKOBAN.AIR, SOKOBAN.TARGET]:
                # Player is trying to push a box to the right
                levelHasChanged = True
                if level.structure[y][x + 1] == SOKOBAN.TARGET_FILLED:
                    level.structure[y][x + 1] = SOKOBAN.TARGET
                else:
                    level.structure[y][x + 1] = SOKOBAN.AIR

                if level.structure[y][x + 2] == SOKOBAN.TARGET_FILLED:
                    level.structure[y][x + 2] = SOKOBAN.TARGET
                elif level.structure[y][x + 2] == SOKOBAN.TARGET:
                    level.structure[y][x + 2] = SOKOBAN.TARGET_FILLED
                else:
                    level.structure[y][x + 2] = SOKOBAN.BOX

                self.pos[0] += 1

        if direction == K_UP or direction == K_z:
            self.direction = SOKOBAN.UP
            if y > 0 and level.structure[y - 1][x] in [SOKOBAN.AIR, SOKOBAN.TARGET]:
                self.pos[1] -= 1
            elif y > 1 and level.structure[y - 1][x] in [SOKOBAN.BOX, SOKOBAN.TARGET_FILLED] and level.structure[y - 2][x] in [SOKOBAN.AIR, SOKOBAN.TARGET]:
                # Player is trying to push a box to the left
                levelHasChanged = True
                if level.structure[y - 1][x] == SOKOBAN.TARGET_FILLED:
                    level.structure[y - 1][x] = SOKOBAN.TARGET
                else:
                    level.structure[y - 1][x] = SOKOBAN.AIR

                if level.structure[y - 2][x] == SOKOBAN.TARGET_FILLED:
                    level.structure[y - 2][x] = SOKOBAN.TARGET
                elif level.structure[y - 2][x] == SOKOBAN.TARGET:
                    level.structure[y - 2][x] = SOKOBAN.TARGET_FILLED
                else:
                    level.structure[y - 2][x] = SOKOBAN.BOX

                self.pos[1] -= 1

        if direction == K_DOWN or direction == K_s:
            self.direction = SOKOBAN.DOWN
            if level.structure[y + 1][x] in [SOKOBAN.AIR, SOKOBAN.TARGET]:
                self.pos[1] += 1
            elif level.structure[y + 1][x] in [SOKOBAN.BOX, SOKOBAN.TARGET_FILLED] and level.structure[y + 2][x] in [SOKOBAN.AIR, SOKOBAN.TARGET]:
                # Player is trying to push a box to the left
                levelHasChanged = True
                if level.structure[y + 1][x] == SOKOBAN.TARGET_FILLED:
                    level.structure[y + 1][x] = SOKOBAN.TARGET
                else:
                    level.structure[y + 1][x] = SOKOBAN.AIR

                if level.structure[y + 2][x] == SOKOBAN.TARGET_FILLED:
                    level.structure[y + 2][x] = SOKOBAN.TARGET
                elif level.structure[y + 2][x] == SOKOBAN.TARGET:
                    level.structure[y + 2][x] = SOKOBAN.TARGET_FILLED
                else:
                    level.structure[y + 2][x] = SOKOBAN.BOX

                self.pos[1] += 1

        if levelHasChanged:
            level.last_structure_state = previous_level_structure
            level.last_player_pos = previous_player_pos
            interface.colorTxtCancel = SOKOBAN.BLACK

    def render(self, window, textures):
        if self.direction == SOKOBAN.DOWN:
            top = 0
        elif self.direction == SOKOBAN.LEFT:
            top = SOKOBAN.SPRITESIZE
        elif self.direction == SOKOBAN.RIGHT:
            top = SOKOBAN.SPRITESIZE * 2
        elif self.direction == SOKOBAN.UP:
            top = SOKOBAN.SPRITESIZE * 3

        time.sleep(0.1)
        
        areaPlayer = pygame.Rect((0, top), (32, 32))
        window.blit(textures[SOKOBAN.PLAYER], (self.pos[0] * SOKOBAN.SPRITESIZE, self.pos[1] * SOKOBAN.SPRITESIZE), area=areaPlayer)
