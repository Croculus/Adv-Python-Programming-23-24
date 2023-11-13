import pygame, sprites




pygame.init()
screen_width = 750
screen_height = 450
screen = pygame.display.set_mode((screen_width, screen_height))
game_state = "start_menu"

player = sprites.Player()
background = pygame.image.load("backgrounds/Phyton Game Corner.jpg")

def draw_start_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('My Game', True, (255, 255, 255))
    start_button = font.render('Start', True, (255, 255, 255))
    screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/2))
    screen.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/2 + start_button.get_height()/2))
    pygame.display.update()

#rough psudocode
def shoot():
    #frames to show player grabbing ball, going back to shooting position
    #subtract 1 from rack
    # pick a spot on the bar as the "hotspot"
    # while key is pressed player jumps and bar moves
    # if key is held for too long automatically jump
    # player move down
    # check deviation from hotspot, calculate %change of going in and determine whether to score
    # ball moves through air
    # if ball is made, show path to going in to hoop
    # else then generate a random number to offset ball path
    # reset bar
    # if rack is empty, change rack
    pass

while True: 

   for event in pygame.event.get(): 
       if event.type == pygame.QUIT:
           pygame.quit()
           quit()

   if game_state == "start_menu":
       draw_start_menu()
        
