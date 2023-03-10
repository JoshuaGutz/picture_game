import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import json
import random
import pygame
#import ptext

# Get the directory path of the script, json, and images
dir_path = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(dir_path, "json")
images_path = os.path.join(dir_path, "images")

def random_rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def show_instructions():
    font = pygame.font.Font(None, 30)
    instructions_text1 = "Welcome to the game. Click or press any key to begin!"
    instructions_text2 = "Click on the boxes to reveal images. They disappear after 1 second."
    instructions_text3 = "Make your own categories with json!"
    instructions_text4 = "Press 'r' to reset with 5 new random categories."
    instructions_text5 = "Press 'i' to revisit these instructions."
    instructions_text6 = "Press 'Esc' or 'q' or 'w' or 'Ctrl+q' or 'Ctrl+w' quit."
    instructions_text7 = "Yes, all colors everywhere are randomly generated every time just because."
    instructions_text = "\n".join([instructions_text1, instructions_text2, instructions_text3, instructions_text4, instructions_text5, instructions_text6, instructions_text7])
    instructions_text = instructions_text1 + "\n" + instructions_text2 + "\n" + instructions_text3 + "\n" + instructions_text4 + "\n" + instructions_text5 + "\n" + instructions_text6 + "\n" + instructions_text7
    #print(instructions_text)
    #text_surface = font.render(instructions_text, True, (255, 255, 255))
    text_surface1 = font.render(instructions_text1, True, random_rgb_color())
    text_surface2 = font.render(instructions_text2, True, random_rgb_color())
    text_surface3 = font.render(instructions_text3, True, random_rgb_color())
    text_surface4 = font.render(instructions_text4, True, random_rgb_color())
    text_surface5 = font.render(instructions_text5, True, random_rgb_color())
    text_surface6 = font.render(instructions_text6, True, random_rgb_color())
    text_surface7 = font.render(instructions_text7, True, random_rgb_color())
    #text_surface = font.render(instructions_text, True, random_rgb_color())
    screen.fill(random_rgb_color())
    screen.blit(text_surface1, (25, 50))
    screen.blit(text_surface2, (25, 100))
    screen.blit(text_surface3, (25, 150))
    screen.blit(text_surface4, (25, 200))
    screen.blit(text_surface5, (25, 250))
    screen.blit(text_surface6, (25, 300))
    screen.blit(text_surface7, (25, 350))
    #screen.blit(text_surface, (50, 50))
    #ptext.draw(instructions_text, (10, 10), color=random_rgb_color())  # Recognizes newline characters.
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return

def load_categories():
    # Get a list of all category-*.json files in the json subdirectory
    files = [file for file in os.listdir(json_path) if file.startswith("category-") and file.endswith(".json")]

    # Select 5 random files from the list
    random_files = random.sample(files, 5)

    # Load the data for each selected file
    categories = []
    for file in random_files:
        try:
            with open(os.path.join(json_path, file)) as json_file:
                categories.append(json.load(json_file))
                #print(f"{file} loaded successfully")
        except FileNotFoundError:
            print(f"File {file} not found.")
        except json.decoder.JSONDecodeError:
            print(f"File {file} is not a valid json file.")
        # handle any other exception
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    return categories

