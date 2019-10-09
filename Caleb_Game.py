import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("CALEB GAME")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png'), pygame.image.load('R10.png'), pygame.image.load('R11.png'), pygame.image.load('R12.png'), pygame.image.load('R13.png'), pygame.image.load('R14.png'), pygame.image.load('R15.png'), pygame.image.load('R16.png'), pygame.image.load('R17.png'), pygame.image.load('R18.png'), pygame.image.load('R19.png')]
walkLeft =  [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png'), pygame.image.load('R10.png'), pygame.image.load('R11.png'), pygame.image.load('R12.png'), pygame.image.load('R13.png'), pygame.image.load('R14.png'), pygame.image.load('R15.png'), pygame.image.load('R16.png'), pygame.image.load('R17.png'), pygame.image.load('R18.png'), pygame.image.load('R19.png')]
bg = pygame.image.load('BG.jpg')
char = pygame.image.load('Idle.png')

clock = pygame.time.Clock()

x = 50
y = 440
width = 60
height = 60
vel = 10

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    window.blit(bg, (0,0))

    if walkCount + 1 > 27:
        walkCount = 0

    if left:
        window.blit(walkLeft[walkCount//3], (x,y))
        walkCount +- 1
    elif right:
        window.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        window.blit(char, (x,y))

    pygame.display.update()


run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 501 - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0

    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()

pygame.QUIT()