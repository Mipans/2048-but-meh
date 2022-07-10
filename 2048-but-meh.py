from keyboard import is_pressed
from time import sleep
from random import randrange, choice
from list_manipulation_functions import rotate, legal

FPS = 60
run = True
'''
board = [
        [131072, 65536, 32768, 16384],
        [8192, 4096, 2048, 1024],
        [64, 128, 256, 512],
        [32, 16, 0, 0]
    ]
'''
(board, savedBoard, temp, boardLen) = ([], [], [], 4)
for y in range(boardLen):
    board.append([])
    savedBoard.append([])
    temp.append([])
    for x in range(boardLen):
        board[y].append(0)
        savedBoard[y].append(0)
        temp[y].append(0)


def spawn():
    global board
    list = []
    for y in range(0, len(board)):
        for x in range(0, len(board[y])):
            if board[y][x] == 0:
                list.append([y, x])
    
    if len(list) <= 1:
        cell = list[0]
    else:
        cell = list[randrange(0, len(list)-1)]
    board[cell[0]].pop(cell[1])
    board[cell[0]].insert(cell[1], choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4]))


def move(key, n):
    global board, suc
    if n == 1:
        suc = False
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

    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] != oldBoard[y][x]:
                suc = True


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


def undo(save):
    global board
    for y in range(len(save)):
        for x in range(len(save[y])):
            board[y][x] = save[y][x]


def draw(board):
    text = ""
    list = []
    lenght = 0

    for y in range(len(board)):
        for x in range(len(board[y])):
            if lenght < len(str(board[y][x])):
                lenght = len(str(board[y][x]))

    for y in range(len(board)):
        list.append("[")
        for x in range(len(board[y])):
            cell = str(board[y][x])
            if cell == "0":
                cell = "_"
            c = " "*((lenght - len(cell))//2) + cell + " "*(lenght - len(cell) - (lenght - len(cell))//2)
            list.append(c)
            list.append(" ")
        list.append("]\n")
    
    for t in list:
        text += t
    text.replace("0", "_")
    print(f"{text}\n")


def quit():
    global run
    if is_pressed("esc"):
        run = False


def main():
    spawn()
    draw(board)
    suc = False
    
    while run:
        quit()
        if run == False:
            break
        
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
            move(pressed, 1)
            merge(pressed)
            move(pressed, 2)
            suc = legal(board, temp)
            if suc:
                for y in range(len(temp)):
                    for x in range(len(temp[y])):
                        savedBoard[y][x] = temp[y][x]
                spawn()
                draw(board)
        elif pressed == "b":
            undo(savedBoard)
            draw(board)
            
        sleep(1/FPS)
    

if __name__ == '__main__':
    main()