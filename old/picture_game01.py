import pygame

# Initialize pygame and create a window for the game
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 30)

# Create a list of questions and answers
questions = [("What is the capital of France?", "Paris", "france.jpg"), 
              ("What is the largest planet in our solar system?", "Jupiter", "jupiter.jpg")]

for question in questions:
    # Display the question
    question_text = font.render(question[0], True, (255, 255, 255))
    screen.blit(question_text, (100, 100))
    # Display the image
    image = pygame.image.load(question[2])
    screen.blit(image, (400, 100))
    pygame.display.update()
    # Wait for user input
    answer = input("Your answer: ")
    if answer.lower() == question[1].lower():
        print("Correct!")
    else:
        print("Incorrect.")

# Close the window and deinitialize pygame
pygame.display.quit()
pygame.quit()
