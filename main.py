from math import log
from time import sleep
from random import randrange, choice
from functions import rotate, is_same, paint

FPS = 60
boardLen = 4
mode = "menu"
run = True
saveFile = open("data", "a").close

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

    if key in ("d", "a"):
        for i in range(len(board)):
            row = board[i]
            zero_count = row.count(0)
            if zero_count > 0:
                for n in range(zero_count):
                    row.remove(0)
                for n in range(zero_count):
                    if key == "d":
                        row.insert(0, 0)
                    if key == "a":
                        row.append(0)
            board[i] = row
    
    if key in ("w", "s"):
        board = rotate(board)
        for i in range(len(board)):
            column = board[i]
            zero_count = column.count(0)
            if zero_count > 0:
                for n in range(zero_count):
                    column.remove(0)
                for n in range(zero_count):
                    if key == "s":
                        column.insert(0, 0)
                    if key == "w":
                        column.append(0)
            board[i] = column
        board = rotate(board)


def merge(key):
    global board
    
    if key == "d":
        for y in range(len(board)):
            for x in range(len(board[y]) - 1, 0, -1):
                mainCell = board[y][x]
                secondaryCell = board[y][x - 1]
                if mainCell == secondaryCell:
                    board[y][x] = mainCell + secondaryCell
                    board[y][x - 1] = 0
    
    if key == "a":
        for y in range(len(board)):
            for x in range(len(board[y]) - 1):
                mainCell = board[y][x]
                secondaryCell = board[y][x + 1]
                if mainCell == secondaryCell:
                    board[y][x] = mainCell + secondaryCell
                    board[y][x + 1] = 0

    if key == "s":
        for y in range(len(board) - 1, 0, -1):
            for x in range(len(board[y])):
                mainCell = board[y][x]
                secondaryCell = board[y - 1][x]
                if mainCell == secondaryCell:
                    board[y][x] = mainCell + secondaryCell
                    board[y - 1][x] = 0
    
    if key == "w":
        for y in range(len(board) - 1):
            for x in range(len(board[y])):
                mainCell = board[y][x]
                secondaryCell = board[y + 1][x]
                if mainCell == secondaryCell:
                    board[y][x] = mainCell + secondaryCell
                    board[y + 1][x] = 0


def menu(sel):
    global mode, board, run
    if sel == 0:
        mode = "game"
        load_game()
        draw_board(board)
    
    elif sel == 1:
        mode = "game"
        for y in range(boardLen):
            for x in range(boardLen):
                board[y][x] = 0
        spawn(0)
        spawn(0)
        draw_board(board)

    elif sel == 2:
        run = False

def draw_board(board):
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
            list.append("|——" + (boardLen-1)*(lenght*"—" + "+——") + lenght*"—" + "|\n")
        else:
            list.append("'——" + (boardLen-1)*(lenght*"—" + "'——") + lenght*"—" + "'\n")
    for t in list:
        text += t
    print(f"\n{text}")


def draw_menu(sel):
    if sel == 0: arrow = [">", " ", " "]
    if sel == 1: arrow = [" ", ">", " "]
    if sel == 2: arrow = [" ", " ", ">"]
    print(
    f"""
 .———————————————————————.
 |  ___  ____   __  ___  |
 | (__ \/    \ /  || _ | |
 | / __/| [] |/_' || _ | |
 | \___)\____/  |_||___| |
 |                       |
 '———————————————————————'

{arrow[0]} CONTINIUE
{arrow[1]} RESET
{arrow[2]} QUIT
    """)


def save_game():
    # save the current board
    cells = list()
    for y in range(boardLen):
        row = board[y]
        for x in range(len(row)):
            cell = row[x]
            cells.append(str(cell)+'\n')
            
    saveFile = open("data", "w")
    saveFile.writelines(cells)
    saveFile.close()


def load_game():
    global board
    # load the previously saved game
    saveFile = open("data", "r")
    content = saveFile.readlines()
    saveFile.close()
    cells = []
    for i in range(boardLen**2):
        cells.append(int(content[i]))
    for y in range(boardLen):
        row = list()
        for x in range(boardLen):
            row.append(cells[y*boardLen+x])
        board[y] = row.copy()


def main():
    global mode
    run = True
    pressed = ""
    selected = 0
    draw_menu(selected)
    
    while run:

        if run == False:
            break

        # MENU
        if mode == "menu":

            pressed = input("\nup/down/enter : ")
            
            if pressed == "up":
                if selected > 0: selected -= 1
                else: selected = 2
                draw_menu(selected)

            elif pressed == "down":
                if selected < 2: selected += 1
                else: selected = 0
                draw_menu(selected)
            
            elif pressed == "enter":
                menu(selected)

        # GAME
        elif mode == "game":
            pressed = input("\nw/a/s/d/undo/save/load/menu/quit : ")
            hehe = 0
            if pressed.find("4") != -1:
                hehe = 4
                pressed = pressed.replace("4", "")
            elif pressed.find("2") != -1:
                hehe = 2
                pressed = pressed.replace("2", "")

            if pressed == "menu":
                mode = "menu"
                draw_menu(0)
            
            if pressed == "quit":
                run = False

            if pressed in ("d", "a", "w", "s"):
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
                    draw_board(board)

            elif pressed == "undo":
                for y in range(len(savedBoard)):
                    for x in range(len(savedBoard[y])):
                        board[y][x] = savedBoard[y][x]
                draw_board(board)

            elif pressed == "load":
                load_game()
                draw_board(board)
            elif pressed == "save":
                save_game()

        pressed = ""
        print(mode)
        sleep(1/FPS)
    

if __name__ == '__main__':
    main()
