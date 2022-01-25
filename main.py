#run > python -m pip install pygame (in python/scripts folder to install pygame module)

import pygame, sys

screen = pygame.display.set_mode((1280, 720))
player1 = pygame.Rect(50, 50, 50, 150)
player2 = pygame.Rect(1180, 50, 50, 150)
clock = pygame.time.Clock()
ballX = 610
ballY = 330
speedX = 1
speedY = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    if pygame.key.get_pressed()[pygame.K_s]:
        player1.y += 10
    if pygame.key.get_pressed()[pygame.K_w]:
        player1.y -= 10

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        player2.y += 10
    if pygame.key.get_pressed()[pygame.K_UP]:
        player2.y -= 10

    ballX += speedX
    ballY += speedY

    if ballY >= 690:
        speedY *= -1

    if ballY <= 30:
        speedY *= -1

    if ballX >= 1250:
        ballX, ballY = 610, 330
        speedX *= -1

    if ballX <= 30:
        ballX, ballY = 610, 330
        speedX *= -1

    if ballX > player1.y and ballX < player1.y + 50:
        print("fsafsa")
        #speedX *= -1

    # print(kolox)

    screen.fill((35, 35, 35))
    pygame.draw.rect(screen, (50, 50, 200), player1)
    pygame.draw.rect(screen, (50, 50, 200), player2)
    pygame.draw.circle(screen, (50, 200, 50), (ballX, ballY), 30)
    pygame.display.flip()

    clock.tick(100)