def draw_game_board(screen, categories, font=None):
    if font is None:
        font = pygame.font.Font(None, 30)
    #screen.fill((0, 0, 0))
    screen.fill(random_rgb_color())
    screen.fill((0, 0, 0))
    screen_rect = screen.get_rect()
    column_width = screen_rect.width / 5
    row_height = screen_rect.height / 6
    # Draw the game board
    for i, category in enumerate(categories):
        column_rect = pygame.Rect(i * column_width, 0, column_width, screen_rect.height)
        #pygame.draw.rect(screen, (255, 255, 255), column_rect, 2)
        pygame.draw.rect(screen, random_rgb_color(), column_rect, 2)
        #category_name = category["name"]
        #image_files = category["image_files"]
        # Draw the category heading
        heading_rect = pygame.Rect(i * column_width, 0, column_width, row_height)
        #heading_text = font.render(category['name'], True, (255, 255, 255))
        heading_text = font.render(category['name'], True, random_rgb_color())
        heading_text_rect = heading_text.get_rect(center=heading_rect.center)
        screen.blit(heading_text, heading_text_rect)
        # Draw the underline
        #pygame.draw.line(screen, (255, 255, 255), (heading_text_rect.left, heading_text_rect.bottom+2), (heading_text_rect.right, heading_text_rect.bottom+2), 2)
        pygame.draw.line(screen, random_rgb_color(), (heading_text_rect.left, heading_text_rect.bottom+2), (heading_text_rect.right, heading_text_rect.bottom+2), 2)
        # Draw the boxes and values
        for j, value in enumerate([200, 400, 600, 800, 1000]):
            box_rect = pygame.Rect(i * column_width, (j + 1) * row_height, column_width, row_height)
            #pygame.draw.rect(screen, (255, 255, 255), box_rect, 2)
            pygame.draw.rect(screen, random_rgb_color(), box_rect, 2)
            #value_text = font.render(str(value), True, (255, 255, 255))
            value_text = font.render(str(value), True, random_rgb_color())
            value_text_rect = value_text.get_rect(center=box_rect.center)
            screen.blit(value_text, value_text_rect)
    # Update the display
    pygame.display.update()

def check_box_clicked(x, y):
    screen_rect = screen.get_rect()
    column_width = screen_rect.width / 5
    row_height = screen_rect.height / 6
    for i in range(5):
        for j in range(5):
            box_rect = pygame.Rect(i * column_width, (j + 1) * row_height, column_width, row_height)
            if box_rect.collidepoint(x, y):
                return i, j
    return None

def show_image_not_found():
    font = pygame.font.SysFont(None, 60)
    screen_rect = screen.get_rect()
    #text = font.render("Image not found", True, (255,255,255))
    text = font.render("Image not found", True, random_rgb_color())
    text_rect = text.get_rect()
    text_rect.center = screen_rect.center
    screen.blit(text, text_rect)
    #pygame.display.update()

def show_image(i, j):
    try:
        image = pygame.image.load(os.path.join(images_path, categories[i]['image_files'][j]))
        # Scale the image to fit the window size
        image = pygame.transform.scale(image, (width, height))
        # Set the transparency level of the image
        # image.set_alpha(128) sets the transparency level of the image to 128 out of 255.
        image.set_alpha(128)
        # Set a transparent color for the image
        # image.set_colorkey((255, 0, 255)) sets the color (255, 0, 255) as the transparent color for the image.
        #image.set_colorkey((255, 0, 255))
        image.set_colorkey(random_rgb_color())
        # Convert the image to the same format as the screen and keep transparency
        image = image.convert_alpha()
        # Draw the image on top of the game board
        screen.blit(image, (0, 0))
    except (pygame.error, FileNotFoundError, Exception):
        show_image_not_found()
    pygame.display.update()

# load the json
categories = load_categories()

# Initialize pygame and create the screen
pygame.init()
info = pygame.display.Info()
width = int(info.current_w * 0.4)
height = int(info.current_h * 0.4)
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

show_instructions()

# Main loop
resizing = False
redrawing = True
running = True
while running:
    if resizing:
        resizing = False
        redrawing = True
        screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    if redrawing:
        redrawing = False
        draw_game_board(screen, categories)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_ESCAPE) or (event.mod & pygame.KMOD_CTRL and event.key == pygame.K_w) or (event.mod & pygame.KMOD_CTRL and event.key == pygame.K_q) or (event.key == pygame.K_q) or (event.key == pygame.K_w):
                running = False
            elif (event.key == pygame.K_r):
                redrawing = True
                categories = load_categories()
            elif (event.key == pygame.K_i):
                redrawing = True
                show_instructions()
        elif event.type == pygame.VIDEORESIZE:
            resizing = True
            width, height = event.size
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get position of the mouse click and check if it was inside a box
            mouse_pos = pygame.mouse.get_pos()
            box_clicked = check_box_clicked(*mouse_pos)
            if box_clicked is not None:
                show_image(*box_clicked)
                # Make this shorter for debugging, longer for playing
                #pygame.time.wait(50)
                pygame.time.wait(1000)
                while pygame.mouse.get_pressed()[0]:
                    pygame.event.pump()
                redrawing = True

# Close the window and deinitialize pygame
pygame.display.quit()
pygame.quit()

