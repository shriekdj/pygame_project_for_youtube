import pygame


pygame.init()

screen = pygame.display.set_mode(
    (1280, 720) # 720p Screen
)
clock = pygame.time.Clock()

# global variables
running = True
fps = 60 # cap all frames to 60
dt = 0 # frames speed

# player vars that's gonna update everytime
player_pos = pygame.Vector2(
    (screen.get_width() / 2,screen.get_height() / 2)
) # center of the screen point type in a tuple
player_dir = pygame.Vector2(
    0,0
) # no tuple because it's stores direction

player_speed = 300 # pixels per seconds

while running:
    # Let's Listen Global Window Events
    for event in pygame.event.get():
        # window x is clicked
        if event.type == pygame.QUIT:
            running = False

    screen.fill('purple')

    # Game Code Start

    ## draw player
    pygame.draw.circle(
        screen, # background
        'red',
        player_pos,
        radius=90 # pixels
    )

    # normal keyboard click events
    keys = pygame.key.get_pressed()

    # reset the direction
    player_dir.x, player_dir.y = 0,0

    if keys[pygame.K_LEFT]:
        player_dir.x = -1
    if keys[pygame.K_RIGHT]:
        player_dir.x = 1
    if keys[pygame.K_UP]:
        player_dir.y = -1
    if keys[pygame.K_DOWN]:
        player_dir.y = 1

    if player_dir.magnitude_squared() > 0:
        player_dir = player_dir.normalize() # unitless

    player_pos += player_speed * player_dir * dt

    if keys[pygame.K_ESCAPE]:
        running = False

    # Game Code End

    pygame.display.flip()

    dt = clock.tick(fps) / 1000 # return frames per seconds

pygame.quit()
