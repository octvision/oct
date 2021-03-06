############################################################################################
'''
Snap To Ground Tool
--------------------------------------------------------------------------------------------
Author: Ryan Nolan
Contact: RyanNolan3D@gmail.com
--------------------------------------------------------------------------------------------
Usage:
Select your ground object and "set surface to snap to"
NOTE: Ground must have some sort of UVs for script to work
Then "Snap objects"
Note: It's recommended to move your objects above the ground. Objects below the ground will
    be ignored
'''
############################################################################################
import maya .cmds as mc #line:1
import maya .mel as mel #line:2
import maya .OpenMayaUI as omui #line:5
import maya .OpenMaya as om #line:6
import os as os #line:8
__all__ =[]#line:10
class SnapToPlane ():#line:12
    terrain =""#line:13
    def __init__ (self ):#line:15
        self .createWindow ()#line:16
    def SetSurfaceObj (OO0O000O0O00O00OO ,*OO00O0OOO000O0O00 ):#line:18
        OO0O000O0O00O00OO .terrain =mc .ls (sl =True ,o =True )#line:19
        print (OO0O000O0O00O00OO .terrain )#line:20
        print ("Surface terrain set")#line:21
    def Snap (OOOOOO000O0OOO0O0 ,*OOO00000O0OOOOO00 ):#line:24
        O00OOO000O00O0OOO =mc .ls (sl =True )#line:25
        for O00OO000O0OOOOOO0 in O00OOO000O00O0OOO :#line:28
            O00000OO00O00OOOO =mc .getAttr (O00OO000O0OOOOOO0 +".translate")[0]#line:30
            objWorldPivot = mc.xform(O00OO000O0OOOOOO0,q=True, ws=True, rp=True)
            OOOOO00O00OOO00O0 =O00OO0OO00000OO00 (OOOOOO000O0OOO0O0 .terrain [0 ],objWorldPivot,[0 ,-1 ,0 ])#line:31
            if OOOOO00O00OOO00O0 !=None :#line:33
                print OOOOO00O00OOO00O0 ['hit'][1 ]
                mc .setAttr ((O00OO000O0OOOOOO0 +".translateY"),(OOOOO00O00OOO00O0 ['hit'][1 ]+O00000OO00O00OOOO[1]-objWorldPivot[1]))#line:34
            else:
                print 'None'
    def createWindow (O00OO0O0O00O0O000 ):#line:38
        if mc .window ("SnapToGroundTool",exists =True ):#line:40
            mc .deleteUI ("SnapToGroundTool")#line:41
        if mc .windowPref ("SnapToGroundTool",exists =True ):#line:43
            mc .windowPref ("SnapToGroundTool",remove =True )#line:44
        mc .window ("SnapToGroundTool",title ="Snap To Ground Tool")#line:46
        mc .columnLayout (rs =5 )#line:48
        mc .button (w =200 ,h =30 ,label ="Set surface to snap to",c =O00OO0O0O00O0O000 .SetSurfaceObj )#line:49
        mc .button (w =200 ,h =30 ,label ="Snap objects",c =O00OO0O0O00O0O000 .Snap )#line:50
        mc .showWindow ("SnapToGroundTool")#line:52
