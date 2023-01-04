

def getValue(list, rgbint, searchedValue):

    listValue = []
    for i in range (len(list)):
        if(list[i][rgbint] == searchedValue):
            listValue.append(i)
    return listValue