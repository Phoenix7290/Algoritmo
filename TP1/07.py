def selectAStrings(array):
    newArray = []
    for i in range(len(array)):
        if array[i].startswith("a"):
            newArray.append(array[i])
    return newArray

