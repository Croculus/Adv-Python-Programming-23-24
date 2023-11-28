import pygame, sprites



#initialization
pygame.init()
screen_width = 950
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
game_state = "start_menu"

clock = pygame.time.Clock()
FPS = 60
player = sprites.Player()

def draw_start_menu():
    screen.fill((0, 255, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('My Game', True, (255, 255, 255))
    start_button = font.render('Start (with y)', True, (255, 255, 255))
    screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/2))
    screen.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/2 + start_button.get_height()/2))
    pygame.display.update()

player = sprites.Player()
ball = sprites.Ball()
player_group = pygame.sprite.Group()
player_group.add(player)
player_group.add(ball)
while True: 
   clock.tick(FPS)
   for event in pygame.event.get(): 
       if event.type == pygame.QUIT:
           pygame.quit()
           quit()
   if game_state == "start_menu":
       draw_start_menu()
       keys = pygame.key.get_pressed()
       if keys[pygame.K_y]:
            game_state = "game"
            game_over = False
   if game_state == "game":
        
        
        
        background = pygame.image.load("backgrounds/Phyton Game Corner 2.jpg")
        screen.blit(background, (0, 0)) 
        player_group.update()
        player_group.draw(screen)
        #print(pygame.mouse.get_pos())
        pygame.display.update()
        pygame.event.pump()
        
            
   #print(pygame.mouse.get_pos()) 250 425
