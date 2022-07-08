
def rotate(oldList):
    newList = []
    for x in range(len(oldList)):
        column = []
        for y in range(len(oldList[x])):
            column.append(oldList[y][x])
        newList.append(column)
    return newList


def mirror_x(oldList):
    newList = []
    for y in range(len(oldList)):
        row = []
        for x in range(len(oldList[y])):
            row.insert(0, oldList[y][x])
        newList.append(row)
    return newList


def mirror_y(oldList):
    newList = []
    for y in range(len(oldList)):
        row = []
        for x in range(len(oldList[y])):
            row.append(oldList[y][x])
        newList.insert(0, row)
    return newList


def legal(list1, list2):
    for y in range(len(list1)):
        for x in range(len(list1[y])):
            if list2[y][x] != list1[y][x]:
                return True
    return False


def draw(oldList):
    text = ""
    list = []
    
    for y in range(len(oldList)):
        list.append("[")
        for x in range(len(oldList[y])):
            cell = str(oldList[y][x])
            list.append(cell)
            list.append(" ")
        list.append("]\n")
    
    for t in list:
        text += t
    print(f"{text}\n")


def main():
    board = [
        [0, 1, 0, 0],
        [4, 0, 0, 0],
        [0, 0, 10, 0],
        [0, 13, 0, 0]
    ]

    print(" " + str(board).replace(",", "").replace("[[", "[").replace("]]", "]").replace("]", "]\n"))
    print("\n\n " + str(mirror_x(board)).replace(",", "").replace("[[", "[").replace("]]", "]").replace("]", "]\n"))
    print("\n\n " + str(mirror_y(board)).replace(",", "").replace("[[", "[").replace("]]", "]").replace("]", "]\n"))
    print("\n\n " + str(mirror_y(mirror_x(board))).replace(",", "").replace("[[", "[").replace("]]", "]").replace("]", "]\n"))
    print("\n\n " + str(rotate(board)).replace(",", "").replace("[[", "[").replace("]]", "]").replace("]", "]\n"))

    print("\n\n\nHellu:\n")
    draw(board)


if __name__ == '__main__':
    main()