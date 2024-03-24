import pygame
import sys
from pygame.locals import *
import constants as SOKOBAN
from level import *
from player import *
from scores import *
from player_interface import *
from solver import *
from pyautogui import press, typewrite, hotkey

import _thread
import time
def move( threadName, delay, strategy):
    for step in strategy:
        if step in ['R','r']:
            press('right')
        if step in ['L','l']:
            press('left')
        if step in ['D','d']:
            press('down')
        if step in ['U','u']:
            press('up')
        # time.sleep(0.2)
class Game:
    #!!!
    INDEX_LEVEL = 1 # static attribute to select 'level' for game  
    def __init__(self, window):
        self.window = window
        self.load_textures()
        self.player = None
        self.index_level = Game.INDEX_LEVEL 
        self.load_level()
        self.play = True
        self.scores = Scores(self)
        self.player_interface = PlayerInterface(self.player, self.level)

    def load_textures(self):
       self.textures = {
           SOKOBAN.WALL: pygame.image.load('assets/images/wall.png').convert_alpha(),
           SOKOBAN.BOX: pygame.image.load('assets/images/box.png').convert_alpha(),
           SOKOBAN.TARGET: pygame.image.load('assets/images/target.png').convert_alpha(),
           SOKOBAN.TARGET_FILLED: pygame.image.load('assets/images/valid_box.png').convert_alpha(),
           SOKOBAN.PLAYER: pygame.image.load('assets/images/player_sprites.png').convert_alpha()
       }

    def load_level(self):
        self.level = Level(self.index_level)
        self.board = pygame.Surface((self.level.width, self.level.height))
        if self.player:
            self.player.pos = self.level.position_player
            self.player_interface.level = self.level
        else:
            self.player = Player(self.level)

    def start(self):
        while self.play:
            #self.process_event(pygame.event.wait())
            self.process_event(pygame.event.wait())
            self.update_screen()

    def process_event(self, event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                # Quit game
                self.play = False
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT, K_z, K_s, K_q, K_d]:
                # Move players
                self.player.move(event.key, self.level, self.player_interface)
                if self.has_win():
                    self.index_level += 1
                    if (self.index_level == 17):
                        self.index_level = 1
                    self.scores.save()
                    self.load_level()
            if event.key == K_r:
                # Restart current level
                self.load_level()
            if event.key == K_l:
                # Cancel last move
                self.level.cancel_last_move(self.player, self.player_interface)
        if event.type == MOUSEBUTTONUP:
            self.player_interface.click(event.pos, self.level, self)
        if event.type == MOUSEMOTION:
            self.player_interface.mouse_pos = event.pos

    def update_screen(self):
        pygame.draw.rect(self.board, SOKOBAN.WHITE, (0,0, self.level.width * SOKOBAN.SPRITESIZE, self.level.height * SOKOBAN.SPRITESIZE))
        pygame.draw.rect(self.window, SOKOBAN.WHITE, (0,0,SOKOBAN.WINDOW_WIDTH,SOKOBAN.WINDOW_HEIGHT))

        self.level.render(self.board, self.textures)
        self.player.render(self.board, self.textures)

        pox_x_board = (SOKOBAN.WINDOW_WIDTH / 2) - (self.board.get_width() / 2)
        pos_y_board = (SOKOBAN.WINDOW_HEIGHT / 2) - (self.board.get_height() / 2)
        self.window.blit(self.board, (pox_x_board, pos_y_board))

        self.player_interface.render(self.window, self.index_level)

        pygame.display.flip()

    def has_win(self):
        nb_missing_target = 0
        for y in range(len(self.level.structure)):
            for x in range(len(self.level.structure[y])):
                if self.level.structure[y][x] == SOKOBAN.TARGET:
                    nb_missing_target += 1

        return nb_missing_target == 0

    #!!!
    #:: some printed messege to log 
    def mesVerbose(self, verboseMes, func_dir=""): 
        print("__verbose__:", str(func_dir), verboseMes) 
    def mesWarning(self, verWarning, func_dir=""): 
        print("__warning__:", str(func_dir), verWarning + "!!!") 
    LOCK_FLAG = False #:: static atribute to synchronized
    PRESS_FALG = True #:: static atribute that decide it is need to press keyboard 
    
    def auto_move(self):
        #* 'get_move' from 'solver.py'
        if(Game.LOCK_FLAG == True): return self.mesWarning("there is a algorithm that running") 
        else: Game.LOCK_FLAG = True 
        
        self.mesVerbose("algorithm is begin", "game.py > GameClass > auto_move")
        self.mesVerbose("level is {}".format(Game.INDEX_LEVEL))
        #:: select algorithm for searching 
        strategy, IS_WIN, CNT_PROCESS = get_move(self.level.structure[:-1], 
                                            self.level.position_player, SOKOBAN.ALGO)
        # strategy = get_move(self.level.structure[:-1], self.level.position_player, 'bfs')
        # strategy = get_move(self.level.structure[:-1], self.level.position_player, 'ucs')
        #:: I think I not need use print file 
        # with open("assets/sokobanSolver/Solverlevel_" + str(self.index_level) + ".txt", 'w+') as solver_file:
        #     for listitem in strategy:
        #         solver_file.write('%s, ' % listitem)
        self.mesVerbose("algorithm is FINISH", "game.py > GameClass > auto_move:")
        self.mesVerbose("number of move is {}".format(len(strategy)), "game.py > GameClass > auto_move:")
        if(IS_WIN): self.mesVerbose("you win")
        else: self.mesVerbose("sorry, you not win")
        self.mesVerbose("{} cnt_process_unit".format(CNT_PROCESS))
        
        #:: if True, perform press keyboard (if need) 
        if Game.PRESS_FALG and strategy is not None:
            try:
                _thread.start_new_thread( move, ("Thread-1", 2, strategy) )
            except:
                print ("Error: unable to start thread")
        Game.LOCK_FLAG = False 
        #* synchronized
# Define a function for the thread

#!!!
#:: This is a execuable block that be build to run programs not need graphic 
if(SOKOBAN.NEED): 
    Game.PRESS_FALG = False 
    pygame.init()
    pygame.key.set_repeat(SOKOBAN.REPEAT_PARAM, 100)
    pygame.display.set_caption("Sokoban Game")
    window = pygame.display.set_mode((SOKOBAN.WINDOW_WIDTH, SOKOBAN.WINDOW_HEIGHT))

    for t in range(0, 3): 
        if(t == 0): 
            SOKOBAN.ALGO = 'dfs'
        if(t == 1): 
            SOKOBAN.ALGO = 'bfs'
        if(t == 2):
            SOKOBAN.ALGO = 'ucs'
            
        for i in range(17, 18): 
            if(t == 0 and i == 4): continue 
            
            Game.INDEX_LEVEL = i+1 
            sokoban = Game(window)
            sokoban.auto_move() 
    
# pygame.draw.rect(window, SOKOBAN.WHITE, (0,0,SOKOBAN.WINDOW_WIDTH,SOKOBAN.WINDOW_HEIGHT))
# # menu.render(window)
# pygame.display.flip()

# pygame.quit()