import maya.cmds as cmds
import json
import os
import system.utils as utils


ikjnt_list = [['ik_shoulder_jnt', [0.0, 0.0, 0.0]], ['ik_elbow_jnt', [-1.0, 0.0, 2.0]], ['ik_wrist_jnt', [0.0, 0.0, 4.0]], ['ik_wristEnd_jnt', [0.0, 0.0, 6.0]]]
fkjnt_list = [['fk_shoulder_jnt', [0.0, 0.0, 0.0]], ['fk_elbow_jnt', [-1.0, 0.0, 2.0]], ['ifk_wrist_jnt', [0.0, 0.0, 4.0]], ['fk_wristEnd_jnt', [0.0, 0.0, 6.0]]]
rigjnt_list = [['rig_shoulder_jnt', [0.0, 0.0, 0.0]], ['rig_elbow_jnt', [-1.0, 0.0, 2.0]], ['rig_wrist_jnt', [0.0, 0.0, 4.0]], ['rig_wristEnd_jnt', [0.0, 0.0, 6.0]]]

class Rig_Arm:
    def __init__(self):
        # Get our joint lists from a json file.
        data_path = os.environ["RDOJO_DATA"] + 'rig/arm.json'
        # Use our readJson function
        data = utils.readJson(data_path)
        # Load the json into a dictionary
        self.module_info = json.loads( data )
        """ NOTE: If we wanted to build our arm from some set of joints
        in the scene, we could overwrite self.module_info['positions']"""


    def rig_arm(self):
        # Create Ik joints
        self.createJoint(self.module_info['ikjnts'])
        cmds.select(d=True)
        # Create Fk joints
        self.createJoint(self.module_info['fkjnts'])
        cmds.select(d=True)
        # Create Rig joints
        self.createJoint(self.module_info['rigjnts'])
        cmds.select(d=True)


        # Create Ik Rig
        # Ik handle
        #"ikcontrols": ["ctrl_ik_arm, ikh_arm", "ctrl_pv_arm"]
        ikh = cmds.ikHandle( n=self.module_info["ikcontrols"][1], sj=self.module_info['ikjnts'][0], ee=self.module_info['ikjnts'][2], sol='ikRPsolver', p=2, w=1 )

        self.createControl([[self.module_info['positions'][2], self.module_info["ikcontrols"][0]]])

        pvpos = self.calculatePVPosition([self.module_info['ikjnts'][0], self.module_info['ikjnts'][1], self.module_info['ikjnts'][2]])

        pvctrlinfo = [[pvpos, self.module_info["ikcontrols"][2]]]
        self.createControl(pvctrlinfo)

        # Parent ikh to ctrl
        cmds.parent(self.module_info["ikcontrols"][1], self.module_info["ikcontrols"][0])

        # PV constraint
        cmds.poleVectorConstraint(self.module_info["ikcontrols"][2], self.module_info["ikcontrols"][1])

        # orient constrain arm ik_wrist to ctrl_arm
        cmds.orientConstraint(self.module_info["ikcontrols"][0], self.module_info['ikjnts'][2], mo=True)

        # Create FK rig   
        fkctrlinfo = self.createControl([[self.module_info["positions"][2], self.module_info["fkcontrols"][2]],
        [self.module_info["positions"][1], self.module_info["fkcontrols"][1]],
        [self.module_info["positions"][0], self.module_info["fkcontrols"][0]]])

        # Parent fk controls
        print fkctrlinfo
        cmds.parent(fkctrlinfo[0][0], fkctrlinfo[1][1][0])
        cmds.parent(fkctrlinfo[1][0], fkctrlinfo[2][1][0])
        # Connect Ik and Fk to Rig joints


    def createJoint(self, jntinfo):
        for i in range(len(jntinfo)):
            cmds.joint(n=jntinfo[i], p=self.module_info['positions'][i])

    def createControl(self, ctrlinfo):
        control_info = []
        for info in ctrlinfo:
            # Create ik control
            # Get ws position of wrist joint
            pos = info[0]
            # Create an empty group
            ctrlgrp = cmds.group( em=True, name='grp_' + info[1] )
            # Create circle control object
            ctrl = cmds.circle( n=info[1], nr=(0, 0, 1), c=(0, 0, 0) )
            # Parent the control to the group
            cmds.parent(ctrl, ctrlgrp)
            # Move the group to the joint
            cmds.xform(ctrlgrp, t=pos, ws=True)
            control_info.append([ctrlgrp, ctrl])
        return(control_info)


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


