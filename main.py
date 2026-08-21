import pygame


pygame.init()

screen = pygame.display.set_mode(
    (1280, 720) # 720p Screen
)
screen_rect = screen.get_rect()

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

player_radius = 90
player_speed = 300 # pixels per seconds

player_surface = pygame.Surface(
    (player_radius*2, player_radius*2), # 180x180
    pygame.SRCALPHA # surface will be transparent
)
pygame.draw.circle(
    player_surface, # background
    'red',
    (player_radius, player_radius), # center of surface
    radius=player_radius # pixels
)
player_rect = player_surface.get_rect() # reference

while running:
    # Let's Listen Global Window Events
    for event in pygame.event.get():
        # window x is clicked
        if event.type == pygame.QUIT:
            running = False

    screen.fill('purple')

    # Game Code Start

    ## draw player_surface on screen like sticky notes
    screen.blit(
        player_surface, player_rect
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

    player_rect.center = (
        player_pos.x,
        player_pos.y
    ) # change position of center of rect

    # does not allow to go outside of boundary rect passed
    player_rect.clamp_ip(
        screen_rect
    )

    player_pos.update(
        player_rect.center
    )


    if keys[pygame.K_ESCAPE]:
        running = False

    # Game Code End

    pygame.display.flip()

    dt = clock.tick(fps) / 1000 # return frames per seconds

pygame.quit()
