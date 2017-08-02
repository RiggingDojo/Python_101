import maya.cmds as cmds

print "ui"

def ArmRig():
	print "RigArm"

mymenu = cmds.menu("Test_Menu", label = 'TestMenu', to= True, p= "MayaWindow")
cmds.menuItem(label = "RigArm", p = mymenu, command = ArmRig)



