
def rotate(oldList):
    newList = []
    for x in range(4):
        column = []
        for y in range(4):
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


if __name__ == '__main__':
    main()