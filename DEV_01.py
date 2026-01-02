import MyFramework.DE as DE
import json
import os
import pickle
import xmltodict

contentForFile = {
# Text Type:	str
    "key01" : "value1",
# Numeric Types:	int, float, complex
    "key02" : 123,
    "key03" : 1.23,
    "key04" : str((3 + 7j)),
# Sequence Types:	list, tuple, range --> Not supported
    "key05" : "[1, 2]",
    "key06" : str(("TUPLE A", '{"eins":"zwei"}')),

# Mapping Type:	dict
    "key07" : {
        "keyA" : "DICT valueA",
        "keyB" : "DICT valueB"
        },
    "key07STR" : '{"keyA" : "DICT valueA","keyB" : "DICT valueB"}',
# Set Types:	set, frozenset
    "key08" : str({"SET A", "SET B", "SET C"}),
    "key09" : str(frozenset([1,3,(3,5)])),
# Boolean Type:	bool
    "key10" : True,
    "key11" : False,
# Binary Types:	bytes, bytearray, memoryview --> Not supported
    "key12" : str(bytes('Python', 'utf-8')),
    "key13" : str(bytearray([2, 3, 5, 7])),
# None Type:	NoneType
    "key14" : None,
# XML
    # "xml": "&lt;mxGraphModel&gt;&lt;root&gt;&lt;mxCell id=\"0\"/&gt;&lt;mxCell id=\"1\" parent=\"0\"/&gt;&lt;object label=\"Table*\" name=\"DB Table\" id=\"2\"&gt;&lt;mxCell style=\"shape=table;startSize=20;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;\" vertex=\"1\" parent=\"1\"&gt;&lt;mxGeometry y=\"1.1368683772161603e-13\" width=\"280\" height=\"40\" as=\"geometry\"/&gt;&lt;/mxCell&gt;&lt;/object&gt;&lt;object label=\"\" name=\"DB Column\" id=\"3\"&gt;&lt;mxCell style=\"shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;\" vertex=\"1\" parent=\"2\"&gt;&lt;mxGeometry y=\"20\" width=\"280\" height=\"20\" as=\"geometry\"/&gt;&lt;/mxCell&gt;&lt;/object&gt;&lt;mxCell id=\"4\" value=\"000 FK, PK N\" style=\"shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=0;overflow=hidden;whiteSpace=wrap;html=1;\" vertex=\"1\" parent=\"3\"&gt;&lt;mxGeometry width=\"80\" height=\"20\" as=\"geometry\"&gt;&lt;mxRectangle width=\"80\" height=\"20\" as=\"alternateBounds\"/&gt;&lt;/mxGeometry&gt;&lt;/mxCell&gt;&lt;mxCell id=\"5\" value=\"UniqueID*\" style=\"shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=0;overflow=hidden;whiteSpace=wrap;html=1;\" vertex=\"1\" parent=\"3\"&gt;&lt;mxGeometry x=\"80\" width=\"200\" height=\"20\" as=\"geometry\"&gt;&lt;mxRectangle width=\"200\" height=\"20\" as=\"alternateBounds\"/&gt;&lt;/mxGeometry&gt;&lt;/mxCell&gt;&lt;/root&gt;&lt;/mxGraphModel&gt;",
}

