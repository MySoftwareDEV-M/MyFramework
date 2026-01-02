import MyFramework.DE   as DE
import MyFramework.Data as Data
import json

xml = "&lt;mxGraphModel&gt;&lt;root&gt;&lt;mxCell id=\"0\"/&gt;&lt;mxCell id=\"1\" parent=\"0\"/&gt;&lt;object label=\"Table*\" name=\"DB Table\" id=\"2\"&gt;&lt;mxCell style=\"shape=table;startSize=20;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;\" vertex=\"1\" parent=\"1\"&gt;&lt;mxGeometry y=\"1.1368683772161603e-13\" width=\"280\" height=\"40\" as=\"geometry\"/&gt;&lt;/mxCell&gt;&lt;/object&gt;&lt;object label=\"\" name=\"DB Column\" id=\"3\"&gt;&lt;mxCell style=\"shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;\" vertex=\"1\" parent=\"2\"&gt;&lt;mxGeometry y=\"20\" width=\"280\" height=\"20\" as=\"geometry\"/&gt;&lt;/mxCell&gt;&lt;/object&gt;&lt;mxCell id=\"4\" value=\"000 FK, PK N\" style=\"shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=0;overflow=hidden;whiteSpace=wrap;html=1;\" vertex=\"1\" parent=\"3\"&gt;&lt;mxGeometry width=\"80\" height=\"20\" as=\"geometry\"&gt;&lt;mxRectangle width=\"80\" height=\"20\" as=\"alternateBounds\"/&gt;&lt;/mxGeometry&gt;&lt;/mxCell&gt;&lt;mxCell id=\"5\" value=\"UniqueID*\" style=\"shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=0;overflow=hidden;whiteSpace=wrap;html=1;\" vertex=\"1\" parent=\"3\"&gt;&lt;mxGeometry x=\"80\" width=\"200\" height=\"20\" as=\"geometry\"&gt;&lt;mxRectangle width=\"200\" height=\"20\" as=\"alternateBounds\"/&gt;&lt;/mxGeometry&gt;&lt;/mxCell&gt;&lt;/root&gt;&lt;/mxGraphModel&gt;"

dicts = []

def addUniqueSet(aSet):
    for entry in dicts:
        if(entry == aSet):
            return
    dicts.append(aSet)

def sortByNames(dicts):
    tmp = {}
    for aSet in list(dicts):
        name = ""
        for i in aSet:
            if(i.startswith("<<DICT>>")):
                name = i
                aSet.remove(name)
                break

        Data.addListToDict(tmp, name, aSet)

    return tmp

def evaluate(dicts):
    bases       = []    # List, in der die Basen der Dictionaries erfasst werden.
    extensions  = []    # List, in der die Erweiterungen von Basen erfasst werden.

    step = 0
    while(len(dicts) > 0):
        step = step + 1
        for aSet in dicts:
            isSubset = False

            if(len(aSet) == step):
                print("\nDO: " + str(aSet))
                for base in bases:
                    if base.issubset(aSet):
                        isSubset = True

                for extension in extensions:
                    if extension.issubset(aSet):
                        isSubset = True

                if isSubset:
                    print("\tEXTENSION: " + str(aSet))
                    extensions.append(aSet)
                else:
                    print("\tBASE: " + str(aSet))
                    bases.append(aSet)

        for aSet in bases:
            if(aSet in dicts):
                dicts.remove(aSet)

        for aSet in extensions:
            if(aSet in dicts):
                dicts.remove(aSet)

        print("")
        print(str(step) + " STEP ###################################")
        print("==> bases:")
        Data.printNice(bases)
        print("--------------------")
        print("==> extensions:")
        Data.printNice(extensions)
        print("--------------------")
        print("==> dicts:")
        print(len(dicts))
        Data.printNice(dicts)



def getKeys(de : DE):

    if (de.type() == dict):
        aDict = set()
        for child in de.children():
            aDict.add(child.key())

        if(de.key()):
            aDict.add("<<DICT>>" + de.key())
        addUniqueSet(aDict)

    # if (de.type() == list):
    #     aDict = set()
    #     for child in de.children():
    #         aDict.add(child.key())

    #     if(de.key()):
    #         aDict.add("<<LIST>>" + de.key())
    #     addUniqueSet(aDict)

    for child in de.children():
        getKeys(child)


de_mxCell = DE.DE(xml, ["xml", "mxGraphModel", "root", "mxCell"])
print(de_mxCell.dumps())
# print(de_mxCell.dumps("no types"))
# print(de_mxCell.dumps("no values"))
# print(de_mxCell.dumps("no values, no types"))
getKeys(de_mxCell)


# de_object = DE.DE(xml, ["xml", "mxGraphModel", "root", "object"])
# print(de_object.dumps())
# # print(de_object.dumps("no types"))
# # print(de_object.dumps("no values"))
# # print(de_object.dumps("no values, no types"))
# getKeys(de_object)

dictsByName = sortByNames(dicts)
dicts = sorted(dicts, key=len, reverse=True)



# print("#####################################")
# print(len(dictsByName))
# for name in list(dictsByName):
#     print(name)
#     tmp = sorted(dictsByName[name], key=len, reverse=True)
#     for entry in list(tmp):
#         print(" - " + str(entry))

# print("#####################################")
# print(len(dicts))
# for entry in list(dicts):
#     print(entry)

# print("#####################################")
# evaluate(dicts)

# Datenstrukturen erkennen
# - Basis: '@width', '@height', '@as',
# - Erweiterungen:
#   ==> '@width', '@height', '@as', 'mxRectangle'
#   ==> '@width', '@height', '@as', 'mxRectangle', '@x'
# - Varianten:
#   Basis: '@id'
#   ==> '@id'   >>> Variante A: '@parent'
#   ==> '@id'   >>> Variante A: '@parent' Erweiterung: '@style', '@vertex', 'mxGeometry', '@value'
#   ==> '@id'   >>> Variante B: '@label', '@name', 'mxCell'


# - oneTimer
#   ==> Einträge, die nur einmal und auch nur als einzelner Wert vorkommen
