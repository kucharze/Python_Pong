import pygame

pygame.init()

# initials
Width, Height = 1000, 600
wn = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Pong_But_Better")  # The window game
run = True

# colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# ball
radius = 15
# Helps keep the ball at the exact center
ball_x, ball_y = Width/2-radius, Height/2 - radius
ball_vel_x, ball_vel_y = 0.2, 0.2

# paddle Dimensions
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = Height/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - \
    paddle_width/2, Width - (100 - paddle_width/2)
right_paddle_vel = left_paddle_vel = 0

# Main loop
while run:
    wn.fill(BLACK)  # Make the screen all black to erase the previous screen

    # Get all of the pygame events
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.9
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.9
            if i.key == pygame.K_w:
                left_paddle_vel = -0.9
            if i.key == pygame.K_s:
                left_paddle_vel = 0.9

    # print("Circle")

    # ball's movement controls
    if ball_y <= 0 + radius or ball_y >= Height - radius:
        ball_vel_y *= -1

    if ball_x <= 0 + radius or ball_x >= Width - radius:
        ball_vel_x *= -1
        ball_vel_y *= -1
        ball_x, ball_y = Width/2-radius, Height/2 - radius

    # update ball position
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)

    pygame.draw.rect(wn, RED, pygame.Rect(
        left_paddle_x, left_paddle_y, paddle_width, paddle_height))

    pygame.draw.rect(wn, RED, pygame.Rect(
        right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    # Update the display window
    pygame.display.update()

print("done")
