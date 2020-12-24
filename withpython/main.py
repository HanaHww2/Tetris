import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes : S, Z, I, O, J, L, T
represented in order by 0 -6
"""

pygame.font.init()

# GLOBAL VARs
s_width = 700
s_height = 800
play_width = 300  # meaning 300//10 = 30 width per block
play_height = 600  # meaning 300//20 = 30 width per block
block_size = 30

top_left_x = 80 # 임의 지정, (s_width - play_width) // 2 : 가운데
top_left_y = s_height - play_height - 80 # 120, 아래에서 80

# SHAPE FORMATs
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.000.',
      '...0.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]  # index 0 - 6 represent each shape
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0),
                (255, 165, 0), (0, 0, 255), (128, 0, 128)]


class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

def get_shape():
    return Piece(5, 0, random.choice(shapes))

def create_grid(locked_pos={}):  # ex. {(1,1):(255,0,0)}
    # 20 x 10, (0, 0, 0) means rgb
    # for _ in range(10) is same with for x in range(10)
    grid = [[(0, 0, 0) for x in range(10)]for _ in range(20)]

    for i in range(len(grid)): # 20
        for j in range(len(grid[i])): # 10
            if (j, i) in locked_pos:
                c = locked_pos[(j, i)]
                grid[i][j] = c
    return grid

def draw_window(surface, grid, score = 0, h_score = 0):
    # 배경색
    surface.fill((0, 0, 0))  # black
    pygame.font.init()
    # sx = top_left_x + play_width
    # sy = top_left_y + play_height/2 - 100
    font = pygame.font.SysFont('comicsans', 60)
    # game title on top
    label = font.render('Tetris', 1, (255, 255, 255))
    surface.blit(label,
                 (top_left_x + play_width/2 - (label.get_width()/2), 40))  # 40은 임의의 높이 (80/2)
    # current score
    font = pygame.font.SysFont('comicsans', 30)
    current_score = font.render('Score : ' + str(score), 1, (255, 255, 255))
    surface.blit(current_score,
                 (top_left_x * 2+ play_width + 10, top_left_y + 150))
    # last_score
    last_score = font.render('High Score : ' + h_score, 1, (255, 255, 255))
    surface.blit(last_score, 
                (top_left_x * 2+ play_width + 10, top_left_y + 200))
    # 흰색 외곽선 그리기
    pygame.draw.rect(surface, (255, 255, 255), (top_left_x, top_left_y, play_width, play_height), 5)
    # draw grid inside and border
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j],  # 각 블록을 색상별로 그리드에 그리기
                             (top_left_x + j * block_size + 1, top_left_y + i * block_size + 1,
                              block_size - 1, block_size - 1), 0) # -1을 해서 블록 간 여백 만들기
    # draw_grid(surface, grid)
    

def draw_next_shape(shape, surface):
    sx = top_left_x * 2+ play_width # + 50
    sy = top_left_y # + play_height/2 - 100
    # label 그리기    
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255, 255, 255))
    surface.blit(label, (sx + 10, sy - 30))
    # 다음 블록 미리 보기
    format = shape.shape[shape.rotation % len(shape.shape)]
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, 
                (sx +  j * block_size + 1, sy + i * block_size + 1, 
                            block_size - 1, block_size - 1), 0)

# This function draws the grey grid lines that we see, 이보다는 블록의 여백으로 대체
# def draw_grid(surface, grid):     
    # pass
    # sx = top_left_x
    # sy = top_left_y
    # for i in range(len(grid)):
    #     pygame.draw.line(surface, (128, 128, 128), # draw horizontal line
    #                     (sx, sy + i * block_size), (sx + play_width, sy + i * block_size))
        # for j in range(len(grid[i])):
        #     pygame.draw.line(surface, (128, 128, 128), # vertical lines
        #                 (sx + j * block_size, sy), (sx + j * block_size, sy + play_height))                

def convert_shape_format(shape): # shape을 컴퓨터가 이해하도록 변환
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)] # shape의 형태

    for i, line in enumerate(format):
        row = list(line) # 각 행을 체크
        for j, column in enumerate(row):
            if column == '0': # 행 안의 '0'을 체크
                positions.append((shape.x + j, shape.y + i)) # shape 형태('0'의 위치)의 리스트 생성

    # offset 조정, format에서 보면, '.'으로 만들어진 부분이 존재하므로, 제거 필요
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)   
    return positions

# 블록을 생성하거나 회전할 때, 공간이 있는지 체크
def valid_space(shape, grid):
    # 블록(색)이 채워지지 않은 공간정보를 리스트로 생성
    # accepted_pos = [(j, i) for j in range(10) if grid[i][j] == (0, 0, 0) for i in range(20)]
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)] 
    accepted_pos = [j for sub in accepted_pos for j in sub] # flatten, 1차원 리스트, sub 행/ j 열
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_pos: # 블록에 공간이 적합하지 않다면
            if pos[1] > -1: # 위치가 y >= 0 이면, 블록이 게임화면에 드러나 있는 경우면, 
                return False # 새로운 블록을 만들지 않음
    return True

def clear_rows(grid, locked_pos):
    inc = 0 # increment
    ind = []
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if (0, 0, 0) not in row: # empty = (0, 0, 0)
            # inc += 1
            ind.append(i) # bottom to top, ind = i
            for j in range(len(row)):
                try:
                    del locked_pos[(j, i)]
                except: # 오류 발생 방지, outofsomething
                    continue
    # if inc > 0:
    #     for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
    #         x, y = key
    #         if y < ind: # 삭제되는 선이 띄엄띄엄 있을 때 오류 발생! -> fixed it!(아래)
    #             newKey = (x, y + inc)
    #             locked[newKey] = locked.pop(key)

    if len(ind) > 0:
        # list(dict) key 값만 list로 변환
        for key in sorted(list(locked_pos), key = lambda k: k[1])[::-1]:
                x, y = key
                # y값보다 큰 ind 의 갯수만큼 위치 이동
                inc_list = list(filter(lambda i: ind[i] > y, range(len(ind))))
                if len(inc_list) > 0:
                    newKey = (x, y + max(inc_list) + 1)
                    locked_pos[newKey] = locked_pos.pop(key)
    return len(ind)

# 게임의 lost, checking if we lose the Game
def check_lost(positions): 
    for pos in positions:
        x, y = pos
        if y < 1 : # 블록이 천장에 닿으면, y<=0
            return True
    return False

def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, 
        (s_width /2 - (label.get_width()/2), top_left_y + play_height/2 - (label.get_height()/2)))

def update_score(nscore):
    score = max_score()

    with open('scores.txt', 'r') as f:
        if int(score) > nscore:
            f.write(str(score))
        else:
            f.write(str(nscore))

def max_score():
    with open('scores.txt', 'r') as f:
        lines = f.readlines()
        score = lines[0].strip()
    return score

def main(win):
    locked_positions = {} # 더 이상 moving이 없는 블록들의 위치(key)와 색상(value)의 딕셔너리
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
#     # next_next_piece 이것도 추가하고 싶다
    clock = pygame.time.Clock()
    fall_speed = .27
    fall_time = 0
    level_time = 0
    score = 0
    last_score = max_score()

    while run:
        grid = create_grid(locked_positions)

        level_time += clock.get_rawtime()
        fall_time += clock.get_rawtime()
        clock.tick() # 타이머 작동 시작인 듯
        if level_time/1000 > 5: # > 5sec
            level_time = 0
            if fall_speed > .2: # 제한속도
                fall_speed -= .001 # 5

            #             level_time = 0
#             if level_time > 0.12:
#                 level_time -= 0.005

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1 # automatically y값이 아래로 떨어지도록 한다
            if not(valid_space(current_piece, grid)) and current_piece.y > 0: # 블록이 화면상에 있고, 이동할 공간이 있다면
                current_piece.y -= 1 # pretend not to happen, 더 이상 움직일 수 없음
                change_piece = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit() # 종료
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.rotation -= 1

        shape_pos = convert_shape_format(current_piece)
        
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece: # 새로운 블록 생성
            for pos in shape_pos:
                p = (pos[0], pos[1])
                # 딕셔너리 key 값 : p, value 값 : (rgb), 현재 블록을 고정시킴
                locked_positions[p] = current_piece.color 
            current_piece = next_piece # 새 블록
            next_piece = get_shape() # 다음에 나올 블록 설정
            change_piece = False
            num_rows = clear_rows(grid, locked_positions)
            score += num_rows * 10
            if num_rows > 2 : # 연속 3줄 이상이면 추가점수
                score += num_rows * 5

        draw_window(win, grid, score, last_score)
        draw_next_shape(next_piece, win)
        pygame.display.update() # 파이게임에 그리기

        if check_lost(locked_positions):
            draw_text_middle(win, 'YOU LOST!', 80, (255, 0, 0))
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
            update_score(score)

def main_menu(win):
    window = True
    while window:
        win.fill((0, 0, 0))
        draw_text_middle(win, 'Press Any Key To play', 60, (255, 255, 255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window = False
            if event.type == pygame.KEYDOWN:
                main(win)

#     pygame.display.quit()


win = pygame.display.set_mode((s_width, s_height)) # is gonna be surface
pygame.display.set_caption('Tetris')
main_menu(win)  # start game