def O00OO0OO00000OO00 (OOOOO0OO000OOOO00 ,O00OO00OO00O00OO0 ,OO00000OOOO0O000O ,OO00O0000O00O0000 =1000 ):#line:54
    O00000O0OOO0O0OO0 =om .MSelectionList ()#line:56
    O00000O0OOO0O0OO0 .add (OOOOO0OO000OOOO00 )#line:59
    OO0O00OOOOOOOO0O0 =om .MDagPath ()#line:62
    O00000O0OOO0O0OO0 .getDagPath (0 ,OO0O00OOOOOOOO0O0 )#line:66
    OOO0OO0OOO00000O0 =om .MFnMesh (OO0O00OOOOOOOO0O0 )#line:70
    O00OO00OO00O00OO0 =om .MFloatPoint (O00OO00OO00O00OO0 [0 ],O00OO00OO00O00OO0 [1 ],O00OO00OO00O00OO0 [2 ])#line:73
    O000O0000O0O0OOOO =om .MFloatVector (OO00000OOOO0O000O [0 ],OO00000OOOO0O000O [1 ],OO00000OOOO0O000O [2 ])#line:76
    O0O000000OO0OOOOO =om .MFloatPoint ()#line:79
    OOO00OO00OO0O0000 =False #line:81
    OOO0OO0O00O0O00OO =om .MDistance .internalToUI (1000000 )#line:82
    O00OOO0O0000OO000 =False #line:83
    OOOOOO000O0OOOOO0 =None #line:84
    OO000O0O0OOO00000 =None #line:85
    O0O0OOO00O0O0000O =None #line:86
    O0O00OOO000O0000O =None #line:87
    O00000O00O0000000 =None #line:88
    O00O000OOO0000O0O =None #line:89
    O0OOO0O00O00OOOOO =None #line:90
    O00O00O0O0000O00O =None #line:91
    O0O0O000OOO00OOOO =OOO0OO0OOO00000O0 .closestIntersection (O00OO00OO00O00OO0 ,O000O0000O0O0OOOO ,OOOOOO000O0OOOOO0 ,OO000O0O0OOO00000 ,OOO00OO00OO0O0000 ,om .MSpace .kWorld ,OOO0OO0O00O0O00OO ,O00OOO0O0000OO000 ,O0O0OOO00O0O0000O ,O0O000000OO0OOOOO ,O0O00OOO000O0000O ,O00000O00O0000000 ,O00O000OOO0000O0O ,O0OOO0O00O00OOOOO ,O00O00O0O0000O00O )#line:100
    if O0O0O000OOO00OOOO :#line:103
        O00000000O0O0OOO0 =om .MPoint (O0O000000OO0OOOOO )#line:104
        OO000OOO0O0OO000O =[0.0 ,0.0 ]#line:105
        O0O0000OOOOOOOO00 =om .MScriptUtil ()#line:106
        O0O0000OOOOOOOO00 .createFromList (OO000OOO0O0OO000O ,2 )#line:107
        O0OOOOOO0OOOOO0O0 =O0O0000OOOOOOOO00 .asFloat2Ptr ()#line:108
        O0OO000000O00O0O0 =None #line:109
        O0OO0OOO0OO0O0O00 =None #line:110
        OO00OOOOOO0OO00OO =OOO0OO0OOO00000O0 .getUVAtPoint (O00000000O0O0OOO0 ,O0OOOOOO0OOOOO0O0 ,om .MSpace .kWorld )#line:111
        OO0OOOOO0OOOO00O0 =om .MScriptUtil .getFloat2ArrayItem (O0OOOOOO0OOOOO0O0 ,0 ,0 )or False #line:113
        O0OOOO0O0000O0000 =om .MScriptUtil .getFloat2ArrayItem (O0OOOOOO0OOOOO0O0 ,0 ,1 )or False #line:114
        if OO0OOOOO0OOOO00O0 and O0OOOO0O0000O0000 :#line:115
            return {'hit':[O0O000000OO0OOOOO .x ,O0O000000OO0OOOOO .y ,O0O000000OO0OOOOO .z ],'source':[O00OO00OO00O00OO0 .x ,O00OO00OO00O00OO0 .y ,O00OO00OO00O00OO0 .z ],'uv':[OO0OOOOO0OOOO00O0 ,O0OOOO0O0000O0000 ]}#line:116
        else :#line:117
            return {'hit':[O0O000000OO0OOOOO .x ,O0O000000OO0OOOOO .y ,O0O000000OO0OOOOO .z ],'source':[O00OO00OO00O00OO0 .x ,O00OO00OO00O00OO0 .y ,O00OO00OO00O00OO0 .z ],'uv':False }#line:118
    else :#line:119
        return None #line:120
# SnapToPlane ()

#===============================================================#
# Obfuscated by Oxyry Python Obfuscator (http://pyob.oxyry.com) #
#===============================================================#
