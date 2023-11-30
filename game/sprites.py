import pygame, random, math, time


#jumpshot is a parabola; a(x-h)^2 +k
jumpshot_dur = 100 # vertex y /k value
jumpshot_peak = jumpshot_dur/2 #vertex x / h value
jumpshot_a = (-1*jumpshot_dur)/math.pow(jumpshot_peak, 2) #a value required to start from original position

class Player(pygame.sprite.Sprite):

    def __init__(self):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self) #start at 240, 365
       
       self.image = pygame.image.load("sprites/Character1.png") 

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.x = 285 #initial x
       self.y = 515 #initial y

       self.count = 0 #count of frames in which space is pressed
       self.score= 0
       self.rect.center = [self.x, self.y]
       self.sent_data = False #boolean to check wheter shot data is sent

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        #print("{},{}".format(str(self.count), str(keys[pygame.K_SPACE])))
        if keys[pygame.K_SPACE]:
            if self.count == 0:
                self.image = pygame.image.load("sprites/Character2.png")
                self.rect = self.image.get_rect()
            if self.count < 100:
             self.count+=1
            self.y = 495 - ((jumpshot_a*math.pow(self.count-jumpshot_peak, 2))+jumpshot_dur) # inital y - parabola function, lower value = going up
            
            
            self.rect.center = [self.x,self.y]
        
        
        elif self.count > 1:
            #release data
            if self.sent_data == False: # checks if data has been sent then quits
                 #raw number to reduce chance of making shots
                if self.count < 45 or self.count > 55:
                    release = pygame.event.Event(pygame.USEREVENT+1, {'make': False, 'x': self.x, 'y': self.y}) #send event, notify ball to move
                    print(self.count)
                    print('miss\n')
                else:
                    release = pygame.event.Event(pygame.USEREVENT+1, {'make': True, 'x': self.x, 'y': self.y})
                    background = pygame.USEREVENT +2
                    pygame.event.post(pygame.event.Event(background))
                    print('make')
                pygame.event.post(release)
                self.sent_data = True

            #release animation
            self.count += 1

            self.image = pygame.image.load("sprites/Character3.png")
            self.rect = self.image.get_rect()
            self.y = 495 - ((jumpshot_a*math.pow(self.count-jumpshot_peak, 2))+jumpshot_dur)
            self.rect.center = [self.x, self.y]
            


            #reset for next shot
            if self.y >= 495:
                self.image = pygame.image.load("sprites/Character1.png")
                self.rect = self.image.get_rect()
                self.y = 515
                self.count = 0
                self.rect.center = [self.x,self.y]
                self.sent_data = False
        


class Ball(pygame.sprite.Sprite):

    def __init__(self):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.image.load("sprites/ball.png") #placeholder image
       self.image.convert_alpha()

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.x = 310
       self.y = 200
       self.count=1
       self.in_motion = False

    def update(self) -> None:
        if self.in_motion == True:
            if self.count%3 == 0:
                self.image = pygame.transform.smoothscale_by(self.image, 0.99)
            #self.image = pygame.transform.scale(self.image, (self.image.get_width()*(0.9999), self.image.get_height()*(0.9999)))
            self.rect = self.image.get_rect()
            self.count+=4
            self.x+=4
            self.y = 270 + (0.01*(self.count)*(self.count-170))
            self.rect.center = [self.x, self.y]
            if self.count >= 170: # reset
                self.image = pygame.image.load("sprites/ball.png")
                self.rect = self.image.get_rect()
                self.x = 310
                self.y = 200
                self.in_motion = False

        release= pygame.event.get(pygame.USEREVENT+1) #get for event
        if len(release) == 0: #check if event is present (will cause error otherwise)
            return
        else:
            self.count = 1
            self.in_motion = True

            self.rect.center= [self.x,self.y]
            #math for ball path
            pass

    #be sure to override update to change animation

