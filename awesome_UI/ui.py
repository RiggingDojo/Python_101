import maya.cmds as cmds

print "ui"

def rigarm(*args):
	print "rig_arm"
	import rig.rig_arm as rig_arm
	print rig_arm
	reload(rig_arm)
	rig_arm = rig_arm.Rig_Arm()
	print rig_arm
	rig_arm.rig_arm()

def rigleg(*args):
	print "rig_leg"
	import rig.rig_leg as rig_leg
	print rig_leg
	reload(rig_leg)
	rig_leg = rig_leg.Rig_Leg()
	print rig_leg
	rig_leg.rig_leg()

menuarray = cmds.window("MayaWindow", q= True, ma= True)
if "Test_Menu" not in menuarray:
	mymenu = cmds.menu("Test_Menu", label = 'TestMenu', to= True, p= "MayaWindow")
	cmds.menuItem(label = "Arm", p = mymenu, command = rigarm)
	cmds.menuItem(label = "Leg", p = mymenu, command = rigleg)



