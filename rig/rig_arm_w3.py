import maya.cmds as cmds


ikjnt_list = [['ik_shoulder_jnt', [0.0, 0.0, 0.0]], ['ik_elbow_jnt', [-1.0, 0.0, 2.0]], ['ik_wrist_jnt', [0.0, 0.0, 4.0]], ['ik_wristEnd_jnt', [0.0, 0.0, 6.0]]]
fkjnt_list = [['fk_shoulder_jnt', [0.0, 0.0, 0.0]], ['fk_elbow_jnt', [-1.0, 0.0, 2.0]], ['ifk_wrist_jnt', [0.0, 0.0, 4.0]], ['fk_wristEnd_jnt', [0.0, 0.0, 6.0]]]
rigjnt_list = [['rig_shoulder_jnt', [0.0, 0.0, 0.0]], ['rig_elbow_jnt', [-1.0, 0.0, 2.0]], ['rig_wrist_jnt', [0.0, 0.0, 4.0]], ['rig_wristEnd_jnt', [0.0, 0.0, 6.0]]]

def createJoint(jntinfo):
	for item in jntinfo:
		cmds.joint(n=item[0], p=item[1])

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

# Create ik control
# Get ws position of wrist joint
pos = cmds.xform('ik_wrist_jnt', q=True, t=True, ws=True)
# Create an empty group
cmds.group( em=True, name='grp_ctrl_ikWrist' )
# Create circle control object
cmds.circle( n='ctrl_ikWrist', nr=(0, 0, 1), c=(0, 0, 0) )
# Parent the control to the group
cmds.parent('ctrl_ikWrist', 'grp_ctrl_ikWrist')
# Move the group to the joint
cmds.xform('grp_ctrl_ikWrist', t=pos, ws=True)
# Parent ikh to ctrl
cmds.parent('ikh_arm', 'ctrl_ikWrist')

# Create FK rig


# Connect Ik and Fk to Rig joints