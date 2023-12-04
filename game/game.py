import pygame, sprites


#pygame.init()


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
    screen.fill((0, 0, 0))
    start = pygame.image.load("backgrounds/Game Logo.jpg")
    screen.blit(start, (0,0))
    pygame.display.update()

player = sprites.Player()
ball = sprites.Ball()
scoreboard = sprites.Scoreboard()
player_group = pygame.sprite.Group()
player_group.add(player)
player_group.add(ball)
player_group.add(scoreboard)
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
        if event.type == pygame.USEREVENT+2:
            background = pygame.image.load("backgrounds/Green Corner 2.png")
        else:
            background = pygame.image.load("backgrounds/Phyton Game Corner 2.jpg")
        if event.type == pygame.USEREVENT+4:
            game_state = 'endgame'
        screen.blit(background, (0, 0)) 
        player_group.update()
        player_group.draw(screen)
        #print(pygame.mouse.get_pos())
        pygame.display.update()   
        pygame.event.pump()
   if game_state == 'endgame':
       pygame.quit()
       quit()
        
            
   #print(pygame.mouse.get_pos()) 480, 270
