import pygame
import random

# 초기화
pygame.init()

# 상수 정의
BLOCK_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * BOARD_WIDTH
SCREEN_HEIGHT = BLOCK_SIZE * BOARD_HEIGHT

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 테트리스 블록 모양 정의
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]  # Z
]

class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('테트리스 게임')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        
        self.board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.score = 0
        self.current_piece = None
        self.current_x = 0
        self.current_y = 0
        
        self.fall_time = 0
        self.fall_speed = 1000  # 1초
        
    def new_piece(self):
        self.current_piece = random.choice(SHAPES)
        self.current_x = BOARD_WIDTH // 2 - len(self.current_piece[0]) // 2
        self.current_y = 0
        
    def collision(self):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.current_x + x
                    new_y = self.current_y + y
                    if (new_x < 0 or new_x >= BOARD_WIDTH or
                        new_y >= BOARD_HEIGHT or
                        (new_y >= 0 and self.board[new_y][new_x])):
                        return True
        return False
        
    def merge_piece(self):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.current_y + y][self.current_x + x] = 1
        self.clear_lines()
        
    def clear_lines(self):
        lines_cleared = 0
        for y in range(BOARD_HEIGHT - 1, -1, -1):
            if all(self.board[y]):
                del self.board[y]
                self.board.insert(0, [0 for _ in range(BOARD_WIDTH)])
                lines_cleared += 1
        self.score += lines_cleared * 100
        
    def rotate_piece(self):
        rotated = [[self.current_piece[y][x] 
                   for y in range(len(self.current_piece)-1, -1, -1)]
                   for x in range(len(self.current_piece[0]))]
        if not self.collision():
            self.current_piece = rotated
            
    def draw(self):
        self.screen.fill(BLACK)
        
        # 보드 그리기
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, WHITE,
                                   (x * BLOCK_SIZE, y * BLOCK_SIZE,
                                    BLOCK_SIZE - 1, BLOCK_SIZE - 1))
                    
        # 현재 조각 그리기
        if self.current_piece:
            for y, row in enumerate(self.current_piece):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(self.screen, RED,
                                       ((self.current_x + x) * BLOCK_SIZE,
                                        (self.current_y + y) * BLOCK_SIZE,
                                        BLOCK_SIZE - 1, BLOCK_SIZE - 1))
                        
        # 점수 표시
        score_text = self.font.render(f'점수: {self.score}', True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        
    def run(self):
        if not self.current_piece:
            self.new_piece()
            
        running = True
        while running:
            self.clock.tick(60)
            current_time = pygame.time.get_ticks()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.current_x -= 1
                        if self.collision():
                            self.current_x += 1
                    elif event.key == pygame.K_RIGHT:
                        self.current_x += 1
                        if self.collision():
                            self.current_x -= 1
                    elif event.key == pygame.K_DOWN:
                        self.current_y += 1
                        if self.collision():
                            self.current_y -= 1
                            self.merge_piece()
                            self.new_piece()
                            if self.collision():
                                self.board = [[0 for _ in range(BOARD_WIDTH)] 
                                            for _ in range(BOARD_HEIGHT)]
                                self.score = 0
                    elif event.key == pygame.K_UP:
                        self.rotate_piece()
                        
            # 자동 낙하
            if current_time - self.fall_time > self.fall_speed:
                self.current_y += 1
                if self.collision():
                    self.current_y -= 1
                    self.merge_piece()
                    self.new_piece()
                    if self.collision():
                        self.board = [[0 for _ in range(BOARD_WIDTH)] 
                                    for _ in range(BOARD_HEIGHT)]
                        self.score = 0
                self.fall_time = current_time
                
            self.draw()
            
        pygame.quit()

if __name__ == '__main__':
    game = Tetris()
    game.run()
