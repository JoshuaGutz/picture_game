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

# Create the game board
screen = pygame.display.set_mode((800, 600))
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

# Update the display
pygame.display.update()

answer = input("Your answer: ")

# Close the window and deinitialize pygame
pygame.display.quit()
pygame.quit()
