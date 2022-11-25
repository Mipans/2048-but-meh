def rotate(oldList):
    newList = []
    for x in range(len(oldList)):
        column = []
        for y in range(len(oldList[x])):
            column.append(oldList[y][x])
        newList.append(column)
    return newList


def is_same(list1, list2):
    for y in range(len(list1)):
        for x in range(len(list1[y])):
            if list2[y][x] != list1[y][x]:
                return True
    return False


def draw_list(oldList):
    text = ""
    list = []
    
    for y in range(len(oldList)):
        list.append("[")
        for x in range(len(oldList[y])):
            cell = str(oldList[y][x])
            cell = paint(cell, oldList[y][x])
            list.append(cell)
            list.append(" ")
        list.append("]\n")
    
    for t in list:
        text += t
    print(f"{text}\n")


def paint(text, color):
    if isinstance(color, str):
        color = color.lower()
    if str(color) in ("black"):
        color = 0
    if str(color) in ("grey"):
        color = 1 
    if str(color) in ("white"):
        color = 2
    if str(color) in ("dark&red", "darkred", "dark red", "brown"):
        color = 3
    if str(color) in ("light_red", "lightred", "light red", "red"):
        color = 4
    if str(color) in ("dark_yellow", "darkyellow", "dark yellow", "orange"):
        color = 5
    if str(color) in ("light_yellow", "lightyellow", "light yellow", "yellow"):
        color = 6
    if str(color) in ("light_green", "lightgreen", "light green", "lime"):
        color = 7
    if str(color) in ("dark_green", "darkgreen", "dark green", "green"):
        color = 8
    if str(color) in ("light_cyan", "lightcyan", "light cyan", "cyan"):
        color = 9
    if str(color) in ("dark_cyan", "darkcyan", "dark cyan"):
        color = 10
    if str(color) in ("light_blue", "lightblue", "light blue"):
        color = 11
    if str(color) in ("dark_blue", "darkblue", "dark blue", "blue"):
        color = 12
    if str(color) in ("purple"):
        color = 13
    if str(color) in ("pink"):
        color = 14
    BLACK      = '\033[30m'
    GREY       = '\033[90m'
    WHITE      = '\033[37m'
    RED        = '\033[31m'
    LIGHTRED   = '\033[91m'
    DARKYELLOW = '\033[33m'
    YELLOW     = '\033[93m'
    LIGHTGREEN = '\033[92m'
    GREEN      = '\033[32m'
    LIGHTCYAN  = '\033[96m'
    CYAN       = '\033[36m'
    LIGHTBLUE  = '\033[94m'
    BLUE       = '\033[34m'
    PURPLE     = '\033[35m'
    PINK       = '\033[95m'
    colors = [BLACK, GREY, WHITE, LIGHTRED, RED, YELLOW, DARKYELLOW, LIGHTGREEN, GREEN, LIGHTCYAN, CYAN, LIGHTBLUE, BLUE, PURPLE, PINK]
    return colors[color] + str(text) + WHITE


def main():
    board = [
        [0 , 1 , 2 , 3 ],
        [4 , 5 , 6 , 7 ]
    ]
    draw_list(board)

    print(paint("███", 0))
    print(paint("███", 1))
    print(paint("███", 2))
    print(paint("███", 3))
    print(paint("███", 4))
    print(paint("███", 5))
    print(paint("███", 6))
    print(paint("███", 7))
    print(paint("███", 8))
    print(paint("███", 9))
    print(paint("███", 10))
    print(paint("███", 11))
    print(paint("███", 12))
    print(paint("███", 13))
    print(paint("███", 14))
    time.sleep(999)

if __name__ == '__main__':
    import time 
    main()