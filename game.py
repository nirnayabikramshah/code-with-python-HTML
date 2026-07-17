import pygame as py
import sys
import random

# start up pygame and audio stuff so it actually works
py.init()
py.mixer.init() 

# setting up the window size (made it pretty tall)
size_x = 800
size_y = 900
screen_size = py.display.set_mode((size_x, size_y))
py.display.set_caption("Flippy Bird")

# font stuff for the title and score text
colour = (0, 225, 225)
font = py.font.Font(None, 36)
score_font = py.font.Font(None, 60)
game_over_font = py.font.Font(None, 80) # big font for when you lose
location = (300, 10)
text_surface = font.render("Flippy Bird", True, colour)

# 1. load the bird pic or just make a yellow box if the file is missing
try:
    original_bird_image = py.image.load("code-with-python-HTML/image-removebg-preview.png")
    bird_image = py.transform.scale(original_bird_image, (50, 40))
except py.error:
    bird_image = py.Surface((50, 40))
    bird_image.fill((255, 200, 0))

# 2. background image loading stuff
try:
    bg_image_loaded = py.image.load("/home/isofuji/Documents/c6c16091f90a41ded3a74b74d8cfacad.jpg")
    bg_image = py.transform.scale(bg_image_loaded, (size_x, size_y))
except py.error:
    # backup plan: dark blue background if the image breaks
    bg_image = py.Surface((size_x, size_y))
    bg_image.fill((0, 0, 50))

# bird starting position
bird_x = 100
bird_y = 400

# gravity and jumping variables (physics engine lol)
gravity = 0.5
bird_velocity = 0
flap_strength = -10  

# --- PIPE VARIABLES ---
pipe_width = 80
pipe_speed = 5
pipe_gap = 200  # how big the opening is for the bird to fit through

# make a green block for the pipes
pipe_image = py.Surface((pipe_width, size_y)) 
pipe_image.fill((0, 255, 0)) 

# pick a random spot for the gap so the game isn't too easy
def get_random_gap_y():
    return random.randint(200, 700)

pipe_x = 800
gap_y = get_random_gap_y()

# load the sound effects (hope the paths are right on my computer)
try:
    flap_sound = py.mixer.Sound("/home/isofuji/Downloads/sfx_wing.mp3")
    score_sound = py.mixer.Sound("/home/isofuji/Downloads/12-points.mp3")
    hit_sound = py.mixer.Sound("/home/isofuji/Downloads/1a758380-9bff-442f-9f32-444179da9361.mp3")
except py.error:
    # if sounds break, just ignore them so the game doesn't crash
    flap_sound = None
    score_sound = None
    hit_sound = None

# --- GAME STATS ---
score = 0
pipe_passed = False  
game_over = False # turns true when you die

clock = py.time.Clock()
running = True

# --- MAIN GAME LOOP ---
while running:
    
    # check for keyboard inputs and closing the window
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
            
        elif event.type == py.KEYDOWN:
            if not game_over:
                # jump if you press space or up arrow
                if event.key == py.K_SPACE or event.key == py.K_UP:
                    bird_velocity = flap_strength
                    if flap_sound: 
                        flap_sound.play() # make the flap noise
            else:
                # controls for the game over screen
                if event.key == py.K_r: # press R to try again
                    bird_y = 400
                    bird_velocity = 0
                    pipe_x = size_x
                    gap_y = get_random_gap_y()
                    score = 0
                    pipe_passed = False
                    game_over = False
                elif event.key == py.K_ESCAPE: # press esc to rage quit
                    running = False

    # only move things if you haven't crashed yet
    if not game_over:
        # physics calculation to make the bird fall down
        bird_velocity += gravity     
        bird_y += bird_velocity      

        # you lose if you fly off screen or hit the floor
        if bird_y > size_y - 40 or bird_y < 0:
            if hit_sound:
                hit_sound.play()
            game_over = True

        # move the pipe left across the screen
        pipe_x -= pipe_speed  
        # if the pipe goes off the left side, reset it on the right side
        if pipe_x < -pipe_width:
            pipe_x = size_x
            gap_y = get_random_gap_y()  
            pipe_passed = False 

        # math to figure out where the top and bottom pipes start
        top_pipe_y = gap_y - (pipe_gap / 2) - size_y
        bottom_pipe_y = gap_y + (pipe_gap / 2)

        # hitboxes for collision detection
        bird_rect = py.Rect(bird_x, bird_y, 50, 40)
        top_pipe_rect = py.Rect(pipe_x, top_pipe_y, pipe_width, size_y)
        bottom_pipe_rect = py.Rect(pipe_x, bottom_pipe_y, pipe_width, size_y)

        # check if the bird box runs into either pipe box
        if bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect):
            if hit_sound:
                hit_sound.play() # boom sound
            game_over = True

        # give a point if you successfully pass the pipe
        if pipe_x + pipe_width < bird_x and not pipe_passed:
            score += 1
            pipe_passed = True # make sure it only gives 1 point per pipe, not 60 points
            if score_sound:
                score_sound.play() # ding noise

    # --- DRAWING EVERYTHING ON SCREEN ---
    # draw background first so it doesn't cover up the player
    screen_size.blit(bg_image, (0, 0))

    # draw the text, bird, and pipes
    screen_size.blit(text_surface, location)
    screen_size.blit(bird_image, (bird_x, bird_y))
    screen_size.blit(pipe_image, (pipe_x, top_pipe_y))     
    screen_size.blit(pipe_image, (pipe_x, bottom_pipe_y))  

    # show score while playing
    if not game_over:
        score_surface = score_font.render(str(score), True, (255, 255, 255))
        screen_size.blit(score_surface, (size_x // 2 - 15, 60))
    else:
        # draw a dark tint overlay so the text stands out
        overlay = py.Surface((size_x, size_y), py.SRCALPHA)
        overlay.fill((0, 0, 0, 150)) 
        screen_size.blit(overlay, (0, 0))
        
        # game over screen UI layout
        go_surface = game_over_font.render("GAME OVER", True, (255, 50, 50))
        final_score_surface = score_font.render(f"Final Score: {score}", True, (255, 255, 255))
        restart_surface = font.render("Press 'R' to Restart or 'Esc' to Quit", True, (200, 200, 200))
        
        # center alignments using screen width and height division math
        screen_size.blit(go_surface, (size_x // 2 - go_surface.get_width() // 2, size_y // 2 - 100))
        screen_size.blit(final_score_surface, (size_x // 2 - final_score_surface.get_width() // 2, size_y // 2))
        screen_size.blit(restart_surface, (size_x // 2 - restart_surface.get_width() // 2, size_y // 2 + 80))

    # refresh screen and lock frame rate to 60fps so it doesn't run crazy fast
    py.display.update()
    clock.tick(60)

# close everything down clean when the loop ends
py.quit()
sys.exit()
