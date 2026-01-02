import unittest

import MyFramework.DE           as DE

# The general idea:
# Exhausting and somehow complete testing of so many possible combinations is difficult.
# Therefore I defined the data structure decoupled from the test definition.
# So the data structure represents an extensive data set with lots of variants.
#
# Then the tests can address different levels of detail ranging from basic data recognition to
# complex nested data structures, always applied to the same data structure.
#
# Also the tests can be defined in a recurring way and so they are easy to compare.
#

theData = {
    "STR"           : 'TEST STRING',
    "INT"           : 123,
    "FLOAT"         : 1.23,
    "COMPLEX"       : (3.4 + 7.8j),
    "BOOL"          : False,
    "NONE"          : None,
    "LIST"          : [1, 'a'],
    "LIST STR"      : "[1, 'a']",
    "TUPLE"         : (1, 'a'),
    "TUPLE STR"     : "(1, 'a')",
    "SET"           : {1, 'a'},
    "SET STR"       : "{1, 'a'}",
    "FROZENSET"     : frozenset([1,'a']),
    "FROZENSET STR" : "frozenset([1,'a'])",
    "BYTES"         : bytes('Python', 'utf-8'),
    "BYTES STR"     : "bytes('Python', 'utf-8')",
    "BYTEARRAY"     : bytearray([2, 3, 5, 7]),
    "BYTEARRAY STR" : "bytearray([2, 3, 5, 7])",
    "DICT"          : { 'KEY' : 'VALUE'},
    "DICT STR"      : '{"KEY" : "VALUE"}',
    "DICT EMPTY"    : {},
    "XML ESCAPED"   : "&lt;mxGraphModel key='value'&gt;VALUE&lt;/mxGraphModel&gt;",
    "XML UNESCAPED" : "<mxGraphModel key='value'>VALUE</mxGraphModel>",

    "ADDRESS DICT"    : {
        "SIMPLE ONES"   : {
            "STR"           : 'TEST STRING',
            "INT"           : 123,
            "FLOAT"         : 1.23,
            "COMPLEX"       : (3.4 + 7.8j),
            "BOOL"          : False,
            "NONE"          : None,
        },
        "LIST TUPLE SET DICT" : {
            "LIST"          : [1, 'a'],
            "LIST STR"      : "[1, 'a']",
            "TUPLE"         : (1, 'a'),
            "TUPLE STR"     : "(1, 'a')",
            "SET"           : {1, 'a'},
            "SET STR"       : "{1, 'a'}",
            "FROZENSET"     : frozenset([1,'a']),
            "FROZENSET STR" : "frozenset([1,'a'])",
            "DICT"          : { 'KEY' : 'VALUE'},
            "DICT STR"      : '{"KEY" : "VALUE"}',
        },
        "BYTE BYTEARRAY" : {
            "BYTES"         : bytes('Python', 'utf-8'),
            "BYTES STR"     : "bytes('Python', 'utf-8')",
            "BYTEARRAY"     : bytearray([2, 3, 5, 7]),
            "BYTEARRAY STR" : "bytearray([2, 3, 5, 7])",
        },
        "DICT EMPTY" : {
        },
        "XML" : {
            "XML ESCAPED"   : "&lt;mxGraphModel key='value'&gt;VALUE&lt;/mxGraphModel&gt;",
            "XML UNESCAPED" : "<mxGraphModel key='value'>VALUE</mxGraphModel>"
        }
    },

    "ADDRESS LIST"    : [
        'TEST STRING',          #"STR"
        123,                    #"INT"
        1.23,                   #"FLOAT"
        (3.4 + 7.8j),           #"COMPLEX"
        False,                  #"BOOL"
        None,                   #"NONE"
        [1, 'a'],               #"LIST"
        "[1, 'a']",             #"LIST STR"
        (1, 'a'),               #"TUPLE"
        "(1, 'a')",             #"TUPLE STR"
        {1, 'a'},               #"SET"
        "{1, 'a'}",             #"SET STR"
        frozenset([1,'a']),     #"FROZENSET"
        "frozenset([1,'a'])",   #"FROZENSET STR"
        { 'KEY' : 'VALUE'},     #"DICT"
        '{"KEY" : "VALUE"}',    #"DICT STR"
        bytes('Python', 'utf-8'),   #"BYTES"
        "bytes('Python', 'utf-8')", #"BYTES STR"
        bytearray([2, 3, 5, 7]),    #"BYTEARRAY"
        "bytearray([2, 3, 5, 7])",  #"BYTEARRAY STR"
        {},                         #"DICT EMPTY"
        "&lt;mxGraphModel key='value'&gt;VALUE&lt;/mxGraphModel&gt;",   #"XML ESCAPED"
        "<mxGraphModel key='value'>VALUE</mxGraphModel>"                #"XML UNESCAPED"
    ],

    "ADDRESS TUPLE"    : (
        'TEST STRING',          #"STR"
        123,                    #"INT"
        1.23,                   #"FLOAT"
        (3.4 + 7.8j),           #"COMPLEX"
        False,                  #"BOOL"
        None,                   #"NONE"
        [1, 'a'],               #"LIST"
        "[1, 'a']",             #"LIST STR"
        (1, 'a'),               #"TUPLE"
        "(1, 'a')",             #"TUPLE STR"
        {1, 'a'},               #"SET"
        "{1, 'a'}",             #"SET STR"
        frozenset([1,'a']),     #"FROZENSET"
        "frozenset([1,'a'])",   #"FROZENSET STR"
        { 'KEY' : 'VALUE'},     #"DICT"
        '{"KEY" : "VALUE"}',    #"DICT STR"
        bytes('Python', 'utf-8'),   #"BYTES"
        "bytes('Python', 'utf-8')", #"BYTES STR"
        bytearray([2, 3, 5, 7]),    #"BYTEARRAY"
        "bytearray([2, 3, 5, 7])",  #"BYTEARRAY STR"
        {},                         #"DICT EMPTY"
        "&lt;mxGraphModel key='value'&gt;VALUE&lt;/mxGraphModel&gt;",   #"XML ESCAPED"
        "<mxGraphModel key='value'>VALUE</mxGraphModel>"                #"XML UNESCAPED"
    )
}

