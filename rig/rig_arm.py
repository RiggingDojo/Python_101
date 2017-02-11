'''
Rhonda Ray

Description:
   Creating IK/FK arm rig

'''

import pymel.core as pm
import system.ctrl_shapes as cShape
import json

print 'Starting IK-FK Arm Rig...'

class GlobalVars:

	rigInfo = json.loads(inputData)

'''
I was thinking I could break out the keys into their separate lists.  Don't know if this would be the way to go or not.

	for key, value in rigInfo.iteritems():
		key = {}
		key = value

rig_data['bodyPlacement'] = ['lt_', 'rt_']
rig_data['jntType'] = ['ik_', 'fk_', 'rig_', 'bind_']
rig_data['armJnts']	= ['shoulder_jnt', 'elbow_jnt', 'wrist_jnt', 'wristEND_jnt']
rig_data['armIKCtrls']	= ['ctrl_ikWrist', 'ikh_arm', 'ctrl_PV_arm', 'ctrl_ikHand']
rig_data['armFKCtrls']	= ['ctrl_fkShoulder', 'ctrl_fkElbow', 'ctrl_fkWrist']
rig_data['armGrps'] = ['grp_ctrl_ikWrist', 'grp_ctrl_fkShoulder', 'grp_ctrl_fkElbow', 'grp_ctrl_fkWrist', 'grp_arm']
rig_data['armPos'] = [[-7, 0, 2], [-1, 0, 0], [4, 0, 2], [7, 0, 3]]
'''

	
class RigArm():

	def createRig(self):
		self.createJoint()
		self.createIK()
		self.createFK()
		self.connectJoints()
		self.createPoleVector()
		self.createIKSwitch()


	def createJoint(self):
		armList = {} 
		armList = GlobalVars.rigInfo['jntType']
		for key in armList.iteritems():
			print value

		for item in armList:
			for jnt in jntList:
				jntName = item+jnt[0]
				pm.joint(name=jntName, position=jnt[1], radius=.5)

			pm.select(deselect=True)


	def createIK(self):
		# create IK handle
		pm.ikHandle(name='ikh_arm', startJoint='ik_shoulder_jnt', endEffector='ik_wrist_jnt', solver='ikRPsolver', priority=2, weight=1)

		# get world space position of wrist joint
		posWrist = pm.xform('ik_wrist_jnt', query=True, translation=True, worldSpace=True)

		# create an empty group and orient to wrist
		pm.group(empty=True, name='grp_ctrl_ikWrist')

		# create square control
		#TODO: need to get control name - ctrl_ikWrist
		ctrl_ikWrist = cShape.square(self, ctrlName)

		# parent control to group
		pm.parent('ctrl_ikWrist', 'grp_ctrl_ikWrist')

		# move the group to the joint
		pm.xform('grp_ctrl_ikWrist', translation=posWrist, worldSpace=True)

		# parent ik handle to wrist control
		pm.parent('ikh_arm', 'ctrl_ikWrist')


	def createFK(self):
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

			#TODO: add control name - control_jointname
			ctrl_jnt = cShape.circle(self, ctrlName)
			
			# parent control to grp
			pm.parent(ctrl, grp)

			# move group to joint
			pm.xform(grp, translation=posWrist, worldSpace=True)

			# constrain joint to control
			pm.parentConstraint(ctrl, jnt, maintainOffset=True)


	def connectJoints(self):
		# connect IK and FK to rig joints
		# select all three joint chains and group together
		pm.select('rig_shoulder_jnt', replace=True)
		pm.select('fk_shoulder_jnt', add=True)
		pm.select('ik_shoulder_jnt', add=True)
		pm.group(name='grp_arm')

		# select same joint from each arm and add orient constraint
		pm.orientConstraint('fk_shoulder_jnt', 'ik_shoulder_jnt', 'rig_shoulder_jnt')
		pm.orientConstraint('fk_elbow_jnt', 'ik_elbow_jnt', 'rig_elbow_jnt')
		pm.orientConstraint('fk_wrist_jnt', 'ik_wrist_jnt', 'rig_wrist_jnt')

		# create control hierarchy
		pm.parent('grp_ctrl_fkWrist', 'ctrl_fkElbow')
		pm.parent('grp_ctrl_fkElbow', 'ctrl_fkShoulder')

		pm.select(deselect=True)


	def createPoleVector(self):
		# used Lionel Gallat's idea for the pole vector - just converted to python
		# create locator for placement of the pole vector
		pm.spaceLocator(name='lctr_PV_arm')
		posElbow = pm.xform('ik_elbow_jnt', query=True, translation=True, worldSpace=True)
		pm.xform('lctr_PV_arm', worldSpace=True, translation=posElbow)
		pm.setAttr('lctr_PV_arm.tz', posElbow[2] - 5)

		# set visibility attribute
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


	def createIKSwitch(self):

		#TODO: get control name - ctrl_ikHand
		# creates text for IK/FK 
		ctrl_ikHand = cShape.text(self, 'switch', ctrlName)

		# rename control
		newName = ctrl_ikHand[0].strip('Shape')
		txtCurve = pm.rename(ctrl_ikHand[0], newName, ignoreShape = True)
		pm.xform(ctrl_ikHand, centerPivots = True)

		# create locator for the IK switch
		pm.spaceLocator(name='lctr_switch')
		posEnd = pm.xform('rig_wristEND_jnt', query=True, translation=True, worldSpace=True)
		pm.xform('lctr_switch', worldSpace=True, translation=posEnd)
		pm.setAttr('lctr_switch.tx', posEnd[0] + 1.25)

		# move control to locator position
		temp = pm.pointConstraint('lctr_switch', ctrl_ikHand)
		pm.delete(temp)
		pm.xform(ctrl_ikHand, worldSpace=True, rotation=(0,-90,0), scale=(.5,.5,.5))
		pm.makeIdentity(ctrl_ikHand, apply=True, translate=1, rotate=1, scale=1, normal=0, preserveNormals=1) 
		pm.delete('lctr_switch')

		pm.select(deselect=True)




print 'end of script'
