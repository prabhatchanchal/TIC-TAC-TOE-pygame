
import pygame
import random
def template():
    WIDTH = 600
    HEIGHT = 600
    FPS = 30

    # define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BGCOLOR=(247,10,10)
    bg = pygame.image.load("bg.png")
    val=0
    #images
    Xshape=pygame.transform.scale((pygame.image.load("Xshape.jpg")), (WIDTH //3 , HEIGHT //3)) 
    Oshape=pygame.transform.scale((pygame.image.load("Oshape.jpg")), (WIDTH //3 , HEIGHT //3)) 

    # initialize pygame and create window
#<---------------------------------------------------------------------------------------->

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("tick tac toe")
    clock = pygame.time.Clock()
    running = True
    #  KEYS FOR SHAPES
    First=False
    second=False
    third=False
    fouth=False
    fifth=False
    sixth=False
    seventh=False
    eight=False
    ninth=False

    #KEYS FOR SHOW SHAPE
#<---------------------------------------------------------------------------------------->

    #Cirlces
    FirstO=False
    secondO=False
    thirdO=False
    fouthO=False
    fifthO=False
    sixthO=False
    seventhO=False
    eightO=False
    ninthO=False
    #CROSS
    FirstX=False
    secondX=False
    thirdX=False
    fouthX=False
    fifthX=False
    sixthX=False
    seventhX=False
    eightX=False
    ninthX=False
#<---------------------------------------------------------------------------------------->


    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            keys=pygame.key.get_pressed()
        #BACKGROUND
        #INSIDE OF THE GAME LOOP
        screen.blit(bg, (0, 0))
        #screen.blit(Xshape, (0, 0),(0,0,WIDTH//3,WIDTH//3))
        #screen.blit(Xshape, (WIDTH//3,HEIGHT//3),(0,0,WIDTH//3,WIDTH//3))



        #GRIDLINES
        for i in range(0,HEIGHT,HEIGHT//3):
            pygame.draw.line(screen,BGCOLOR,[0,i],[WIDTH,i],1)
        for j in range(0,WIDTH,WIDTH//3):
            pygame.draw.line(screen,BGCOLOR,[j,0],[j,HEIGHT],2)


        #LOCATION DETECTION ON SCREEN
#<---------------------------------------------------------------------------------------->

        if event.type==pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            if pos[0]>0 and pos[0]<(WIDTH//3) and pos[1]>0 and pos[1]<(HEIGHT//3):
                pygame.draw.rect(screen, BLUE, (0,0,WIDTH//3,HEIGHT//3),2)
                First=True
            elif pos[0]>(WIDTH//3) and pos[0]<(2*WIDTH//3) and pos[1]>0 and pos[1]<(HEIGHT//3):
                pygame.draw.rect(screen, BLUE, (WIDTH//3,0,WIDTH//3,HEIGHT//3),2)
                second=True

            elif pos[0]>(2*WIDTH//3) and pos[0]<(WIDTH) and pos[1]>0 and pos[1]<(HEIGHT//3):
                pygame.draw.rect(screen, BLUE, ((2*WIDTH)//3,0,WIDTH//3,HEIGHT//3),2)
                third=True

            elif pos[0]>0 and pos[0]<(WIDTH//3) and pos[1]>HEIGHT//3 and pos[1]<(2*HEIGHT//3):
                pygame.draw.rect(screen, BLUE, (0,HEIGHT//3,WIDTH//3,HEIGHT//3),2)
                fouth=True

            elif pos[0]>WIDTH//3 and pos[0]<(2*WIDTH//3) and pos[1]>HEIGHT//3 and pos[1]<(2*HEIGHT//3):
                pygame.draw.rect(screen, BLUE, (WIDTH//3,HEIGHT//3,WIDTH//3,HEIGHT//3),2)
                fifth=True

            elif pos[0]>(2*WIDTH//3) and pos[0]<(WIDTH) and pos[1]>HEIGHT//3 and pos[1]<(2*HEIGHT//3):
                pygame.draw.rect(screen, BLUE, (2*WIDTH//3,HEIGHT//3,WIDTH//3,HEIGHT//3),2)
                sixth=True

            elif pos[0]>0 and pos[0]<(WIDTH//3) and pos[1]>2*HEIGHT//3 and pos[1]<(3*HEIGHT//3):
                pygame.draw.rect(screen, BLUE, (0,2*HEIGHT//3,WIDTH//3,HEIGHT//3),2)
                seventh=True

            elif pos[0]>WIDTH//3 and pos[0]<(2*WIDTH//3) and pos[1]>2*HEIGHT//3 and pos[1]<(3*HEIGHT//3):
                pygame.draw.rect(screen, BLUE, (WIDTH//3,2*HEIGHT//3,WIDTH//3,HEIGHT//3),2)
                eight=True

            elif pos[0]>(2*WIDTH//3) and pos[0]<(WIDTH) and pos[1]>2*HEIGHT//3 and pos[1]<(3*HEIGHT//3):
                pygame.draw.rect(screen, BLUE, (2*WIDTH//3,2*HEIGHT//3,WIDTH//3,HEIGHT//3),2)
                ninth=True

        #O R X PUTTING ON SELECTED SECTION
#<---------------------------------------------------------------------------------------->

        if First and keys[pygame.K_0]:
            FirstO=True
        if second and keys[pygame.K_0]:
            secondO=True
        if third and keys[pygame.K_0]:
            thirdO=True
        if fouth and keys[pygame.K_0]:
            fouthO=True
        if fifth and keys[pygame.K_0]:
            fifthO=True
        if sixth and keys[pygame.K_0]:
            sixthO=True
        if seventh and keys[pygame.K_0]:
            seventhO=True
        if eight and keys[pygame.K_0]:
            eightO=True
        if ninth and keys[pygame.K_0]:
            ninthO=True
#  CROSS TRIGGERING
        if First and keys[pygame.K_x]:
            FirstX=True
        if second and keys[pygame.K_x]:
            secondX=True
        if third and keys[pygame.K_x]:
            thirdX=True
        if fouth and keys[pygame.K_x]:
            fouthX=True
        if fifth and keys[pygame.K_x]:
            fifthX=True
        if sixth and keys[pygame.K_x]:
            sixthX=True
        if seventh and keys[pygame.K_x]:
            seventhX=True
        if eight and keys[pygame.K_x]:
            eightX=True
        if ninth and keys[pygame.K_x]:
            ninthX=True


            #PERMANENT DRAW ON SCREEN

#                   CIRCLE
#<---------------------------------------------------------------------------------------->
        if FirstO:
            screen.blit(Oshape, (0, 0),(0,0,WIDTH//3,WIDTH//3))
        if secondO:
            screen.blit(Oshape, (WIDTH//3, 0),(0,0,WIDTH//3,WIDTH//3))
        if thirdO:
            screen.blit(Oshape, (2*WIDTH//3, 0),(0,0,WIDTH//3,WIDTH//3))
        if fouthO:
            screen.blit(Oshape, (0, HEIGHT//3),(0,0,WIDTH//3,WIDTH//3))
        if fifthO:
            screen.blit(Oshape, (WIDTH//3,HEIGHT//3 ),(0,0,WIDTH//3,WIDTH//3))
        if sixthO:
            screen.blit(Oshape, (2*WIDTH//3, HEIGHT//3),(0,0,WIDTH//3,WIDTH//3))
        if seventhO:
            screen.blit(Oshape, (0, 2*HEIGHT//3),(0,0,WIDTH//3,WIDTH//3))
        if eightO:
            screen.blit(Oshape, (WIDTH//3, 2*HEIGHT//3),(0,0,WIDTH//3,WIDTH//3))
        if ninthO:
            screen.blit(Oshape, (2*WIDTH//3, 2*HEIGHT//3),(0,0,WIDTH//3,WIDTH//3))


#                               CROSS
#<---------------------------------------------------------------------------------------->
        if FirstX:
            screen.blit(Xshape, (0, 0),(0,0,WIDTH//3,WIDTH//3))
        if secondX:
            screen.blit(Xshape, (WIDTH//3, 0),(0,0,WIDTH//3,WIDTH//3))
        if thirdX:
            screen.blit(Xshape, (2*WIDTH//3, 0),(0,0,WIDTH//3,WIDTH//3))
        if fouthX:
            screen.blit(Xshape, (0, HEIGHT//3),(0,0,WIDTH//3,WIDTH//3))
        if fifthX:
            screen.blit(Xshape, (WIDTH//3,HEIGHT//3 ),(0,0,WIDTH//3,WIDTH//3))
        if sixthX:
            screen.blit(Xshape, (2*WIDTH//3, HEIGHT//3),(0,0,WIDTH//3,WIDTH//3))
        if seventhX:
            screen.blit(Xshape, (0, 2*HEIGHT//3),(0,0,WIDTH//3,WIDTH//3))
        if eightX:
            screen.blit(Xshape, (WIDTH//3, 2*HEIGHT//3),(0,0,WIDTH//3,WIDTH//3))
        if ninthX:
            screen.blit(Xshape, (2*WIDTH//3, 2*HEIGHT//3),(0,0,WIDTH//3,WIDTH//3))




        pygame.display.flip()

    pygame.quit()
template()
