from keyboard import is_pressed
from time import sleep
from random import randrange, choice
from list_manipulation_functions import *

FPS = 1
run = True

board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]


def spawn():
    global board
    list = []
    for y in range(0, len(board)):
        for x in range(0, len(board[y])):
            if board[y][x] == 0:
                list.append([y, x])
    
    cell = list[randrange(0, len(list)-1)]
    board[cell[0]].pop(cell[1])
    board[cell[0]].insert(cell[1], choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4]))


def move(key):
    global board

    if key in ("r", "l"):
        for i in range(len(board)):
            row = board[i]
            zero_count = row.count(0)
            if zero_count > 0:
                for n in range(zero_count):
                    row.remove(0)
                for n in range(zero_count):
                    if key == "r":
                        row.insert(0, 0)
                    if key == "l":
                        row.append(0)
            board.pop(i)
            board.insert(i, row)
    
    if key in ("u", "d"):
        board = rotate(board)
        for i in range(len(board)):
            column = board[i]
            zero_count = column.count(0)
            if zero_count > 0:
                for n in range(zero_count):
                    column.remove(0)
                for n in range(zero_count):
                    if key == "d":
                        column.insert(0, 0)
                    if key == "u":
                        column.append(0)
            board.pop(i)
            board.insert(i, column)
        board = rotate(board)
                

def merge(key):
    global board
    
    if key == "r":
        mirror_x(board)
        for y in range(len(board)):
            for x in range(len(board[y]) - 1):
                mainCell = board[y][x]
                secondaryCell = board[y][x + 1]
                if mainCell == secondaryCell:
                    board[y][x] = mainCell + secondaryCell
                    board[y][x + 1] = 0
        mirror_x(board)
    
    if key == "l":
        for y in range(len(board)):
            for x in range(len(board[y]) - 1):
                mainCell = board[y][x]
                secondaryCell = board[y][x + 1]
                if mainCell == secondaryCell:
                    board[y][x] = mainCell + secondaryCell
                    board[y][x + 1] = 0

    if key == "d":
        mirror_y(board)
        for y in range(len(board) - 1):
            for x in range(len(board[y])):
                mainCell = board[y][x]
                secondaryCell = board[y + 1][x]
                if mainCell == secondaryCell:
                    board[y][x] = mainCell + secondaryCell
                    board[y + 1][x] = 0
        mirror_y(board)
    
    if key == "u":
        for y in range(len(board) - 1):
            for x in range(len(board[y])):
                mainCell = board[y][x]
                secondaryCell = board[y + 1][x]
                if mainCell == secondaryCell:
                    board[y][x] = mainCell + secondaryCell
                    board[y + 1][x] = 0


def draw(board):
    for y in range(len(board)):
        print("".join(str(board[y])).replace(",", "  ").replace("0", " "))
    print("\n\n")

                


def quit():
    global run
    if is_pressed("esc"):
        run = False


def main():
    spawn()
    draw(board)
    
    while run:
        quit()
        if run == False:
            break
        
        if is_pressed("right"):
            pressed = "r"
        elif is_pressed("left"):
            pressed = "l"
        elif is_pressed("up"):
            pressed = "u"
        elif is_pressed("down"):
            pressed = "d"
        else:
            pressed = ""

        if pressed != "":
            move(pressed)
            merge(pressed)
            move(pressed)
            spawn()
            draw(board)
        sleep(1/FPS)
    

if __name__ == '__main__':
    main()