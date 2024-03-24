MAPWIDTH    = 25
MAPHEIGHT   = 15
SPRITESIZE  = 32

WINDOW_WIDTH  = 1024
WINDOW_HEIGHT = 768

# Blocks
AIR             = 0
WALL            = 1
PLAYER          = 2
BOX             = 3
TARGET          = 4
TARGET_FILLED   = 5

UP      = 100
DOWN    = 101
LEFT    = 102
RIGHT   = 103

# Colors
WHITE           = (255,255,255)
BLACK           = (0,0,0)
BLUE            = (0,0,150)
GREY            = (200,200,200)

# Control 
REPEAT_PARAM = 250 # to fixbug press keyboard 
ALGO = 'bfs' #' the algorithm that used 
MAX_CNT_PROCESS = 1e7 # maxinum number of states that be processed, to avoid program too long run
NEED = False # if True: run execuable-blocks in game.py, else not  
