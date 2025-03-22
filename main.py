import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна и цвета
WINDOW_SIZE = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

# Создание окна
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Dots and Boxes")

# Звуковые эффекты
pygame.mixer.init()
click_sound = pygame.mixer.Sound("1.wav")
square_sound = pygame.mixer.Sound("1.wav")

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def main_menu():
    while True:
        screen.fill(WHITE)
        draw_text('Dots and Boxes', pygame.font.SysFont(None, 72), BLACK, screen, WINDOW_SIZE // 2, 100)

        mx, my = pygame.mouse.get_pos()

        button_5 = pygame.Rect(WINDOW_SIZE // 2 - 100, 250, 200, 50)
        button_6 = pygame.Rect(WINDOW_SIZE // 2 - 100, 350, 200, 50)
        button_7 = pygame.Rect(WINDOW_SIZE // 2 - 100, 450, 200, 50)

        if button_5.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                game_loop(5)
        if button_6.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                game_loop(6)
        if button_7.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                game_loop(7)

        pygame.draw.rect(screen, GRAY, button_5)
        pygame.draw.rect(screen, GRAY, button_6)
        pygame.draw.rect(screen, GRAY, button_7)

        draw_text('5x5 Grid', pygame.font.SysFont(None, 36), BLACK, screen, WINDOW_SIZE // 2, 275)
        draw_text('6x6 Grid', pygame.font.SysFont(None, 36), BLACK, screen, WINDOW_SIZE // 2, 375)
        draw_text('7x7 Grid', pygame.font.SysFont(None, 36), BLACK, screen, WINDOW_SIZE // 2, 475)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def game_loop(grid_size):
    cell_size = WINDOW_SIZE // grid_size
    horizontal_lines = [[0] * (grid_size - 1) for _ in range(grid_size)]
    vertical_lines = [[0] * grid_size for _ in range(grid_size - 1)]
    squares = [[0] * (grid_size - 1) for _ in range(grid_size - 1)]
    player_turn = 1
    score = [0, 0]

    def draw_grid():
        screen.fill(WHITE)
        offset = cell_size // 2

        # Рисуем точки
        for x in range(grid_size):
            for y in range(grid_size):
                pygame.draw.circle(screen, BLACK, (x * cell_size + offset, y * cell_size + offset), 5)

        # Рисуем горизонтальные линии
        for y in range(grid_size):
            for x in range(grid_size - 1):
                color = DARK_GRAY if horizontal_lines[y][x] == 0 else (RED if horizontal_lines[y][x] == 1 else BLUE)
                pygame.draw.line(screen, color, (x * cell_size + offset, y * cell_size + offset), ((x + 1) * cell_size + offset, y * cell_size + offset), 3)

        # Рисуем вертикальные линии
        for y in range(grid_size - 1):
            for x in range(grid_size):
                color = DARK_GRAY if vertical_lines[y][x] == 0 else (RED if vertical_lines[y][x] == 1 else BLUE)
                pygame.draw.line(screen, color, (x * cell_size + offset, y * cell_size + offset), (x * cell_size + offset, (y + 1) * cell_size + offset), 3)

        # Рисуем квадраты
        for y in range(grid_size - 1):
            for x in range(grid_size - 1):
                if squares[y][x] != 0:
                    color = RED if squares[y][x] == 1 else BLUE
                    pygame.draw.rect(screen, color, (x * cell_size + offset + 5, y * cell_size + offset + 5, cell_size - 10, cell_size - 10))

        # Отображение счета
        font = pygame.font.SysFont(None, 36)
        score_text = f"Player 1: {score[0]}    Player 2: {score[1]}"
        text = font.render(score_text, True, BLACK)
        screen.blit(text, (10, WINDOW_SIZE - 40))

        pygame.display.flip()

    def check_square():
        completed = False
        for y in range(grid_size - 1):
            for x in range(grid_size - 1):
                if squares[y][x] == 0 and horizontal_lines[y][x] and horizontal_lines[y+1][x] and vertical_lines[y][x] and vertical_lines[y][x+1]:
                    squares[y][x] = player_turn
                    score[player_turn - 1] += 1
                    square_sound.play()
                    completed = True
        return completed

    def handle_click(x, y):
        nonlocal player_turn

        offset = cell_size // 2
        for i in range(grid_size):
            for j in range(grid_size - 1):
                if x > j * cell_size + offset and x < (j + 1) * cell_size + offset and y > i * cell_size + offset - 5 and y < i * cell_size + offset + 5:
                    if horizontal_lines[i][j] == 0:
                        horizontal_lines[i][j] = player_turn
                        click_sound.play()
                        if not check_square():
                            player_turn = 3 - player_turn
                        return

        for i in range(grid_size - 1):
            for j in range(grid_size):
                if x > j * cell_size + offset - 5 and x < j * cell_size + offset + 5 and y > i * cell_size + offset and y < (i + 1) * cell_size + offset:
                    if vertical_lines[i][j] == 0:
                        vertical_lines[i][j] = player_turn
                        click_sound.play()
                        if not check_square():
                            player_turn = 3 - player_turn
                        return

    def is_game_over():
        for row in squares:
            if 0 in row:
                return False
        return True

    def display_winner():
        font = pygame.font.SysFont(None, 72)
        if score[0] > score[1]:
            winner_text = "Player 1 Wins!"
        elif score[0] < score[1]:
            winner_text = "Player 2 Wins!"
        else:
            winner_text = "It's a Tie!"
        text = font.render(winner_text, True, BLACK)
        screen.fill(WHITE)
        screen.blit(text, (WINDOW_SIZE // 2 - text.get_width() // 2, WINDOW_SIZE // 2 - text.get_height() // 2))
        pygame.display.flip()

        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    while True:
        draw_grid()

        if is_game_over():
            display_winner()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                handle_click(x, y)

# Запуск главного меню
main_menu()
