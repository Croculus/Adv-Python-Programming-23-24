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
                make = bool
                if self.count < 45 or self.count > 55:
                    make = False
                    print('miss\n')
                else:
                    make = True
                    background = pygame.USEREVENT +2
                    pygame.event.post(pygame.event.Event(background))
                    update_score = pygame.USEREVENT+3
                    pygame.event.post(pygame.event.Event(update_score))
                    
                release = pygame.event.Event(pygame.USEREVENT+1, {'make': make, 'x': self.x, 'y': self.y}) #send event, notify ball to move
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
       self.image = pygame.image.load("sprites/ball.png") 
       self.image.convert_alpha()

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.x = 310
       self.y = 220
       self.count=0
       self.in_motion = False
       self.make = bool

    def update(self) -> None:
        if self.in_motion == True:
            if self.count%3 == 0: #scale down ball every three frames
                self.image = pygame.transform.smoothscale_by(self.image, 0.99)
            #self.image = pygame.transform.scale(self.image, (self.image.get_width()*(0.9999), self.image.get_height()*(0.9999)))
            self.rect = self.image.get_rect()
            self.count+=4 #count has to match x
            self.x+=4 # move by 4 because it's faster
            self.y = 270 + (0.01*(self.count)*(self.count-170))
            
            if self.count >= 170: # miss/make animation
                if self.make == True:
                    self.x-= 4 #cancels out with the other self.x for a net x of 0
                else:
                    self.y = 270 - (0.01*(self.count)*(self.count-170))
                if self.count >= 210: #reset ball
                    self.image = pygame.image.load("sprites/ball.png")
                    self.rect = self.image.get_rect()
                    self.x = 310
                    self.y = -50
                    self.in_motion = False
                    self.make = bool
            self.rect.center = [self.x, self.y]
        release= pygame.event.get(pygame.USEREVENT+1) #get for event
        if len(release) == 0: 
            return
        else: #check if event is present (will cause error otherwise)
            self.make = release[0].dict['make']
            self.count = 0 #starts frame at one
            self.in_motion = True #sets ball in motion during next frame

            self.rect.center= [self.x,self.y]
            #math for ball path
            

  
class Scoreboard(pygame.sprite.Sprite):

    def __init__(self):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self) 

       self.time = 3600 #60 * seconds
       self.score= 0
       #text prep
       self.font = pygame.font.SysFont("Arial", 15)
       self.textSurf = self.font.render('Score: {} Time: {}'.format(str(self.score), str(int(self.time/60))), 1, (0,0,0))
       self.W_text = self.textSurf.get_width()
       self.H_text = self.textSurf.get_height()

       self.width =200
       self.height = 100
       self.image = pygame.Surface([self.width, self.height])
       self.rect = self.image.fill((255,0, 0)) # Fetch the rectangle object that has the dimensions of the image
       self.rect.x = self.width/2
       self.rect.y = self.height/2
       # Update the position of this object by setting the values of rect.x and rect.y
       self.image.blit(self.textSurf, [self.width/2 - self.W_text/2, self.height/2 - self.H_text/2])
       self.rect.center = [self.rect.x, self.rect.y]
       

       
    def update(self) -> None:
        update_score = pygame.event.get(pygame.USEREVENT+3)
        if len(update_score) <= 0:
            pass
        else:
            self.score +=1
        self.time -=1 # remove a frame
        self.rect = self.image.fill((255,0, 0))
        self.textSurf = self.font.render('Score: {} Time: {}'.format(str(self.score), str(int(self.time/60))), 1, (0,0,0))
        self.image.blit(self.textSurf, [self.width/2 - self.W_text/2, self.height/2 - self.H_text/2])
        if self.time <= 0:
            endgame = pygame.USEREVENT+4
            pygame.event.post(pygame.event.Event(endgame))    