basicTests = {
    "STR" : {
        "data"          : "STR",
        "dataExpected"  : "TEST STRING",
        "numChildren"   : 0,
        "type"          : str,
        "convertedStr"  : False,
        "dump"          : "str: TEST STRING\n",
        "dump_noValues" : "str\n"
    },
    "INT" : {
        "data"          : "INT",
        "dataExpected"  : 123,
        "numChildren"   : 0,
        "type"          : int,
        "convertedStr"  : False,
        "dump"          : "int: 123\n",
        "dump_noValues" : "int\n"
    },
    "FLOAT" : {
        "data"          : "FLOAT",
        "dataExpected"  : 1.23,
        "numChildren"   : 0,
        "type"          : float,
        "convertedStr"  : False,
        "dump"          : "float: 1.23\n",
        "dump_noValues" : "float\n"
    },
    "COMPLEX" : {
        "data"          : "COMPLEX",
        "dataExpected"  : (3.4 + 7.8j),
        "numChildren"   : 0,
        "type"          : complex,
        "convertedStr"  : False,
        "dump"          : "complex: (3.4+7.8j)\n",
        "dump_noValues" : "complex\n"
    },
    "BOOL" : {
        "data"          : "BOOL",
        "dataExpected"  : False,
        "numChildren"   : 0,
        "type"          : bool,
        "convertedStr"  : False,
        "dump"          : "bool: False\n",
        "dump_noValues" : "bool\n"
    },
    "NONE" : {
        "data"          : "NONE",
        "dataExpected"  : None,
        "numChildren"   : 0,
        "type"          : type(None),
        "convertedStr"  : False,
        "dump"          : "NoneType: \n",
        "dump_noValues" : "NoneType\n"
    },
    "LIST" : {
        "data"          : "LIST",
        "dataExpected"  : None,     # For the list data element there should be no value. The values should be assigned to the childten.
        "numChildren"   : 2,
        "type"          : list,
        "convertedStr"  : False,
        "dump"          : "list\n:..[0]:\n:  int: 1\n:..[1]:\n   str: a\n",
        "dump_noValues" : "list\n:..[0]:\n:  int\n:..[1]:\n   str\n"
    },
    "TUPLE" : {
        "data"          : "TUPLE",
        "dataExpected"  : None,     # For the tuple data element there should be no value. The values should be assigned to the childten.
        "numChildren"   : 2,
        "type"          : tuple,
        "convertedStr"  : False,
        "dump"          : "tuple: \n...int: 1\n...str: a\n",
        "dump_noValues" : "tuple\n...int\n...str\n"
    },
    "SET" : {       # From time to time, the test for the set
        "data"          : "SET",
        "dataExpected"  : None,     # For the set data element there should be no value. The values should be assigned to the childten.
        "numChildren"   : 2,
        "type"          : set,
        "convertedStr"  : False,
        "dump"          : "set: \n...int: 1\n...str: a\n",
        "dump_noValues" : "set\n...int\n...str\n"
    },
    "FROZENSET" : { # From time to time, the test for the frozen set
        "data"          : "FROZENSET",
        "dataExpected"  : None,     # For the frozenset data element there should be no value. The values should be assigned to the childten.
        "numChildren"   : 2,
        "type"          : frozenset,
        "convertedStr"  : False,
        "dump"          : "frozenset: \n...int: 1\n...str: a\n",
        "dump_noValues" : "frozenset\n...int\n...str\n"
    },
    "BYTES" : {
        "data"          : "BYTES",
        "dataExpected"  : bytes('Python', 'utf-8'),
        "numChildren"   : 0,
        "type"          : bytes,
        "convertedStr"  : False,
        "dump"          : "bytes: b'Python'\n",
        "dump_noValues" : "bytes\n"
    },
    "BYTEARRAY" : {
        "data"          : "BYTEARRAY",
        "dataExpected"  : bytearray([2, 3, 5, 7]),
        "numChildren"   : 0,
        "type"          : bytearray,
        "convertedStr"  : False,
        "dump"          : "bytearray: bytearray(b'\\x02\\x03\\x05\\x07')\n",
        "dump_noValues" : "bytearray\n"
    },
    "DICT" : {
        "data"          : "DICT",
        "dataExpected"  : None, # For the dict data element there should be no value. The values should be assigned to the childten.
        "numChildren"   : 1,
        "type"          : dict,
        "convertedStr"  : False,
        "dump"          : "dict\n|__KEY:\n   str: VALUE\n",
        "dump_noValues" : "dict\n|__KEY:\n   str\n"
    },
    "DICT EMPTY" : {
        "data"          : "DICT EMPTY",
        "dataExpected"  : None, # For the dict data element there should be no value. The values should be assigned to the childten.
        "numChildren"   : 0,
        "type"          : dict,
        "convertedStr"  : False,
        "dump"          : "dict\n",
        "dump_noValues" : "dict\n"
    },

    #----------------------------------------------------------------------------------------------
    # XML
    "XML ESCAPED" : {
        "data"          : "XML ESCAPED",
        "dataExpected"  : None, # For the xml data element there should be no value. The values should be assigned to the childten.
        "numChildren"   : 1,
        "type"          : 'xml [escaped]',  # This is not a real python type, but somethin I came up with
        "convertedStr"  : True,
        "dump"          : "xml [escaped] (converted String)\n...dict\n   |__mxGraphModel:\n      dict\n      |__@key:\n      |  str: value\n      |__#text:\n         str: VALUE\n",
        "dump_noValues" : "xml [escaped] (converted String)\n...dict\n   |__mxGraphModel:\n      dict\n      |__@key:\n      |  str\n      |__#text:\n         str\n"
    },
    "XML UNESCAPED" : {
        "data"          : "XML UNESCAPED",
        "dataExpected"  : None, # For the xml data element there should be no value. The values should be assigned to the childten.
        "numChildren"   : 1,
        "type"          : 'xml [direct]',  # This is not a real python type, but somethin I came up with
        "convertedStr"  : True,
        "dump"          : "xml [direct] (converted String)\n...dict\n   |__mxGraphModel:\n      dict\n      |__@key:\n      |  str: value\n      |__#text:\n         str: VALUE\n",
        "dump_noValues" : "xml [direct] (converted String)\n...dict\n   |__mxGraphModel:\n      dict\n      |__@key:\n      |  str\n      |__#text:\n         str\n"
    },

    #----------------------------------------------------------------------------------------------
    # String conversions
    "LIST STR" : {
        "data"          : "LIST STR",
        "dataExpected"  : None,     # For the list data element there should be no value. The values should be assigned to the childten.
        "numChildren"   : 2,
        "type"          : list,
        "convertedStr"  : True,
        "dump"          : "list (converted String)\n:..[0]:\n:  int: 1\n:..[1]:\n   str: a\n",
        "dump_noValues" : "list (converted String)\n:..[0]:\n:  int\n:..[1]:\n   str\n"
    },
    "TUPLE STR" : {
        "data"          : "TUPLE STR",
        "dataExpected"  : None,     # For the tuple data element there should be no value. The values should be assigned to the childten.
        "numChildren"   : 2,
        "type"          : tuple,
        "convertedStr"  : True,
        "dump"          : "tuple (converted String): \n...int: 1\n...str: a\n",
        "dump_noValues" : "tuple (converted String)\n...int\n...str\n"
    },
    "SET STR" : {       # From time to time, the test for the set
        "data"          : "SET STR",
        "dataExpected"  : None,     # For the set data element there should be no value. The values should be assigned to the childten.
        "numChildren"   : 2,
        "type"          : set,
        "convertedStr"  : True,
        "dump"          : "set (converted String): \n...int: 1\n...str: a\n",
        "dump_noValues" : "set (converted String)\n...int\n...str\n"
    },
    "FROZENSET STR" : { # From time to time, the test for the frozen set
        "data"          : "FROZENSET STR",
        "dataExpected"  : None,     # For the frozenset data element there should be no value. The values should be assigned to the childten.
        "numChildren"   : 2,
        "type"          : frozenset,
        "convertedStr"  : True,
        "dump"          : "frozenset (converted String): \n...int: 1\n...str: a\n",
        "dump_noValues" : "frozenset (converted String)\n...int\n...str\n"
    },
    "BYTES STR" : {
        "data"          : "BYTES STR",
        "dataExpected"  : ('Python', 'utf-8'),
        "numChildren"   : 0,
        "type"          : bytes,
        "convertedStr"  : True,
        "dump"          : "bytes (converted String): ('Python', 'utf-8')\n",
        "dump_noValues" : "bytes (converted String)\n"
    },
    "BYTEARRAY STR" : {
        "data"          : "BYTEARRAY STR",
        "dataExpected"  : [2, 3, 5, 7],
        "numChildren"   : 0,
        "type"          : bytearray,
        "convertedStr"  : True,
        "dump"          : "bytearray (converted String): [2, 3, 5, 7]\n",
        "dump_noValues" : "bytearray (converted String)\n"
    },
    "DICT STR" : {
        "data"          : "DICT STR",
        "dataExpected"  : None, # For the dict data element there should be no value. The values should be assigned to the childten.
        "numChildren"   : 1,
        "type"          : dict,
        "convertedStr"  : True,
        "dump"          : "dict (converted String)\n|__KEY:\n   str: VALUE\n",
        "dump_noValues" : "dict (converted String)\n|__KEY:\n   str\n"
    }
}

