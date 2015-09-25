import maya.cmds as cmds


ikjnt_list = [['ik_shoulder_jnt', [0.0, 0.0, 0.0]], ['ik_elbow_jnt', [-1.0, 0.0, 2.0]], ['ik_wrist_jnt', [0.0, 0.0, 4.0]], ['ik_wristEnd_jnt', [0.0, 0.0, 6.0]]]
fkjnt_list = [['fk_shoulder_jnt', [0.0, 0.0, 0.0]], ['fk_elbow_jnt', [-1.0, 0.0, 2.0]], ['ifk_wrist_jnt', [0.0, 0.0, 4.0]], ['fk_wristEnd_jnt', [0.0, 0.0, 6.0]]]
rigjnt_list = [['rig_shoulder_jnt', [0.0, 0.0, 0.0]], ['rig_elbow_jnt', [-1.0, 0.0, 2.0]], ['rig_wrist_jnt', [0.0, 0.0, 4.0]], ['rig_wristEnd_jnt', [0.0, 0.0, 6.0]]]

def createJoint(jntinfo):
	for item in jntinfo:
		cmds.joint(n=item[0], p=item[1])

def createControl(ctrlinfo):
	# Create ik control
	# Get ws position of wrist joint
	pos = ctrlinfo[0]
	# Create an empty group
	ctrlgrp = cmds.group( em=True, name=ctrlinfo[1] )
	# Create circle control object
	ctrl = cmds.circle( n=ctrlinfo[2], nr=(0, 0, 1), c=(0, 0, 0) )
	# Parent the control to the group
	cmds.parent(ctrl, ctrlgrp)
	# Move the group to the joint
	cmds.xform(ctrlgrp, t=pos, ws=True)

# Create Ik joints
createJoint(ikjnt_list)
cmds.select(d=True)
# Create Fk joints
createJoint(fkjnt_list)
cmds.select(d=True)
# Create Rig joints
createJoint(rigjnt_list)
cmds.select(d=True)


# Create Ik Rig
# Ik handle
cmds.ikHandle( n='ikh_arm', sj='ik_shoulder_jnt', ee='ik_wrist_jnt', sol='ikRPsolver', p=2, w=1 )

ikctrlinfo = [[ikjnt_list[2][1], 'ctrl_ik_arm', 'grp_ctrl_ik_arm']]
createControl()

# Parent ikh to ctrl
cmds.parent('ikh_arm', 'ctrl_ik_arm')

# Create FK rig
fkctrlinfo = [[fkjnt_list[0][1], 'ctrl_fk_shoulder', 'grp_ctrl_fk_shoulder'],
[fkjnt_list[1][1], 'ctrl_fk_elbow', 'grp_ctrl_fk_elbow'],
[fkjnt_list[2][1], 'ctrl_fk_wrist', 'grp_ctrl_fk_wrist']]


# Connect Ik and Fk to Rig joints