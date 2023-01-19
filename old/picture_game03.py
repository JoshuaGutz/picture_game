import pygame

# Initialize pygame and create a window for the game
pygame.init()
#screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 30)
#
## Create a list of questions and answers
#questions = [("What is the capital of France?", "Paris", "france.jpg"), 
#              ("What is the largest planet in our solar system?", "Jupiter", "jupiter.jpg")]
#
#for question in questions:
#    # Display the question
#    question_text = font.render(question[0], True, (255, 255, 255))
#    screen.blit(question_text, (100, 100))
#    # Display the image
#    image = pygame.image.load(question[2])
#    screen.blit(image, (400, 100))
#    pygame.display.update()
#    # Wait for user input
#    answer = input("Your answer: ")
#    if answer.lower() == question[1].lower():
#        print("Correct!")
#    else:
#        print("Incorrect.")

#######################################################################
import json

# Load the categories and image files from the JSON file
with open('categories.json') as json_file:
    data = json.load(json_file)

## Create the game board
#screen = pygame.display.set_mode((800, 600))
#for i, category in enumerate(data['categories']):
#    # Draw the category heading
#    heading_text = font.render(category['name'], True, (255, 255, 255))
#    screen.blit(heading_text, (i * 150 + 25, 25))
#
#    # Draw the boxes for the values
#    for j, value in enumerate([200, 400, 600, 800, 1000]):
#        box_rect = pygame.Rect(i * 150 + 25, (j + 1) * 50 + 25, 100, 25)
#        pygame.draw.rect(screen, (255, 255, 255), box_rect, 2)
#
#        value_text = font.render(str(value), True, (255, 255, 255))
#        screen.blit(value_text, (i * 150 + 35, (j + 1) * 50 + 30))
#
## Update the display
#pygame.display.update()

#answer = input("Your answer: ")

# Close the window and deinitialize pygame
#pygame.display.quit()
#pygame.quit()


#######################################################################

# Create the game board
def draw_game_board(screen, font, data):
    # Draw the game board
    for i, category in enumerate(data['categories']):
        # Draw the category heading
        heading_text = font.render(category['name'], True, (255, 255, 255))
        screen.blit(heading_text, (i * 150 + 25, 25))

        # Draw the boxes for the values
        for j, value in enumerate([200, 400, 600, 800, 1000]):
            box_rect = pygame.Rect(i * 150 + 25, (j + 1) * 50 + 25, 100, 25)
            pygame.draw.rect(screen, (255, 255, 255), box_rect, 2)

            value_text = font.render(str(value), True, (255, 255, 255))
            screen.blit(value_text, (i * 150 + 35, (j + 1) * 50 + 30))

# create the screen
screen = pygame.display.set_mode((800, 600))

# Draw the game board
draw_game_board(screen, font, data)

# Update the display
pygame.display.update()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_ESCAPE) or (event.mod & pygame.KMOD_CTRL and event.key == pygame.K_w):
                running = False
        # Check for mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            mouse_pos = pygame.mouse.get_pos()
            # Check if the mouse click was inside a box
            for i, category in enumerate(data['categories']):
                for j, value in enumerate([200, 400, 600, 800, 1000]):
                    box_rect = pygame.Rect(i * 150 + 25, (j + 1) * 50 + 25, 100, 25)
                    if box_rect.collidepoint(mouse_pos):
                        try:
                            image = pygame.image.load(data['categories'][i]['image_files'][j])
                        except (pygame.error, FileNotFoundError):
                            font = pygame.font.SysFont(None, 60)
                            text = font.render("Image not found", True, (255, 255, 255))
                            screen.blit(text, (250,250))
                            pygame.display.update()
                            font = pygame.font.Font(None, 30)
                        else:
                            # Scale the image to fit the window size
                            image = pygame.transform.scale(image, screen.get_size())
                            # Set the transparency level of the image
                            # image.set_alpha(128) sets the transparency level of the image to 128 out of 255.
                            image.set_alpha(128)
                            # Set a transparent color for the image
                            # image.set_colorkey((255, 0, 255)) sets the color (255, 0, 255) as the transparent color for the image.
                            image.set_colorkey((255, 0, 255))
                            # Convert the image to the same format as the screen and keep transparency
                            image = image.convert_alpha()
                            # Draw the image on top of the game board
                            screen.blit(image, (0, 0))
                            pygame.display.update()
                        # Wait for the mouse button to be released
#                        pygame.mouse.wait(50)
# Traceback (most recent call last):
#   File "C:\Users\jgutz\Desktop\picture_game\picture_game03.py", line 101, in <module>
#     pygame.mouse.wait(50)
#     ^^^^^^^^^^^^^^^^^
# AttributeError: module 'pygame.mouse' has no attribute 'wait'
                        pygame.time.wait(50)
                        while pygame.mouse.get_pressed()[0]:
                            pygame.event.pump()
                        # Clear the screen and redraw the game board
                        screen.fill((0, 0, 0))
                        draw_game_board(screen, font, data)
#                        pygame.display.update()
                pygame.display.update()

# Close the window and deinitialize pygame
pygame.display.quit()
pygame.quit()

