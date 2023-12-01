# screen dimensions
TILE_SIZE = 200
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# fence dimensions
FENCE_WIDTH = int(800/10)
FENCE_HEIGHT = int(494/10)
FENCE_OPENING_WIDTH = 400

# fence height + 1 because don't want to trigger collide with fence
FENCE_OPENING_HEIGHT = FENCE_HEIGHT + 1
FENCE_Y_POS = SCREEN_HEIGHT - FENCE_HEIGHT - 10

# turkey starting position
TURKEY_START_X = SCREEN_WIDTH/2
TURKEY_START_Y = 100

# cow dimensions
COW_WIDTH = int(7510/100)
COW_HEIGHT = int(4240/100)

# speeds are in pixels per frame and frame rate is 1/60 seconds
TURKEY_SPEED = 3
COW_SPEED_MIN = 0.5
COW_SPEED_MAX = 3



