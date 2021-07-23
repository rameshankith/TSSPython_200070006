import pygame, sys, time, random

#initial game variables

# Window size
frame_size_x = 720
frame_size_y = 480

#Parameters for Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
direction = 'RIGHT'
change_to = direction

#Parameters for food
food_pos = [80,80]
food_spawn = False

score = 0


# Initialise game window
pygame.init()
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))



# FPS (frames per second) controller to set the speed of the game
fps_controller = pygame.time.Clock()




def check_for_events():
    """
    This should contain the main for loop (listening for events). You should close the program when
    someone closes the window, update the direction attribute after input from users. You will have to make sure
    snake cannot reverse the direction i.e. if it turned left it cannot move right next.
    """
    global direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        elif event.type==pygame.KEYDOWN:                                     #finding the direction of movement
            if direction=='RIGHT':
                if event.key==pygame.K_RIGHT:
                    direction='DOWN'
                elif event.key==pygame.K_LEFT:
                    direction='UP'
            elif direction=='LEFT':
                if event.key==pygame.K_RIGHT:
                    direction='UP'
                elif event.key==pygame.K_LEFT:
                    direction='DOWN'
            elif direction=='UP':
                if event.key==pygame.K_RIGHT:
                    direction='RIGHT'
                elif event.key==pygame.K_LEFT:
                    direction='LEFT'
            elif direction=='DOWN':
                if event.key==pygame.K_RIGHT:
                    direction='LEFT'
                elif event.key==pygame.K_LEFT:
                    direction='RIGHT'





def update_snake():
    """
     This should contain the code for snake to move, grow, detect walls etc.
     """
    # Code for making the snake move in the expected direction
    global direction
    if direction=='RIGHT':                                                          #moving snake_pos according to the direction found         
        snake_pos[0]+=10                                               
    elif direction=='LEFT':
        snake_pos[0]-=10
    elif direction=='UP':
        snake_pos[1]-=10
    elif direction=='DOWN':
        snake_pos[1]+=10
    

    # Make the snake's body respond after the head moves. The responses will be different if it eats the food.
    # Note you cannot directly use the functions for detecting collisions 
    # since we have not made snake and food as a specific sprite or surface.
    global score
    if snake_pos==food_pos:
        add_element=[snake_body[-1][0],snake_body[-1][1]]
        snake_body.append(add_element)                                          #adding a list of new block added when snake eats food
        score+=1
        food_spawn=True
        create_food()
        
    second_element=[]
    second_element.append(snake_body[0][0])
    second_element.append(snake_body[0][1])
    
    for i in range(0,(score+2)):                                                #updating the position of each block after it moves like 
        snake_body[(score+2)-i]=snake_body[(score+2)-(i+1)]                     #the 2nd block will take the place of 1st block

    snake_body[1]=second_element                                                #second_element will keep the pplace of 1st block before moving
                                                                                #otherwise the 2nd block will take same value as 1st block after moving
    snake_body[0][0]=snake_pos[0]                                                
    snake_body[0][1]=snake_pos[1]                                               #updating the 1st block position
                          

    


    # End the game if the snake collides with the wall or with itself.
    for body in snake_body:
        if body!=snake_body[0] and body!=snake_body[1]:                 
            if (snake_pos[0]==body[0] and snake_pos[1]==body[1]+10) or (snake_pos[0]==body[0]+10 and snake_pos[1]==body[1]):
                game_over()

    
    if snake_pos[0]<0 or snake_pos[0]>720:
        game_over()
    elif snake_pos[1]<0 or snake_pos[1]>480:
        game_over()






def create_food():
    """ 
    This function should set coordinates of food if not there on the screen. You can use randrange() to generate
    the location of the food.
    """
    global food_pos
    x=random.randrange(0,720,10)
    y=random.randrange(0,480,10)
    food_pos=[x,y]




def show_score(pos, color, font, size):
    """
    It takes in the above arguements and shows the score at the given pos according to the color, font and size.
    """
    global score
    showscore_img = pygame.font.SysFont(font, size).render("score:"+str(score), True, color)
    showscore_rect = showscore_img.get_rect()
    showscore_rect=pos
    game_window.blit(showscore_img, showscore_rect)
    pygame.display.update()


def update_screen():
    """
    Draw the snake, food, background, score on the screen
    """
    game_window.fill((0,0,0))
    for body in snake_body:
        pygame.draw.rect(game_window,(255,255,0),pygame.Rect(body[0],body[1],10,10))
        
       
        
    pygame.draw.rect(game_window,(255,0,0),pygame.Rect(food_pos[0],food_pos[1],10,10))
    
    
    show_score((10,10),(240,240,240),None,20)
    
    pygame.display .update()
    



def game_over():
    """ 
    Write the function to call in the end. 
    It should write game over on the screen, show your score, wait for 3 seconds and then exit
    """
    game_window.fill((0,0,0))
    gameover_img = pygame.font.SysFont(None, 48).render("GAME OVER", True, (240,240,240))
    gameover_rect = gameover_img.get_rect()
    gameover_rect.centerx = frame_size_x/2
    gameover_rect.top = 20
    game_window.blit(gameover_img, gameover_rect)

    show_score((frame_size_x/2-50,50),(240,240,240),None,48)
    pygame.display.flip()
    
    time.sleep(3)
    sys.exit(0)







# Main loop
while True:
    # Make appropriate calls to the above functions so that the game could finally run
    check_for_events()
    update_snake()
    update_screen()

    
    # To set the speed of the screen
    fps_controller.tick(25)
