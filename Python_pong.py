import pygame
#One Time Set
pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
pressed = pygame.key.get_pressed()
done = False

#Mommentom modifier
M = -1.5

color = 0, 128, 255
color2 = 255, 100, 0

#Ball Cords
bx = 200
by = 150
bvx = -2
bvy = -1

#Player 1 Cords
Pl1_y = 80
Pl1_h = 100
Pl1_up = -3
Pl1_down = 3

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  


    #Dont know why this needs to be here?
    pressed = pygame.key.get_pressed()
#Cords
    
    #Ball
    bx += bvx
    by += bvy
    #Player 1
    Pl1_cords = 5, Pl1_y, 25, Pl1_h

#Colision
    #Ball
    if bx <= 50 and by in range(Pl1_y, Pl1_y + Pl1_h):
        bvx *= M
    if bx >= 375:
        bvx *= M
    if by <= 25:
        bvy *= M
    if by >= 275:
        bvy *= M
        
        
    #Player Colision
    if Pl1_y <= 0:
        Pl1_up = 0
    else:
        Pl1_up = -3
    if Pl1_y >= 200:
        Pl1_down = 0
    else:
        Pl1_down = 3


    
#Movment
    if pressed[pygame.K_w]: 
        Pl1_y += Pl1_up 
    if pressed[pygame.K_s]:
        Pl1_y += Pl1_down

#Reset
    if pressed[pygame.K_SPACE]:
        bx = 200
        by = 150
        bvx = -2
        bvy = -1
    

    screen.fill((0,0,0))


    pygame.draw.rect(screen, color2, pygame.Rect(Pl1_cords))
    pygame.draw.circle(screen, color, (int(bx), int(by)), 25)

    pygame.display.flip()
    clock.tick(60)
