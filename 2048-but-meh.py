from keyboard import is_pressed
import os
from math import log
from time import sleep
from random import randrange, choice
from list_manipulation_functions import rotate, is_same, paint

FPS = 60
boardLen = 4
run = True

(board, savedBoard, temp) = ([], [], [])
for y in range(boardLen):
    board.append([])
    savedBoard.append([])
    temp.append([])
    for x in range(boardLen):
        board[y].append(0)
        savedBoard[y].append(0)
        temp[y].append(0)
'''
board = [
        [2**16, 2**15, 2**14, 2**13],
        [2**9, 2**10, 2**11, 2**12],
        [2**8, 2**7, 2**6, 2**5],
        [2**2, 2**2, 2**3, 2**4]
    ]
boardLen = 4
'''

def spawn(cheat):
    global board
    list = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 0:
                list.append([y, x])
    
    if len(list) <= 1:
        cell = list[0]
    else:
        cell = list[randrange(0, len(list))]
    board[cell[0]].pop(cell[1])
    if cheat == 4:
        board[cell[0]].insert(cell[1], 4)
    elif cheat == 2:
        board[cell[0]].insert(cell[1], 2)
    else:
        board[cell[0]].insert(cell[1], choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4]))


def move(key):
    global board
    oldBoard = []
    for y in range(boardLen):
        oldBoard.append([])
        for x in range(boardLen):
            oldBoard[y].append(0)
    
    for y in range(len(board)):
        for x in range(len(board[y])):
            oldBoard[y][x] = board[y][x]

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
            board[i] = row
    
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
            board[i] = column
        board = rotate(board)


def merge(key):
    global board
    
    if key == "r":
        for y in range(len(board)):
            for x in range(len(board[y]) - 1, 0, -1):
                mainCell = board[y][x]
                secondaryCell = board[y][x - 1]
                if mainCell == secondaryCell:
                    board[y][x] = mainCell + secondaryCell
                    board[y][x - 1] = 0
    
    if key == "l":
        for y in range(len(board)):
            for x in range(len(board[y]) - 1):
                mainCell = board[y][x]
                secondaryCell = board[y][x + 1]
                if mainCell == secondaryCell:
                    board[y][x] = mainCell + secondaryCell
                    board[y][x + 1] = 0

    if key == "d":
        for y in range(len(board) - 1, 0, -1):
            for x in range(len(board[y])):
                mainCell = board[y][x]
                secondaryCell = board[y - 1][x]
                if mainCell == secondaryCell:
                    board[y][x] = mainCell + secondaryCell
                    board[y - 1][x] = 0
    
    if key == "u":
        for y in range(len(board) - 1):
            for x in range(len(board[y])):
                mainCell = board[y][x]
                secondaryCell = board[y + 1][x]
                if mainCell == secondaryCell:
                    board[y][x] = mainCell + secondaryCell
                    board[y + 1][x] = 0


def draw(board):
    text = ""
    list = []
    lenght = 0

    for y in range(len(board)):
        for x in range(len(board[y])):
            if lenght < len(str(board[y][x])):
                lenght = len(str(board[y][x]))
    
    list.append(".——" + (boardLen-1)*(lenght*"—" + ".——") + lenght*"—" + ".\n")
    for y in range(len(board)):
        list.append("| ")
        for x in range(len(board[y])):
            if board[y][x] != 0:
                cell = paint(str(board[y][x]), int((log(board[y][x], 2)+1)//2)+1)
            else:
                cell = paint(" ", 0)
            c = " "*(((lenght+10) - len(cell))//2) + cell + " "*((lenght+10) - len(cell) - ((lenght+10) - len(cell))//2)
            list.append(c)
            if x<len(board[y])-1:
                list.append(" | ")
        list.append(" |\n")
        if y<len(board)-1:
            list.append("|——" + (boardLen-1)*(lenght*"—" + ".——") + lenght*"—" + "|\n")
        else:
            list.append("'——" + (boardLen-1)*(lenght*"—" + "'——") + lenght*"—" + "'\n")
    for t in list:
        text += t
    os.system(f"mode {(lenght+3)*boardLen+1},{boardLen*2+3}")
    print(f"\n{text}")


def quit():
    global run
    if is_pressed("esc"):
        run = False


def main():
    spawn(0)
    spawn(0)
    os.system('cls')
    draw(board)
    
    while run:
        quit()
        if run == False:
            break

        hehe = 0
        if is_pressed("2"):
            hehe = 2
        elif is_pressed("4"):
            hehe = 4
        
        if is_pressed("right"):
            if pressed == "r":
                pressed = "!r"
            elif pressed != "!r":
                pressed = "r"
        elif is_pressed("left"):
            if pressed == "l":
                pressed = "!l"
            elif pressed != "!l":
                pressed = "l"
        elif is_pressed("up"):
            if pressed == "u":
                pressed = "!u"
            elif pressed != "!u":
                pressed = "u"
        elif is_pressed("down"):
            if pressed == "d":
                pressed = "!d"
            elif pressed != "!d":
                pressed = "d"
        elif is_pressed("backspace"):
            if pressed == "b":
                pressed = "!b"
            elif pressed != "!b":
                pressed = "b"
        else:
            pressed = ""

        if pressed in ("r", "l", "u", "d"):
            for y in range(len(board)):
                for x in range(len(board[y])):
                    temp[y][x] = board[y][x]
            move(pressed)
            merge(pressed)
            move(pressed)
            if is_same(board, temp):
                for y in range(len(temp)):
                    for x in range(len(temp[y])):
                        savedBoard[y][x] = temp[y][x]
                spawn(hehe)
                os.system('cls')
                draw(board)
        elif pressed == "b":
            for y in range(len(savedBoard)):
                for x in range(len(savedBoard[y])):
                    board[y][x] = savedBoard[y][x]
            os.system('cls')
            draw(board)
        sleep(1/FPS)
    

if __name__ == '__main__':
    main()
