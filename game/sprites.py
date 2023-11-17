import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self) #start at 240, 365
       self.frame = 1  #1, 2, or 3
       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.image.load("sprites/Character1.png") 
       self.image.convert()

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

    def update(self) -> None:
        self.image = pygame.image.load("sprites/Character{}.png".format(self.frame))
        self.frame += 1
        if self.frame > 3:
            self.frame %= 3
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