# imports
import pygame
import time
import random 
# initialised font module
pygame.font.init()

# creating the window
WIDTH, HEIGHT = 1000,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

# setting background image
BG = pygame.transform.scale(pygame.image.load("bg.jpg"),(WIDTH,HEIGHT))
    # drawing the background image
def draw():
    WIN.blit(BG, (0,0))
    pygame.display.update()

# player variables (these are constant variables - independent variables, really)
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

# moving the player around variables
PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

# font
FONT = pygame.font.SysFont("AestheticRegular", 20)

# drawing the player
def draw(player,elapsed_time,stars):
    WIN.blit(BG, (0,0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (15,15))

    pygame.draw.rect(WIN,(88,196,62),player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update()

# caption for the window
pygame.display.set_caption("Space Dodge")

# main game loop (to keep the game alive and running)
    # also, defining the 'x' button so that the game can be quit
def main():
    # make the code run
    run = True

    # moving the character
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH,PLAYER_HEIGHT)

    # determining the speed of the loop that runs the game
    clock = pygame.time.Clock()

    # time variable - current time
    start_time = time.time()
    elapsed_time = 0

    # adding projectiles
    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    # loop that runs all throughout the game
    while run:
        # determines speed of loop when running - value in brackets is fps
        clock.tick(60)
        # generate stars - counts the millisecond since the last clock tick
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range (3):
                # picks random integer between width-star_width, which is a valid position for the x coordinate of the star that we are generating (we can do this because we imported the random module into the program)
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                    # the reason why it is -STAR_HEIGHT, and not 0, is because it looks like the stars are falling into the screen, rather than the stars starting at the top of the screen, and THEN moving down.
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0    

        # being able to exit the game using the 'x' key
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        # moving the character around - keep in mind that the speed that the loop is running is determining the speed that the character is moving
            # adding a guard clause so that you cannot move the character off-screen (e.g.: 'and player.x - PLAYER_VEL >= 0')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_a] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
            # right key is longer gode because it accounts for the fact that the top left corner of the screen is (0,0)
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_d] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        
        # drawing projectiles onto the screen so that they are able to be seen, and removing the projectiles if they get hit by the shooter of if they touch the main character
            # the [:]: means that the code is copied
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                star.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        
        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text,(WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)
    
    pygame.quit()

# making sure that when the code is run that only this file called 'main' is run, not all the other python files on my system called 'main' also running as well at the same time
    # although, if this code is imported, this code here will be false
if __name__ == "__main__":
    main()