addressingTests = {
    # DICT ----------------------------------------------------------------------------------------
    "DICT STR" : {
        "path"      : ["ADDRESS DICT", "SIMPLE ONES", "STR"],
        "basicTests": "STR"
    },
    "DICT INT" : {
        "path"      : ["ADDRESS DICT", "SIMPLE ONES", "INT"],
        "basicTests": "INT"
    },
    "DICT FLOAT" : {
        "path"      : ["ADDRESS DICT", "SIMPLE ONES", "FLOAT"],
        "basicTests": "FLOAT"
    },
    "DICT COMPLEX" : {
        "path"      : ["ADDRESS DICT", "SIMPLE ONES", "COMPLEX"],
        "basicTests": "COMPLEX"
    },
    "DICT BOOL" : {
        "path"      : ["ADDRESS DICT", "SIMPLE ONES", "BOOL"],
        "basicTests": "BOOL"
    },
    "DICT NONE" : {
        "path"      : ["ADDRESS DICT", "SIMPLE ONES", "NONE"],
        "basicTests": "NONE"
    },
    "DICT LIST" : {
        "path"      : ["ADDRESS DICT", "LIST TUPLE SET DICT", "LIST"],
        "basicTests": "LIST"
    },
    "DICT LIST STR" : {
        "path"      : ["ADDRESS DICT", "LIST TUPLE SET DICT", "LIST STR"],
        "basicTests": "LIST STR"
    },
    "DICT TUPLE" : {
        "path"      : ["ADDRESS DICT", "LIST TUPLE SET DICT", "TUPLE"],
        "basicTests": "TUPLE"
    },
    "DICT TUPLE STR" : {
        "path"      : ["ADDRESS DICT", "LIST TUPLE SET DICT", "TUPLE STR"],
        "basicTests": "TUPLE STR"
    },
    "DICT SET" : {
        "path"      : ["ADDRESS DICT", "LIST TUPLE SET DICT", "SET"],
        "basicTests": "SET"
    },
    "DICT SET STR" : {
        "path"      : ["ADDRESS DICT", "LIST TUPLE SET DICT", "SET STR"],
        "basicTests": "SET STR"
    },
    "DICT FROZENSET" : {
        "path"      : ["ADDRESS DICT", "LIST TUPLE SET DICT", "FROZENSET"],
        "basicTests": "FROZENSET"
    },
    "DICT FROZENSET STR" : {
        "path"      : ["ADDRESS DICT", "LIST TUPLE SET DICT", "FROZENSET STR"],
        "basicTests": "FROZENSET STR"
    },
    "DICT DICT" : {
        "path"      : ["ADDRESS DICT", "LIST TUPLE SET DICT", "DICT"],
        "basicTests": "DICT"
    },
    "DICT DICT STR" : {
        "path"      : ["ADDRESS DICT", "LIST TUPLE SET DICT", "DICT STR"],
        "basicTests": "DICT STR"
    },
    "DICT BYTES" : {
        "path"      : ["ADDRESS DICT", "BYTE BYTEARRAY", "BYTES"],
        "basicTests": "BYTES"
    },
    "DICT BYTES STR" : {
        "path"      : ["ADDRESS DICT", "BYTE BYTEARRAY", "BYTES STR"],
        "basicTests": "BYTES STR"
    },
    "DICT BYTEARRAY" : {
        "path"      : ["ADDRESS DICT", "BYTE BYTEARRAY", "BYTEARRAY"],
        "basicTests": "BYTEARRAY"
    },
    "DICT BYTEARRAY STR" : {
        "path"      : ["ADDRESS DICT", "BYTE BYTEARRAY", "BYTEARRAY STR"],
        "basicTests": "BYTEARRAY STR"
    },
    "DICT EMPTY" : {
        "path"      : ["ADDRESS DICT", "DICT EMPTY"],
        "basicTests": "DICT EMPTY"
    },
    "DICT XML ESCAPED" : {
        "path"      : ["ADDRESS DICT", "XML", "XML ESCAPED"],
        "basicTests": "XML ESCAPED"
    },
    "DICT XML UNESCAPED" : {
        "path"      : ["ADDRESS DICT", "XML", "XML UNESCAPED"],
        "basicTests": "XML UNESCAPED"
    },

    # LIST ----------------------------------------------------------------------------------------
    "LIST STR" : {
        "path"      : ["ADDRESS LIST", 0],
        "basicTests": "STR"
    },
    "LIST INT" : {
        "path"      : ["ADDRESS LIST", 1],
        "basicTests": "INT"
    },
    "LIST FLOAT" : {
        "path"      : ["ADDRESS LIST", 2],
        "basicTests": "FLOAT"
    },
    "LIST COMPLEX" : {
        "path"      : ["ADDRESS LIST", 3],
        "basicTests": "COMPLEX"
    },
    "LIST BOOL" : {
        "path"      : ["ADDRESS LIST", 4],
        "basicTests": "BOOL"
    },
    "LIST NONE" : {
        "path"      : ["ADDRESS LIST", 5],
        "basicTests": "NONE"
    },
    "LIST LIST" : {
        "path"      : ["ADDRESS LIST", 6],
        "basicTests": "LIST"
    },
    "LIST LIST STR" : {
        "path"      : ["ADDRESS LIST", 7],
        "basicTests": "LIST STR"
    },
    "LIST TUPLE" : {
        "path"      : ["ADDRESS LIST", 8],
        "basicTests": "TUPLE"
    },
    "LIST TUPLE STR" : {
        "path"      : ["ADDRESS LIST", 9],
        "basicTests": "TUPLE STR"
    },
    "LIST SET" : {
        "path"      : ["ADDRESS LIST", 10],
        "basicTests": "SET"
    },
    "LIST SET STR" : {
        "path"      : ["ADDRESS LIST", 11],
        "basicTests": "SET STR"
    },
    "LIST FROZENSET" : {
        "path"      : ["ADDRESS LIST", 12],
        "basicTests": "FROZENSET"
    },
    "LIST FROZENSET STR" : {
        "path"      : ["ADDRESS LIST", 13],
        "basicTests": "FROZENSET STR"
    },
    "LIST DICT" : {
        "path"      : ["ADDRESS LIST", 14],
        "basicTests": "DICT"
    },
    "LIST DICT STR" : {
        "path"      : ["ADDRESS LIST", 15],
        "basicTests": "DICT STR"
    },
    "LIST BYTES" : {
        "path"      : ["ADDRESS LIST", 16],
        "basicTests": "BYTES"
    },
    "LIST BYTES STR" : {
        "path"      : ["ADDRESS LIST", 17],
        "basicTests": "BYTES STR"
    },
    "LIST BYTEARRAY" : {
        "path"      : ["ADDRESS LIST", 18],
        "basicTests": "BYTEARRAY"
    },
    "LIST BYTEARRAY STR" : {
        "path"      : ["ADDRESS LIST", 19],
        "basicTests": "BYTEARRAY STR"
    },
    "LIST EMPTY" : {
        "path"      : ["ADDRESS LIST", 20],
        "basicTests": "DICT EMPTY"
    },
    "LIST XML ESCAPED" : {
        "path"      : ["ADDRESS LIST", 21],
        "basicTests": "XML ESCAPED"
    },
    "LIST XML UNESCAPED" : {
        "path"      : ["ADDRESS LIST", 22],
        "basicTests": "XML UNESCAPED"
    },

    # TUPLE ---------------------------------------------------------------------------------------
    "TUPLE STR" : {
        "path"      : ["ADDRESS TUPLE", 0],
        "basicTests": "STR"
    },
    "TUPLE INT" : {
        "path"      : ["ADDRESS TUPLE", 1],
        "basicTests": "INT"
    },
    "TUPLE FLOAT" : {
        "path"      : ["ADDRESS TUPLE", 2],
        "basicTests": "FLOAT"
    },
    "TUPLE COMPLEX" : {
        "path"      : ["ADDRESS TUPLE", 3],
        "basicTests": "COMPLEX"
    },
    "TUPLE BOOL" : {
        "path"      : ["ADDRESS TUPLE", 4],
        "basicTests": "BOOL"
    },
    "TUPLE NONE" : {
        "path"      : ["ADDRESS TUPLE", 5],
        "basicTests": "NONE"
    },
    "TUPLE LIST" : {
        "path"      : ["ADDRESS TUPLE", 6],
        "basicTests": "LIST"
    },
    "TUPLE LIST STR" : {
        "path"      : ["ADDRESS TUPLE", 7],
        "basicTests": "LIST STR"
    },
    "TUPLE TUPLE" : {
        "path"      : ["ADDRESS TUPLE", 8],
        "basicTests": "TUPLE"
    },
    "TUPLE TUPLE STR" : {
        "path"      : ["ADDRESS TUPLE", 9],
        "basicTests": "TUPLE STR"
    },
    "TUPLE SET" : {
        "path"      : ["ADDRESS TUPLE", 10],
        "basicTests": "SET"
    },
    "TUPLE SET STR" : {
        "path"      : ["ADDRESS TUPLE", 11],
        "basicTests": "SET STR"
    },
    "TUPLE FROZENSET" : {
        "path"      : ["ADDRESS TUPLE", 12],
        "basicTests": "FROZENSET"
    },
    "TUPLE FROZENSET STR" : {
        "path"      : ["ADDRESS TUPLE", 13],
        "basicTests": "FROZENSET STR"
    },
    "TUPLE DICT" : {
        "path"      : ["ADDRESS TUPLE", 14],
        "basicTests": "DICT"
    },
    "TUPLE DICT STR" : {
        "path"      : ["ADDRESS TUPLE", 15],
        "basicTests": "DICT STR"
    },
    "TUPLE BYTES" : {
        "path"      : ["ADDRESS TUPLE", 16],
        "basicTests": "BYTES"
    },
    "TUPLE BYTES STR" : {
        "path"      : ["ADDRESS TUPLE", 17],
        "basicTests": "BYTES STR"
    },
    "TUPLE BYTEARRAY" : {
        "path"      : ["ADDRESS TUPLE", 18],
        "basicTests": "BYTEARRAY"
    },
    "TUPLE BYTEARRAY STR" : {
        "path"      : ["ADDRESS TUPLE", 19],
        "basicTests": "BYTEARRAY STR"
    },
    "TUPLE EMPTY" : {
        "path"      : ["ADDRESS TUPLE", 20],
        "basicTests": "DICT EMPTY"
    },
    "TUPLE XML ESCAPED" : {
        "path"      : ["ADDRESS TUPLE", 21],
        "basicTests": "XML ESCAPED"
    },
    "TUPLE XML UNESCAPED" : {
        "path"      : ["ADDRESS TUPLE", 22],
        "basicTests": "XML UNESCAPED"
    },
}

