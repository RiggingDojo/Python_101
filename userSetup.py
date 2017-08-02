import os
import sys
import maya.cmds as cmds

print "In user setup"

sys.path.append("C:/Users/Awesome/Documents/maya/2017/scripts/Python_101")
cmds.evalDeferred("import startup")

