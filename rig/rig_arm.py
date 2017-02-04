'''
Rhonda Ray

Description:
   Creating IK/FK arm rig

'''

import pymel.core as pm

print 'Starting IK-FK Arm Rig...'


def createJoint():
	# create joint position based on manual creation values
	jntList = [['shoulder_jnt', [-7, 0, 2]], ['elbow_jnt', [-1, 0, 0]], ['wrist_jnt', [4, 0, 2]], ['wristEND_jnt', [7, 0, 3]]]
	armList = ['ik_', 'fk_', 'rig_']

	for item in armList:
		for jnt in jntList:
			jntName = item+jnt[0]
			pm.joint(name=jntName, position=jnt[1], radius=.5)

		pm.select(deselect=True)


def createIK():
	# create IK handle
	pm.ikHandle(name='ikh_arm', startJoint='ik_shoulder_jnt', endEffector='ik_wrist_jnt', solver='ikRPsolver', priority=2, weight=1)

	# get world space position of wrist joint
	posWrist = pm.xform('ik_wrist_jnt', query=True, translation=True, worldSpace=True)

	# create an empty group and orient to wrist
	pm.group(empty=True, name='grp_ctrl_ikWrist')

	# create circle control
	pm.curve(name='ctrl_ikWrist', degree=1, point=[(1.25, 0, 0), (0, 0, 0), (0, 0, 1.25), (1.25, 0, 1.25), (1.25, 0, 0)], knot=[0, 1, 2, 3, 4])
	pm.xform('ctrl_ikWrist', scale=(1.5, 1.5, 1.5), rotation=(0, 0, 90), preserve=True, centerPivots=True)
	pm.makeIdentity('ctrl_ikWrist', apply=True, translate=1, rotate=1, scale=1, normal=0, preserveNormals=1) 

	'''
	this should work and it does to a certain degree
	the ik arm ends up off center from the rig arm
	and I do not know where to place this code to 
	keep that from happening

	# use parent constraint to center curve control
	#temp=pm.parentConstraint('ctrl_ikWrist', 'ik_wrist_jnt')
	#pm.delete(temp)
	'''

	# parent control to group
	pm.parent('ctrl_ikWrist', 'grp_ctrl_ikWrist')

	# move the group to the joint
	pm.xform('grp_ctrl_ikWrist', translation=posWrist, worldSpace=True)

	# parent ik handle to wrist control
	pm.parent('ikh_arm', 'ctrl_ikWrist')


def createFK():
	# get list of selected objects minus the end joint
	pm.select('fk_shoulder_jnt')
	selJoints = pm.ls(selection=True, dag=True)
	selJoints.pop(-1)

	# loop thru the selected joints
	for jnt in selJoints:
		# get world space position of the joint
		posWrist = pm.xform(jnt, query=True, translation=True, worldSpace=True)

		# pull out the joint name, upper case the first letter and concatenate to fk
		jntName = 'fk' + jnt.split('_')[1].title()

		# create group from joint name
		grp = pm.group(name='grp_ctrl_' + jntName, empty=True)

		# create square control from joint name
		ctrl = pm.circle(name='ctrl_' + jntName, normal=(1,0,0), center=(0,0,0), radius=1.5, constructionHistory=False)
		
		# parent control to grp
		pm.parent(ctrl, grp)

		# move group to joint
		pm.xform(grp, translation=posWrist, worldSpace=True)

		# constrain joint to control
		pm.parentConstraint(ctrl, jnt, maintainOffset=True)


def connectJoints():
	# connect IK and FK to rig joints
	# select all three joint chains and group together
	pm.select('rig_shoulder_jnt', replace=True)
	pm.select('fk_shoulder_jnt', add=True)
	pm.select('ik_shoulder_jnt', add=True)
	pm.group(name='grp_arm')

	# select same joint from each arm and add orient constraint
	pm.orientConstraint('fk_shoulder_jnt', 'ik_shoulder_jnt', 'rig_shoulder_jnt')
	#pm.orientConstraint('ik_shoulder_jnt', 'rig_shoulder_jnt')

	pm.orientConstraint('fk_elbow_jnt', 'ik_elbow_jnt', 'rig_elbow_jnt')
	#pm.orientConstraint('ik_elbow_jnt', 'rig_elbow_jnt')

	pm.orientConstraint('fk_wrist_jnt', 'ik_wrist_jnt', 'rig_wrist_jnt')
	#pm.orientConstraint('ik_wrist_jnt', 'rig_wrist_jnt')

	# create control hierarchy
	pm.parent('grp_ctrl_fkWrist', 'ctrl_fkElbow')
	pm.parent('grp_ctrl_fkElbow', 'ctrl_fkShoulder')

	pm.select(deselect=True)


def createPoleVector():
	# used Lionel Gallat's idea for the pole vector - just converted to python
	# create pole vector for elbow
	pm.spaceLocator(name='lctr_PV_arm')
	posElbow = pm.xform('ik_elbow_jnt', query=True, translation=True, worldSpace=True)
	pm.xform('lctr_PV_arm', worldSpace=True, translation=posElbow)
	pm.setAttr('lctr_PV_arm.tz', posElbow[2] - 5)

	# parent pole vector to shoulder
	#pm.parent('lctr_PV_arm', 'rig_shoulder_jnt')
	pm.setAttr('lctr_PV_arm.visibility', False)

	# create pole vector control
	pm.circle(name='ctrl_PV_arm', normal=(0,1,0), radius=1)[0]
	pm.select('ctrl_PV_arm.ep[2:3]', 'ctrl_PV_arm.ep[5:6]', replace=True)
	pm.xform(scale=[.318733, 1, 1])
	pm.select('ctrl_PV_arm.ep[3]', 'ctrl_PV_arm.ep[5]', replace=True)
	pm.xform(scale=[.400636, 1, 1])

	# move control to locator position
	temp = pm.pointConstraint('lctr_PV_arm', 'ctrl_PV_arm')
	pm.delete(temp)
	pm.makeIdentity('ctrl_PV_arm', apply=True, translate=1, rotate=1, scale=1, normal=0, preserveNormals=1) 
	pm.delete('lctr_PV_arm')
	pm.select(deselect=True)

	# constrain the IK handle to the pole vector control
	pm.poleVectorConstraint('ctrl_PV_arm', 'ikh_arm')


createJoint()
createIK()
createFK()
connectJoints()
createPoleVector

'''
Issue with the parenting of the shape nodes.  See below

# add IK/FK switch
# creates text for IK/FK 
pm.textCurves(name='ctrl_ikHand', font='Courier', text='switch')

# get curves and their shapes
nurbsShapes = pm.listRelatives(allDescendents=True, noIntermediate=True, type="nurbsCurve", fullPath=True, path=True)
nurbsTransforms = pm.listRelatives(nurbsShapes, type="transform", parent=True)

# unparent curves and freeze transforms
pm.select(nurbsTransforms)
pm.parent(world=True)
pm.makeIdentity() 

I can't get this portion to work correctly.  Remove and pop give me an attribute error.
'builtin_function_or_method' object has no attribute '__getitem__' 

What I have now, parents all the curves and all the shapes under the first curve.  I tried
deleting the curve after I added the shape to the new list, but I could not get that to
work either.

# remove first shape then parent to first curve
newShapes = []
for s in nurbsShapes:
	if s != 'curve1':
		newShapes.append(s)

pm.select(newShapes, nurbsTransforms[0], add=True)
pm.parent(relative=True, shape=True)
'''



print 'end of script'