class TestDataRecognition(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)

    def __printInfos(self, de):
        if(len(de.infos())):
            print("==>")
            print("infos:")
        for entry in de.infos():
            print(entry)
        if(len(de.infos())):
            print("<==")

    def basicTests(self):
        for testName in basicTests.keys():
            print("\nBASIC TEST for " + testName + " ==>")

            test = basicTests[testName]
            de = DE.DE(theData[test["data"]])
            self.assertEqual(test["numChildren"],   len(de.children()),     "There should be " + str(test["numChildren"]) + " children")
            self.assertEqual(test["type"],          de.type(),              "Type '" + str(test["type"]) + "' expected")
            self.assertEqual(test["dataExpected"],  de.value(),             "EXPECTED AN OTHER VALUE")
            self.assertEqual(test["convertedStr"],  de.convertedString(),   "EXPECTED " + str(test["convertedStr"]))
            # print(de.dumps())
            # print(de.dumps("no values"))
            self.assertEqual(test["dump"],          de.dumps(),             "EXPECTED AN OTHER DUMP")
            self.assertEqual(test["dump_noValues"], de.dumps("no values"),  "EXPECTED AN OTHER DUMP WITH NO VALUES")
            self.__printInfos(de)
            print("<==")

    def addressingTests(self):
        for testName in addressingTests.keys():
            print("\nADDRESSING TEST for " + testName + " ==>")

            path = addressingTests[testName]["path"]
            test = basicTests[addressingTests[testName]["basicTests"]]
            de = DE.DE(theData, path)

            # if(testName == "DICT LIST"):
                # print(de.children())
                # print(de.type())
                # print(de.value())
                # print(de.convertedString())
                # print(de.dumps())
                # print(de.dumps("no values"))
            self.assertEqual(test["numChildren"],   len(de.children()),     "There should be " + str(test["numChildren"]) + " children")
            self.assertEqual(test["type"],          de.type(),              "Type '" + str(test["type"]) + "' expected")
            self.assertEqual(test["dataExpected"],  de.value(),             "EXPECTED AN OTHER VALUE")
            self.assertEqual(test["convertedStr"],  de.convertedString(),   "EXPECTED " + str(test["convertedStr"]))
            self.assertEqual(test["dump"],          de.dumps(),             "EXPECTED AN OTHER DUMP")
            self.assertEqual(test["dump_noValues"], de.dumps("no values"),  "EXPECTED AN OTHER DUMP WITH NO VALUES")
            self.__printInfos(de)
            print("<==")

def suiteDataRecognition():
    suite = unittest.TestSuite()
    suite.addTest(TestDataRecognition('basicTests'))
    suite.addTest(TestDataRecognition('addressingTests'))
    return suite

if __name__ == '__main__':
    # test = theData
    # de = DE.DE(test)
    # print(de.dumps())

    runner = unittest.TextTestRunner(failfast = False)
    runner.run(suiteDataRecognition())
