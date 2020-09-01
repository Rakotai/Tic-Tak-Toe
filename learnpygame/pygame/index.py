import pygame, sys
pygame.init()
clock = pygame.time.Clock()
# caption
pygame.display.set_caption('Tic Tak Toe')

x=250
y=250
width = 1050
height = 600
speed = 10
color_black = (0,0,0)
color_light_grey = (200,200,200)
bg_color = pygame.Color('grey12')
# screen 
screen = pygame.display.set_mode((width, height))

# objects add:      #left           # top        #width & height 
box = pygame.Rect((width/2 - 100, height/2 - 100), (200, 200))
# main loop --> event   
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
            run = False
    # draw  
    keyPressed = pygame.key.get_pressed()          
    if keyPressed[pygame.K_w] and box.y > 0:
        box.y -= speed
    if keyPressed[pygame.K_s] and box.y < 400:
        box.y += speed
    if keyPressed[pygame.K_a] and box.x > 0:
        box.x -= speed
    if keyPressed[pygame.K_d] and box.x < 850:
        box.x += speed
    # make a jump thing.

    screen.fill(bg_color)
    pygame.draw.rect(screen, color_light_grey, box)

    pygame.display.flip() # or flip()
    clock.tick(60)