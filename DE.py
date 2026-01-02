import ast
import html
import json
import xmltodict

class DE():
    """

    """
    ###############################################################################################
    # class variables
    __dumpStringLength = 30
    __indent = "..."
    __indentDict = "|  "
    __indentDictElement = "|__"
    __indentList = ":  "
    __indentListElement = ":.."

    __infos = []

    ###############################################################################################
    # private functions
    #----------------------------------------------------------------------------------------------
    def __dumpForParent(self, indent : str, mode) -> str:
        text  = ""

        if( ("no types" in mode) and ("no values" in mode) ):
            text = ""
        else:
            text  = indent
            if ("no types" not in mode):
                text = text + self.__typeAsSimpleString()

                if(self.__convertedString):
                    text += " (converted String)"

            if("no values" not in mode):
                if( (self.__type != dict) and (self.__type != list) and (type(self.__type) != str)):
                    if(self.__value == None):
                        text += ": "
                    else:
                        tmp = str(self.__value)
                        if(len(tmp) > self.__dumpStringLength):
                            tmp = tmp[0:self.__dumpStringLength] + "..."
                        text += ": " + tmp
            text += "\n"

        numOfChildren = len(self.__children)
        for i in range(numOfChildren):
            child = self.__children[i]

            indent = indent.replace(".", " ")
            if(self.__type == dict):
                text += indent + self.__indentDictElement + child.__key + ":"
                if(i == numOfChildren-1):
                    text += "\n" + child.__dumpForParent(indent + "   ", mode)
                else:
                    text += "\n" + child.__dumpForParent(indent + self.__indentDict, mode)

            elif(self.__type == list):
                text += indent + self.__indentListElement + "[" + str(i) + "]:"
                if(i == numOfChildren-1):
                    text += "\n" + child.__dumpForParent(indent + "   ", mode)
                else:
                    text += "\n" + child.__dumpForParent(indent + self.__indentList, mode)

            elif( (self.__type == tuple) or (self.__type == set) or (self.__type == frozenset) or (type(self.__type) == str) ):
                text += child.__dumpForParent(indent + self.__indent, mode)

            else:
                text += child.__dumpForParent(indent + self.__indent, mode)
        return text

    # def __dumpForParent(self, indent : str, mode) -> str:
    #     text  = indent

    #     if("no types" not in mode):
    #         text = text + self.__typeAsSimpleString()

    #         if(self.__convertedString):
    #             text += " (converted String)"

    #     if("no values" not in mode):
    #         if( (self.__type != dict) and (self.__type != list) and (type(self.__type) != str)):
    #             if(self.__value == None):
    #                 text += ": "
    #             else:
    #                 tmp = str(self.__value)
    #                 if(len(tmp) > self.__dumpStringLength):
    #                     tmp = tmp[0:self.__dumpStringLength] + "..."
    #                 text += ": " + tmp

    #     numOfChildren = len(self.__children)
    #     for i in range(numOfChildren):
    #         child = self.__children[i]

    #         indent = indent.replace(".", " ")
    #         if(self.__type == dict):
    #             text += "\n" + indent + self.__indentDictElement + child.__key + ":"
    #             if(i == numOfChildren-1):
    #                 text += "\n" + child.__dumpForParent(indent + "   ", mode)
    #             else:
    #                 text += "\n" + child.__dumpForParent(indent + self.__indentDict, mode)

    #         elif(self.__type == list):
    #             text += "\n" + indent + self.__indentListElement + "[" + str(i) + "]:"
    #             if(i == numOfChildren-1):
    #                 text += "\n" + child.__dumpForParent(indent + "   ", mode)
    #             else:
    #                 text += "\n" + child.__dumpForParent(indent + self.__indentList, mode)

    #         elif( (self.__type == tuple) or (self.__type == set) or (self.__type == frozenset) or (type(self.__type) == str) ):
    #             text += "\n" + child.__dumpForParent(indent + self.__indent, mode)

    #         else:
    #             text += "\n" + child.__dumpForParent(indent + self.__indent, mode)
    #     return text

    #----------------------------------------------------------------------------------------------
    def __init__(self, data, path : list = None):
        self.__children         = []
        self.__key              = ""
        self.__value            = ""
        self.__type             = None
        self.__convertedString  = False

        if(path == None):
            self.__parse(data)

        else:
            self.__value = data
            for element in path:
                result = self.__step(element)
                if(result == False):
                    self.__infos.append("Kein gültiger Pfad")
                    return

            self.__parse(self.__value)

    #----------------------------------------------------------------------------------------------
    def __step(self, element):
        self.__type = type(self.__value)
        # print("STEP: " + str(element) + " > " + str(self.__type))

        #------------------------------------------------------------------------------------------
        # Ein indizierbares Element: Bei Listen, Sets, ...
        if(type(element) == int):
            if( (self.__type == list) or (self.__type == tuple)
               or (self.__type == set) or (self.__type == frozenset) ):
                if( (element >= 0) and (element < len(self.__value)) ):
                    if(self.__type == set):
                        self.__infos.append("To index elements, set is converted to list.")

                    self.__value = list(self.__value)[element]
                    return True
                else:
                    self.__infos.append("Out of range in list. [Possible values 0 ... " + str(len(self.__value)-1) + "]")
                    return False

            if(self.__type == str):
                content = self.__tryLiteralEvalOfString(self.__value)
                if(content != None):
                    # known types, recognized by literal evaluations:
                    # complex, tupel, set
                    if( (type(content) == tuple) or (type(content) == set) or (type(content) == list) ):
                        if( (element >= 0) and (element < len(content)) ):
                            if(type(content) == set):
                                self.__infos.append("To index elements, set is converted to list.")

                            self.__value = list(content)[element]
                            return True
                        else:
                            self.__infos.append("Out of range in list. [Possible values 0 ... " + str(len(content)-1) + "]")
                            return False

                # Reaching this point means: It is just a string
                # return True
            self.__value = None
            return False
        #------------------------------------------------------------------------------------------
        # Ein Key in einem Dict
        elif(type(element) == str):
            # print("STEP > str: " + str(self.__type))
            if(self.__type == dict):
                if(element in self.__value):
                    self.__value = self.__value[element]
                    # print("STEP: AUSWERTUNG 1")
                    return True
                self.__infos.append("Key " + element + " not in dict")
                # print("STEP: KEINE AUSWERTUNG 1")
                return False

            if(self.__type == str):
                content = self.__tryString2Dict(self.__value)
                if(content != None):
                    if(type(content) == dict):
                        self.__value = content[element]
                        # print("STEP: AUSWERTUNG 2")
                        return True
                # print("STEP: KEINE AUSWERTUNG 2")

                if(element == "xml"):
                    content = self.__tryString2XML(self.__value)
                    if(content[0] != None):
                        self.__type = "xml [" + str(content[0]) + "]"
                        self.__value = content[1]
                        return True
            self.__value = None
            return False

        #------------------------------------------------------------------------------------------
        # Ein konkreter Type
        elif(type(element) == type):
            self.__value = None
            return False

        #------------------------------------------------------------------------------------------
        # Sollte nicht passieren
        else:
            self.__value = None
            return False

    #----------------------------------------------------------------------------------------------
    def __parse(self, data):
        self.__type = type(data)
    # ---------------------------------------------------------------------------------------------
    # SECTION NO STRINGS
        if( (self.__type == int) or (self.__type == float) or
            (self.__type == complex) or (self.__type == bool) or
            (self.__type == bytearray) or (self.__type == bytes) or
            (self.__type == type(None)) ):

            self.__value = data
            return


        if( (self.__type == list) or (self.__type == tuple)
           or (self.__type == set) or (self.__type == frozenset) ):
            self.__value = None
            self.__parseChildrenForList_Tuple_Set_FrozenSet(data)
            return


        if(self.__type == dict):
            self.__value = None
            self.__parseChildrenForDict(data)
            return

    # ---------------------------------------------------------------------------------------------
    # SECTION STRING
        if(self.__type == str):

            content = self.__tryString2Dict(data)
            if(content != None):
                if(type(content) == dict):
                    self.__type = dict
                    self.__convertedString = True
                    self.__value = None
                    self.__parseChildrenForDict(content)
                    return

            content = self.__tryLiteralEvalOfString(data)
            if(content != None):
                # known types, recognized by literal evaluations:
                # tupel, set, list
                if( (type(content) == tuple) or (type(content) == set) or (type(content) == list) ):
                    self.__type = type(content)
                    self.__convertedString = True
                    self.__value = None
                    self.__parseChildrenForList_Tuple_Set_FrozenSet(content)
                    return

                if(type(content) == complex):
                    self.__type = type(content)
                    self.__convertedString = True
                    self.__value = content
                    return

            if(data.startswith("bytearray(") and data.endswith(")")):
                data = data[10:]
                data = data[0:-1]
                content = self.__tryLiteralEvalOfString(data)
                if(content != None):
                    self.__type = bytearray
                    self.__convertedString = True
                    self.__value = content
                    return
            if(data.startswith("bytes(") and data.endswith(")")):
                data = data[6:]
                data = data[0:-1]
                content = self.__tryLiteralEvalOfString(data)
                if(content != None):
                    self.__type = bytes
                    self.__convertedString = True
                    self.__value = content
                    return

            if(data.startswith("frozenset(") and data.endswith(")")):
                data = data[10:]
                data = data[0:-1]
                content = self.__tryLiteralEvalOfString(data)
                if(content != None):
                    self.__type = frozenset
                    self.__convertedString = True
                    self.__value = None
                    self.__parseChildrenForList_Tuple_Set_FrozenSet(content)
                    return

            content = self.__tryString2XML(data)
            if(content[0] != None):
                self.__type = "xml [" + str(content[0]) + "]"
                self.__convertedString = True
                self.__value = None
                self.__children.append(DE(content[1]))
                return

            # If we come to this point, it' just a string :)
            self.__value = data
            return


        # If we made it this far, we missed something.
        if(data == None):
            return

        self.__value = "NOT IMPLEMENTED TYPE \"" + str(self.__type) + "\""

    #----------------------------------------------------------------------------------------------
    def __parseChildrenForDict(self, data):
        keys = list(data.keys())
        for key in keys:
            de = DE(data[key])
            de.__key = key
            self.__children.append(de)
            # self.__children.append( (key, DE(data[key]) ) )

    #----------------------------------------------------------------------------------------------
    def __parseChildrenForList_Tuple_Set_FrozenSet(self, data):
            for element in data:
                self.__children.append( DE(element) )

    #----------------------------------------------------------------------------------------------
    def __typeAsSimpleString(self) -> str:
        if(type(self.__type) == str):
            return self.__type

        output = str(self.__type)
        output = output[8:]
        output = output[0:-2]
        return output

    #----------------------------------------------------------------------------------------------
    def __tryString2Dict(self, data : str) -> dict:
        content = None
        try:
            content = json.loads(data)
        except:
            pass
        return content

    #----------------------------------------------------------------------------------------------
    def __tryLiteralEvalOfString(self, data : str) -> set:
        content = None
        try:
            content = ast.literal_eval(data)
        except:
            pass
        return content

    #----------------------------------------------------------------------------------------------
    def __tryString2XML(self, data : str) -> tuple:
        content = (None, None)
        try:
            content = ("direct", xmltodict.parse(data))
        except:
            try:
                data = html.unescape(data)
                content = ("escaped", xmltodict.parse(data))
            except:
                pass
        return content

    ###############################################################################################
    # Public functions
    #----------------------------------------------------------------------------------------------
    def children(self) -> list:
        return self.__children

    #----------------------------------------------------------------------------------------------
    def convertedString(self) -> bool:
        return self.__convertedString

    #----------------------------------------------------------------------------------------------
    def dumps(self, mode = "") -> str:
        return self.__dumpForParent("", mode)

    #----------------------------------------------------------------------------------------------
    def key(self) -> str:
        return self.__key

    #----------------------------------------------------------------------------------------------
    def infos(self) -> list:
        return self.__infos

    #----------------------------------------------------------------------------------------------
    def type(self) -> type:
        return self.__type

    #----------------------------------------------------------------------------------------------
    def value(self):
        return self.__value

###################################################################################################
# Public global functions / Helper functions
