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
                modifier = 30 #raw number to reduce chance of making shots
                shot_percentage = (-100/(math.pow(jumpshot_peak,2)))*(math.pow(self.count-jumpshot_peak, 2))+100
                shot_percentage -= modifier
                shot_make = random.choices([True, False],cum_weights=[shot_percentage, 100])
                release = pygame.event.Event(pygame.USEREVENT+1, {'make': shot_make, 'x': self.x, 'y': self.y}) #send event, notify ball to move
                pygame.event.post(release)
                print('{},{}'.format(str(shot_percentage), str(shot_make)))
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
       self.image.convert()

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

    def update(self) -> None:
        release= pygame.event.get(pygame.USEREVENT+1) #get for event
        if len(release) == 0: #check if event is present (will cause error otherwise)
            return
        else:
            print('true')
            x = release[0].dict['x']+25
            y = release[0].dict['y']-155
            self.rect.center= [x,y]
            #math for ball path
            pass

    #be sure to override update to change animation

class Bar(pygame.sprite.Sprite):

    def __init__(self):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.image.load("backgrounds/Phyton Game Corner 2.jpg") #placeholder image
       self.image.convert()

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

    def update(self) -> None:
        pass
    #be sure to override update to change animation

class Cart(pygame.sprite.Sprite):

    def __init__(self):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.image.load("backgrounds/Phyton Game Corner 2.jpg") #placeholder image
       self.image.convert()

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

    def update(self) -> None:
        pass
    #be sure to override update to change animation