# screen dimensions
TILE_SIZE = 200
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# turkey starting position + dim
TURKEY_START_X = SCREEN_WIDTH/2
TURKEY_START_Y = 100
TURKEY_WIDTH = int(845/13)
TURKEY_HEIGHT = int(873/13)

# fence dimensions
FENCE_WIDTH = int(800/10)
FENCE_HEIGHT = int(494/10)
FENCE_Y_POS = SCREEN_HEIGHT - FENCE_HEIGHT - 10

FENCE_OPENING_WIDTH = TURKEY_WIDTH + 5
FENCE_OPENING_HEIGHT = FENCE_HEIGHT + 1

#heart dimensions
HEART_SIZE = int(512/10)
#hole dimenstions
HOLE_WIDTH = int(540/10)
HOLE_HEIGHT = int(360/10)


# cow dimensions
COW_WIDTH = int(7510/90)
COW_HEIGHT = int(4240/90)

# speeds are in pixels per frame and frame rate is 1/60 seconds
TURKEY_SPEED = 1
COW_SPEED_MIN = .5
COW_SPEED_MAX = 2

NUM_LIVES = 3


