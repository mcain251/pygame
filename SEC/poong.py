import pygame
from random import randint

pygame.init()
clock = pygame.time.Clock()
original_FPS = 20
max_FPS = 60
FPS = original_FPS
max_score = 5

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
gray = (244, 244, 244)
dark_gray = (200, 200, 200)
darker_gray = (100, 100, 100)

display_width = 700
display_height = 400

directions = [10, -10]

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Poong")

gameExit = False

lead_x = display_width/2 - 5
lead_y = display_height/2 - 5
lead_x_change = 0
lead_y_change = 0
ballExists = False

paddle_length = 50
left_y = display_height/2 - paddle_length/2 - 5
right_y = display_height/2 - paddle_length/2 - 5
left_change = 0
right_change = 0

delay = original_FPS

red_score = 0
blue_score = 0

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                right_change = -10
            elif event.key == pygame.K_DOWN:
                right_change = 10
            if event.key == pygame.K_w:
                left_change = -10
            elif event.key == pygame.K_s:
                left_change = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                right_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                left_change = 0

    if red_score >= max_score or blue_score >= max_score:
        gameExit = True

    if not ballExists:
        FPS = original_FPS
        if (delay == FPS):
            lead_y = randint(5, (display_height/10)*10 - 5) - 5
            lead_x = display_width/2 - 5
        if (delay > 0):
            lead_x_change = 0
            lead_y_change = 0
            delay -= 1
        else:
            lead_x_change = directions[randint(0,1)]
            lead_y_change = directions[randint(0,1)]
            ballExists = True


    lead_x += lead_x_change
    lead_y += lead_y_change
    if lead_y <= 0 or lead_y >= display_height - 10:
        lead_y_change = (-1)*lead_y_change
        if lead_y < 0:
            lead_y = 0
        elif lead_y > display_height - 10:
            lead_y = display_height - 10
    if lead_x <= 0:
        ballExists = False
        blue_score += 1
        delay = original_FPS
    if lead_x >= display_width - 10:
        ballExists = False
        red_score += 1
        delay = original_FPS

    if not right_y + right_change < 0 and not right_y + right_change > (display_height - paddle_length):
        right_y += right_change
    if not left_y + left_change < 0 and not left_y + left_change > (display_height - paddle_length):
        left_y += left_change

    if lead_x == 15 and lead_y >= left_y and lead_y <= left_y + paddle_length - 10:
        lead_x_change = (-1) * lead_x_change
        if FPS < max_FPS:
            FPS += 2
    if lead_x == display_width - 25 and lead_y >= right_y and lead_y <= right_y + paddle_length - 10:
        lead_x_change = (-1) * lead_x_change
        if FPS < max_FPS:
            FPS += 2

    gameDisplay.fill(gray)
    pygame.draw.rect(gameDisplay, dark_gray, [display_width/2 - 5, 0, 10, display_height])

    pygame.draw.rect(gameDisplay, darker_gray, [lead_x, lead_y, 10, 10])
    pygame.draw.rect(gameDisplay, red, [10, left_y, 5, paddle_length])
    pygame.draw.rect(gameDisplay, blue, [display_width - 15, right_y, 5, paddle_length])

    i = 0
    while i < red_score:
        pygame.draw.rect(gameDisplay, red, [2, 5 + 10*i, 5, 5])
        i += 1
    i = 0
    while i < blue_score:
        pygame.draw.rect(gameDisplay, blue, [display_width - 7, 5 + 10*i, 5, 5])
        i += 1

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
if red_score >= max_score:
    print "Red wins!"
elif blue_score >= max_score:
    print "Blue wins!"

quit()
