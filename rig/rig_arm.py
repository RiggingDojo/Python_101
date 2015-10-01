import maya.cmds as cmds


ikjnt_list = [['ik_shoulder_jnt', [0.0, 0.0, 0.0]], ['ik_elbow_jnt', [-1.0, 0.0, 2.0]], ['ik_wrist_jnt', [0.0, 0.0, 4.0]], ['ik_wristEnd_jnt', [0.0, 0.0, 6.0]]]
fkjnt_list = [['fk_shoulder_jnt', [0.0, 0.0, 0.0]], ['fk_elbow_jnt', [-1.0, 0.0, 2.0]], ['ifk_wrist_jnt', [0.0, 0.0, 4.0]], ['fk_wristEnd_jnt', [0.0, 0.0, 6.0]]]
rigjnt_list = [['rig_shoulder_jnt', [0.0, 0.0, 0.0]], ['rig_elbow_jnt', [-1.0, 0.0, 2.0]], ['rig_wrist_jnt', [0.0, 0.0, 4.0]], ['rig_wristEnd_jnt', [0.0, 0.0, 6.0]]]

class Rig_Arm:

    def rig_arm(self):
        # Create Ik joints
        self.createJoint(ikjnt_list)
        cmds.select(d=True)
        # Create Fk joints
        self.createJoint(fkjnt_list)
        cmds.select(d=True)
        # Create Rig joints
        self.createJoint(rigjnt_list)
        cmds.select(d=True)


        # Create Ik Rig
        # Ik handle
        ikh = cmds.ikHandle( n='ikh_arm', sj='ik_shoulder_jnt', ee='ik_wrist_jnt', sol='ikRPsolver', p=2, w=1 )

        ikctrlinfo = [[ikjnt_list[2][1], 'ctrl_ik_arm', 'grp_ctrl_ik_arm']]
        self.createControl(ikctrlinfo)

        pvpos = self.calculatePVPosition([ikjnt_list[0][0], ikjnt_list[1][0], ikjnt_list[2][0]])
        pvctrlinfo = [[pvpos, 'ctrl_pv_arm', 'grp_ctrl_pv_arm']]
        self.createControl(pvctrlinfo)

        # Parent ikh to ctrl
        cmds.parent('ikh_arm', 'ctrl_ik_arm')

        # PV constraint
        cmds.poleVectorConstraint(pvctrlinfo[0][1], ikh[0])

        # orient constrain arm ik_wrist to ctrl_arm
        cmds.orientConstraint(ikctrlinfo[0][1], ikjnt_list[2][0], mo=True)

        # Create FK rig
        fkctrlinfo = [[fkjnt_list[0][1], 'ctrl_fk_shoulder', 'grp_ctrl_fk_shoulder'],
        [fkjnt_list[1][1], 'ctrl_fk_elbow', 'grp_ctrl_fk_elbow'],
        [fkjnt_list[2][1], 'ctrl_fk_wrist', 'grp_ctrl_fk_wrist']]
        self.createControl(fkctrlinfo)

        # Parent fk controls
        cmds.parent(fkctrlinfo[1][2], fkctrlinfo[0][1])
        cmds.parent(fkctrlinfo[2][2], fkctrlinfo[1][1])
        # Connect Ik and Fk to Rig joints


    def createJoint(self, jntinfo):
    	for item in jntinfo:
    		cmds.joint(n=item[0], p=item[1])

    def createControl(self, ctrlinfo):
    	for info in ctrlinfo:
    		# Create ik control
    		# Get ws position of wrist joint
    		pos = info[0]
    		# Create an empty group
    		ctrlgrp = cmds.group( em=True, name=info[2] )
    		# Create circle control object
    		ctrl = cmds.circle( n=info[1], nr=(0, 0, 1), c=(0, 0, 0) )
    		# Parent the control to the group
    		cmds.parent(ctrl, ctrlgrp)
    		# Move the group to the joint
    		cmds.xform(ctrlgrp, t=pos, ws=True)

    def calculatePVPosition(self, jnts):
        from maya import cmds , OpenMaya
        start = cmds.xform(jnts[0] ,q=True ,ws=True, t=True)
        mid = cmds.xform(jnts[1] ,q=True ,ws=True, t=True)
        end = cmds.xform(jnts[2] ,q=True ,ws=True, t=True)
        startV = OpenMaya.MVector(start[0] ,start[1],start[2])
        midV = OpenMaya.MVector(mid[0] ,mid[1],mid[2])
        endV = OpenMaya.MVector(end[0] ,end[1],end[2])
        startEnd = endV - startV
        startMid = midV - startV
        dotP = startMid * startEnd
        proj = float(dotP) / float(startEnd.length())
        startEndN = startEnd.normal()
        projV = startEndN * proj
        arrowV = startMid - projV
        arrowV*= 0.5
        finalV = arrowV + midV
        return ([finalV.x , finalV.y ,finalV.z])


