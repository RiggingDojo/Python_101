import maya.cmds as cmds
import json
import os
import system.utils as utils
reload(utils)


class Rig():
    def __init__(self, uiinfo, datapath, numjnts):
        self.rig_info = self.collectRigData(uiinfo, datapath, numjnts)
        self.numjnts = numjnts

        # Create a master asset
        if cmds.objExists == True:
            self.rig_info['mainasset'] = self.module_info['rootname'] + self.rig_info['instance'] + 'ASSET'
        else:
            self.rig_info['mainasset'] = cmds.container(
                n=self.module_info['rootname'] + self.rig_info['instance'] + 'ASSET')


        #cmds.addAttr(self.rig_info['mainasset'], sn=)

    def install(self):
        print 'In Rig Install'

        return

    def layout(self):
        lytpath = os.environ["RIGGING_TOOL"] + '/layout/layout_chain.ma'

        cmds.namespace(set=':')
        for n in range(self.numjnts - 1):
            fileinfo = cmds.file(lytpath, i=True, ns=self.module_info['rootname'] + self.rig_info['instance'] + str(n), rnn=True)
            cmds.namespace(set=':')
            assetroot = self.module_info['rootname'] + self.rig_info['instance'] + str(n) + ':lyt_main_GRP_AST'
            cmds.xform(assetroot, ws=True, t=self.rig_info['positions'][n])

            lytend = self.module_info['rootname'] + self.rig_info['instance'] + str(n) + ':lyt_end_CTRL'
            cmds.xform(lytend, ws=True, t=self.rig_info['positions'][n + 1])

            for node in fileinfo:
                try:
                    cmds.container(self.rig_info['mainasset'], edit=True, an=node)
                except: pass

        return

    def ui(self):
        return

    def collectRigData(self, uiinfo, data_path, numjnts):
        self.rig_info = {}

        # Use our readJson function
        self.data_path = data_path
        data = utils.readJson(self.data_path)

        # Load the json into a dictionary
        self.module_info = json.loads(data)
        """ NOTE: If we wanted to build our arm from some set of joints
        in the scene, we could overwrite self.module_info['positions']"""
        # Make a new dictionary to store information about the arm rig.

        # Here we will see if we have a selection to get new positions from.
        self.numjnts = numjnts
        if len(cmds.ls(sl=True, type='joint')) == self.numjnts:
            sel = cmds.ls(sl=True, type='joint')
            positions = []
            for s in sel:
                positions.append(cmds.xform(s, q=True, ws=True, t=True))
            self.rig_info['positions'] = positions

        else:
            self.rig_info['positions'] = self.module_info['positions']

        #self.rig_info['rootname'] = self.module_info['rootname']
        #find all part of type in the scene.  Make this cleaner once we use assets
        assetlist = cmds.ls(type='container')

        partlist = []
        for a in assetlist:
            if a.endswith('ASSET'):
                partlist.append(a)

        # Find the instance of the object
        self.rig_info['partnum'] = 1
        self.rig_info['partnum'] = str(utils.findHighestTrailingNumber(partlist, self.module_info['rootname'] + uiinfo['side']))

        self.rig_info['instance'] = uiinfo['side'] + self.rig_info['partnum'] + '_'

        return self.rig_info

    def createJoint(self, name, position, instance, *args):
        # Use a list comprehension to build joints.
        jnt_list = [cmds.joint(n=name[i].replace('_s_', instance), p=position[i]) for i in range(len(name))]
        cmds.select(d=True)
        return (jnt_list)

    def createControl(self, ctrlinfo):
        control_info = []
        for info in ctrlinfo:
            print info
            # Create ik control
            # Get ws position of the joint
            pos = info[0]
            # Create circle control object
            ctrl_file = os.environ["RDOJO_DATA"] + 'controls/' + info[2]
            print ctrl_file
            # Import a control object
            cmds.file(ctrl_file, i=True)
            ctrl = info[1]
            ctrlgrp = 'grp_' + info[1]
            if cmds.objExists('grp_control') == True:
                cmds.rename('grp_control', ctrlgrp)
                cmds.rename('control', ctrl)
            # Move the group to the joint
            cmds.xform(ctrlgrp, t=pos, ws=True)
            control_info.append([ctrlgrp, ctrl])
        return (control_info)

    def connectThroughBC(self, parentsA, parentsB, children, switchattr, instance, *args):
        constraints = []
        for j in range(len(children)):
            switchPrefix = children[j].partition('_')[0]
            bcNodeT = cmds.shadingNode("blendColors", asUtility=True, n='bcNodeT_switch_' + self.rig_info['instance'] + switchPrefix)
            if switchattr:
                cmds.connectAttr(switchattr, bcNodeT + '.blender')
            bcNodeR = cmds.shadingNode("blendColors", asUtility=True, n='bcNodeR_switch_' + switchPrefix)
            if switchattr:
                cmds.connectAttr(switchattr, bcNodeR + '.blender')
            bcNodeS = cmds.shadingNode("blendColors", asUtility=True, n='bcNodeS_switch_' + switchPrefix)
            if switchattr:
                cmds.connectAttr(switchattr, bcNodeS + '.blender')
            constraints.append([bcNodeT, bcNodeR, bcNodeS])
            # Input Parents
            cmds.connectAttr(parentsA[j] + '.translate', bcNodeT + '.color1')
            cmds.connectAttr(parentsA[j] + '.rotate', bcNodeR + '.color1')
            cmds.connectAttr(parentsA[j] + '.scale', bcNodeS + '.color1')
            if parentsB != 'None':
                cmds.connectAttr(parentsB[j] + '.translate', bcNodeT + '.color2')
                cmds.connectAttr(parentsB[j] + '.rotate', bcNodeR + '.color2')
                cmds.connectAttr(parentsB[j] + '.scale', bcNodeS + '.color2')
            # Output to Children
            cmds.connectAttr(bcNodeT + '.output', children[j] + '.translate')
            cmds.connectAttr(bcNodeR + '.output', children[j] + '.rotate')
            cmds.connectAttr(bcNodeS + '.output', children[j] + '.scale')
        return constraints




