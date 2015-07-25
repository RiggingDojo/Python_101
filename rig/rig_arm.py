
# Create Ik joints
cmds.joint( n='ik_shoulder_jnt', p=[2.1, 0, 5.0])
cmds.joint( n='ik_elbow_jnt', p=[-0.1, 0, 0.0])
cmds.joint( n='ik_wrist_jnt', p=[1.0, 0, -5.0])
cmds.joint( n='ik_wristEnd_jnt', p=[1.0, 0, -8.0])
cmds.select(d=True)

# Create Fk joints
cmds.joint( n='fk_shoulder_jnt', p=[2.1, 0, 5.0])
cmds.joint( n='fk_elbow_jnt', p=[-0.1, 0, 0.0])
cmds.joint( n='fk_wrist_jnt', p=[1.0, 0, -5.0])
cmds.joint( n='fk_wristEnd_jnt', p=[1.0, 0, -8.0])
cmds.select(d=True)

# Create rig joints
cmds.joint( n='rig_shoulder_jnt', p=[2.1, 0, 5.0])
cmds.joint( n='rig_elbow_jnt', p=[-0.1, 0, 0.0])
cmds.joint( n='rig_wrist_jnt', p=[1.0, 0, -5.0])
cmds.joint( n='rig_wristEnd_jnt', p=[1.0, 0, -8.0])
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