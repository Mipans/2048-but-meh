
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
