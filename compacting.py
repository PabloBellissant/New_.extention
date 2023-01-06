


def simpleValue(val1, val2):
    if(str(val1).__contains__("-")):
        return val2
    strVal1 = str(val1)
    strVal2 = str(val2)
    cutPlace = 0
    if(strVal2[:-1] == strVal1[:-1]):
        return strVal2[len(strVal2)-1]
    for i in range(len(strVal1)):
        if(strVal1[i] != strVal2[i]):
            if(int(strVal1[i]) == int(strVal2[i])-1 and strVal2[-1:] <= strVal1[-1:]):
                return strVal2[i+1:]
            else:
                return strVal2[i:]
                break

def compacty(list):
    newList = list
    for i in range(len(list)-1):
        casual = len(list)-i-1
        val2 = list[casual]
        val1 = list[casual-1]
        newList[casual] = simpleValue(val1, val2)

    for i in range(len(newList)):
        list[i] = str(list[i])
        string = "/".join([str(x) for x in list])
    return [string]