contentDirect = {
# Text Type:	str
    "key01" : "value1",
# Numeric Types:	int, float, complex
    "key02" : 123,
    "key03" : 1.23,
    "key04" : (3 + 7j),
# Sequence Types:	list, tuple, range --> Not supported
    "key05" : [1, 2],
    "key05STR" : '[1, 2]',
    "key06" : ("TUPLE A", {"eins":"zwei"}),

# Mapping Type:	dict
    "key07" : {
        "keyA" : "DICT valueA",
        "keyB" : "DICT valueB"
        },
    "key07STR" : '{"keyA" : "DICT valueA","keyB" : "DICT valueB"}',
# Set Types:	set, frozenset
    "key08" : {"SET A", "SET B", "SET C"},
    "key09" : frozenset([1,3,(3,5)]),
# Boolean Type:	bool
    "key10" : True,
    "key11" : False,
# Binary Types:	bytes, bytearray, memoryview --> Not supported
    "key12" : bytes('Python', 'utf-8'),
    "key13" : bytearray([2, 3, 5, 7]),
# None Type:	NoneType
    "key14" : None,
# XML
    # "xmlEntry": "&lt;mxGraphModel&gt;&lt;root&gt;&lt;mxCell id=\"0\"/&gt;&lt;mxCell id=\"1\" parent=\"0\"/&gt;&lt;object label=\"Table*\" name=\"DB Table\" id=\"2\"&gt;&lt;mxCell style=\"shape=table;startSize=20;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;\" vertex=\"1\" parent=\"1\"&gt;&lt;mxGeometry y=\"1.1368683772161603e-13\" width=\"280\" height=\"40\" as=\"geometry\"/&gt;&lt;/mxCell&gt;&lt;/object&gt;&lt;object label=\"\" name=\"DB Column\" id=\"3\"&gt;&lt;mxCell style=\"shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;\" vertex=\"1\" parent=\"2\"&gt;&lt;mxGeometry y=\"20\" width=\"280\" height=\"20\" as=\"geometry\"/&gt;&lt;/mxCell&gt;&lt;/object&gt;&lt;mxCell id=\"4\" value=\"000 FK, PK N\" style=\"shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=0;overflow=hidden;whiteSpace=wrap;html=1;\" vertex=\"1\" parent=\"3\"&gt;&lt;mxGeometry width=\"80\" height=\"20\" as=\"geometry\"&gt;&lt;mxRectangle width=\"80\" height=\"20\" as=\"alternateBounds\"/&gt;&lt;/mxGeometry&gt;&lt;/mxCell&gt;&lt;mxCell id=\"5\" value=\"UniqueID*\" style=\"shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=0;overflow=hidden;whiteSpace=wrap;html=1;\" vertex=\"1\" parent=\"3\"&gt;&lt;mxGeometry x=\"80\" width=\"200\" height=\"20\" as=\"geometry\"&gt;&lt;mxRectangle width=\"200\" height=\"20\" as=\"alternateBounds\"/&gt;&lt;/mxGeometry&gt;&lt;/mxCell&gt;&lt;/root&gt;&lt;/mxGraphModel&gt;",
}
xml = "&lt;mxGraphModel&gt;&lt;root&gt;&lt;mxCell id=\"0\"/&gt;&lt;mxCell id=\"1\" parent=\"0\"/&gt;&lt;object label=\"Table*\" name=\"DB Table\" id=\"2\"&gt;&lt;mxCell style=\"shape=table;startSize=20;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;whiteSpace=wrap;\" vertex=\"1\" parent=\"1\"&gt;&lt;mxGeometry y=\"1.1368683772161603e-13\" width=\"280\" height=\"40\" as=\"geometry\"/&gt;&lt;/mxCell&gt;&lt;/object&gt;&lt;object label=\"\" name=\"DB Column\" id=\"3\"&gt;&lt;mxCell style=\"shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;\" vertex=\"1\" parent=\"2\"&gt;&lt;mxGeometry y=\"20\" width=\"280\" height=\"20\" as=\"geometry\"/&gt;&lt;/mxCell&gt;&lt;/object&gt;&lt;mxCell id=\"4\" value=\"000 FK, PK N\" style=\"shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=0;overflow=hidden;whiteSpace=wrap;html=1;\" vertex=\"1\" parent=\"3\"&gt;&lt;mxGeometry width=\"80\" height=\"20\" as=\"geometry\"&gt;&lt;mxRectangle width=\"80\" height=\"20\" as=\"alternateBounds\"/&gt;&lt;/mxGeometry&gt;&lt;/mxCell&gt;&lt;mxCell id=\"5\" value=\"UniqueID*\" style=\"shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=0;overflow=hidden;whiteSpace=wrap;html=1;\" vertex=\"1\" parent=\"3\"&gt;&lt;mxGeometry x=\"80\" width=\"200\" height=\"20\" as=\"geometry\"&gt;&lt;mxRectangle width=\"200\" height=\"20\" as=\"alternateBounds\"/&gt;&lt;/mxGeometry&gt;&lt;/mxCell&gt;&lt;/root&gt;&lt;/mxGraphModel&gt;"

with open("DEV.json", "w") as f:
    f.write(json.dumps(contentForFile, indent=3))
    

f = open("DEV.json")
data = f.read()

data = contentDirect

# de = DE.DE(data)
de = DE.DE(data, ["key07"])
# de = DE.DE(data, ["key05STR"])

print(de.dumps())#"no values"))