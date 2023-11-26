import pygame, random, math

#jumpshot is a parabola; a(x-h)^2 +k
jumpshot_dur = 180 # length/k value
jumpshot_peak = jumpshot_dur/2 #vertex/ h value
jumpshot_a = (-1*jumpshot_dur)/math.pow(jumpshot_peak, 2) #a value required to start from original position
class Player(pygame.sprite.Sprite):

    def __init__(self):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self) #start at 240, 365
       
       self.image = pygame.image.load("sprites/Character1.png") 

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.x = 240 #initial x
       self.y = 365 #initial y
       self.rect.center = [self.x, self.y]

       self.count = 0 #count of frames in which space is pressed
       self.score= 0

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.count == 0:
                self.image = pygame.image.load("sprites/Character2.png")
                self.rect = self.image.get_rect()
            self.count+=1
            self.y = 365 - ((jumpshot_a*math.pow(self.count-jumpshot_peak, 2))+jumpshot_dur) # inital y - parabola function, lower value = going up
            
            
            self.rect.center = [self.x,self.y]
            
        elif self.count > 0:
            shot_percentage = (-100/(math.pow(jumpshot_peak,2)))*(math.pow(self.count-jumpshot_peak))+100
            shot_make = random.choices([True, False],cum_weights=[shot_percentage, 100])
            release = pygame.event.Event(pygame.USEREVENT+1, {'make': shot_make}) #send event, notify ball to move
            pygame.event.post(release)
            #keep 
        pass
    #be sure to override update to change animation

class Ball(pygame.sprite.Sprite):

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
        release= pygame.event.get(pygame.USEREVENT+1) #check for event
        if release[0].__getattribute__('make') == True:
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