import pygame, sys

screen = pygame.display.set_mode((1280,720))
gracz1 = pygame.Rect(50,50,50,150)
gracz2 = pygame.Rect(1180,50,50,150)
clock = pygame.time.Clock()
kolox = 610
koloy = 330
speedx = 1
speedy = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    if pygame.key.get_pressed()[pygame.K_s]:
        gracz1.y += 10
    if pygame.key.get_pressed()[pygame.K_w]:
        gracz1.y -= 10

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        gracz2.y += 10
    if pygame.key.get_pressed()[pygame.K_UP]:
        gracz2.y -= 10

    kolox += speedx
    koloy += speedy

    if koloy >= 690:
        speedy *= -1

    if koloy <= 30:
        speedy *= -1

    if kolox >= 1250:
        kolox, koloy = 610, 330
        speedx *= -1

    if kolox <= 30:
        kolox, koloy = 610, 330
        speedx *= -1

    if kolox > gracz1.y and kolox < gracz1.y + 50:
        print("fsafsa")
        #speedx *= -1

    # print(kolox)

    screen.fill((35,35,35))
    pygame.draw.rect(screen, (50,50,200), gracz1)
    pygame.draw.rect(screen, (50, 50, 200), gracz2)
    pygame.draw.circle(screen, (50,200,50), (kolox, koloy), 30)
    pygame.display.flip()

    clock.tick(60)