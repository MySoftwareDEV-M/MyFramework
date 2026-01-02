import ast
import html
import inspect
import json
import xmltodict

def addListToDict(aDict : dict, key : str, value):
    """
    Erzeugt ein key-value-Paar, wenn zu dem Key noch keines besteht.
    Der value wird in eine Liste eingefügt.
    Wenn bereits ein key-value-Paar besteht, wird der value der Liste angehangen.

    Args:
        aDict (dict): Das Dictionary, in dem das key-value-Paar zeugt oder ergänzt werden soll
        key (str): Key zu der Liste, die erzeugt oder ergänzt werden soll
        value (beliebig): Value, der in der Liste hinzugefügt werden soll
    """
    try:
        theList = aDict[key]
        theList.append(value)
        aDict[key] = theList
    except:
        aDict[key] = [value]

def countInDict(countDict : dict, value):
    """
    Über das countDict werden die values gezählt. Wenn der value noch nicht enthalten ist, wird
    er hinzugefüht mit mit der Anzahl 1 vermerkt.
    Wenn der value bereits enthalten ist, wird dessen Anzahl um 1 inkrementiert.

    Args:
        countDict (dict): Das Dictionary, in dem die values gezählt werden.
        value (beliebig): Value, der gezählt wird.
    """
    try:
        count = countDict[value]
        count = count +1
        countDict[value] = count
    except:
        countDict[value] = 1

def copyArguments(sourceDict : dict) -> dict:
    """
    Creates a Dictionary which contains all the Arguments, the keys starting wird "@",
    within the sourceDict.
    Args:
        sourceDict (dict): Dictionary to be copied.

    Returns:
        dict: Dictionary, only containing the key value pairs whies keys start with "@"
    """
    result = {}
    for key in sourceDict.keys():
        if(key[0] == "@"):
            result[key] = sourceDict[key]

    return result

def printNice(content, highlighting = "", addFileInfo = True):
    """
    Gibt dicts über json.dumps() mit einem indent = 3 aus.
    Gibt lists als liste aus.
    Args:
        content (): Content, der über json.dumps() ausgegeben werden kann.
    """

    currentFrame = inspect.currentframe()
    # a list of al the frames / calles, that lead to the call of this function
    callingFrame = inspect.getouterframes(currentFrame, 2)
    # we are interessted in the function that called the announce...() functions
    try:
        frameInfo = callingFrame[1]
        func = "> " + frameInfo.function + "()"
    except:
        frameInfo = callingFrame[1]
        func = ""

    filename = str(frameInfo.filename).split("\\")
    filename = filename[len(filename)-1]

    if(highlighting != ""):
        fileInfo = ""
        if(addFileInfo):
            fileInfo = " (" + filename + func + " in line = " + str(frameInfo.lineno) + ")"

        print("######################################################################")
        print(highlighting + fileInfo + " ==>")
        if(type(content) == dict):
            print(json.dumps(content, indent = 3))
        elif(type(content) == list):
            for entry in content:
                print(entry)
        print("<== " + highlighting)
        print("######################################################################")
    else:
        if(type(content) == dict):
            print(json.dumps(content, indent = 3))
        elif(type(content) == list):
            for entry in content:
                print(entry)
