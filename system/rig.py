import maya.cmds as cmds
import json
import os
import system.utils as utils
reload(utils)

class Rig():
    def __init__(self, uiinfo, numjnts):
        self.uiinfo = uiinfo
        self.numjnts = numjnts
        self.datapath = uiinfo['datapath']
        self.modFile = uiinfo['modfile']
        self.moduleInstance = uiinfo['moduleClass']

        # Dictionary to store rig specific data
        # rig_info stores all data needed to build the rig.
        self.rig_info = {}
        # declare some default values to override later
        self.rig_info['partnum'] = 1

        # Use our readJson function
        data = utils.readJson(self.datapath)
        # Load the json into a dictionary
        # module_info stores all the data needed to build the layout object
        self.module_info = json.loads(data)

    def install(self):
        print 'In Rig Install'
        self.collectRigData()

        if self.rig_info:
            print "Ready for Install"
        else:
            return

    def layout(self):
        # Initialize the part
        self.part()

        lytpath = os.environ["RIGGING_TOOL"] + '/layout/layout_chain.ma'

        cmds.namespace(set=':')
        for n in range(self.numjnts - 1):
            fileinfo = cmds.file(lytpath, i=True, ns=self.module_info['rootname'] + self.module_info['instance'] + str(n), rnn=True)
            cmds.namespace(set=':')
            lytroot = self.module_info['rootname'] + self.module_info['instance'] + str(n) + ':lyt_root_CTRL_GRP'
            cmds.xform(lytroot, ws=True, t=self.module_info['positions'][n])

            lytend = self.module_info['rootname'] + self.module_info['instance'] + str(n) + ':lyt_end_CTRL_GRP'
            cmds.xform(lytend, ws=True, t=self.module_info['positions'][n + 1])

            for node in fileinfo:
                try:
                    cmds.container(self.module_info['layoutasset'], edit=True, an=node)
                except: pass

        return

    def part(self):
        partlist = self.findPartsInScene()
        # Find the instance of the object
        self.module_info['partnum'] = str(
            utils.findHighestTrailingNumber(partlist, self.module_info['rootname'] + self.uiinfo['side']))

        self.module_info['instance'] = self.uiinfo['side'] + self.module_info['partnum'] + '_'

        # Create a master asset
        if cmds.objExists(self.module_info['rootname'] + self.module_info['instance'] + 'ASSET') == True:
            # NOTE:  This would be a good place to further check for asset contents
            self.module_info['mainasset'] = self.module_info['rootname'] + self.module_info['instance'] + 'ASSET'
        else:
            self.module_info['mainasset'] = cmds.container(
                n=self.module_info['rootname'] + self.module_info['instance'] + 'ASSET')


        # Create a layout asset
        self.module_info['layoutasset'] = cmds.container(
            n=self.module_info['rootname'] + self.module_info['instance'] + 'LAYOUT')
        # Add the layout to the main
        cmds.container(self.module_info['mainasset'] , edit=True, an=self.module_info['layoutasset'] )

        # Add attributes to the asset
        self.addAssetAttrs()

    def addAssetAttrs(self):
        attrlist = (['modclass', self.moduleInstance],
                    ['partnum', self.module_info['partnum']],
                    ['rootname',self.module_info['rootname']],
                    ['instance', self.module_info['instance']],
                    ['mainasset', self.module_info['mainasset']],
                    ['layoutasset', self.module_info['layoutasset']])

        for a in attrlist:
            if cmds.attributeQuery(a[0], node=self.module_info['mainasset'], ex=True):
                pass
            else:
                cmds.addAttr(self.module_info['mainasset'], sn=a[0], dt='string', k=False)
                cmds.setAttr(self.module_info['mainasset'] + '.' + a[0], a[1], type='string')

    def queryAssetAttrs(self):
        attrlist = ('modclass',
                    'rootname',
                    'instance',
                    'mainasset',
                    'layoutasset')
        for a in attrlist:
            if cmds.attributeQuery(a, node=self.rig_info['mainasset'], ex=True):
                val = cmds.getAttr(self.rig_info['mainasset'] + '.' + a)
                self.rig_info[a] = val

    @staticmethod
    def findPartsInScene():
        # find all part of type in the scene.
        assetlist = cmds.ls(type='container')

        partlist = []
        for a in assetlist:
            if a.endswith('ASSET'):
                partlist.append(a)
        return partlist

    def ui(self):
        return

    def collectRigData(self):
        """
        Function used to collect the data we need to build the rig
        :return:
        """

        self.queryPartAsset()
        self.queryAssetAttrs()

        if self.rig_info['layoutasset']:
            # We identified the part.
            # get the positions of the joints
            for item in cmds.container(self.rig_info['layoutasset'], q=True, nl=True):
                if cmds.nodeType(item) == 'joint' and item.endswith('lyt_JNT') == True:
                    pos = cmds.xform(item, q=True, ws=True, t=True)
                    self.rig_info.setdefault('positions', []).append(pos)

            self.rig_info['instance'] = cmds.getAttr(self.rig_info['mainasset'] + '.instance')

        else:
            raise RuntimeError('No Valid Layout Selected.')

    def queryPartAsset(self):
        """
        function used to find the main asset
        :return:
        """

        sel = cmds.ls(sl=True)
        if sel:
            # Navigate up to see if the selection is an asset or a child of one.
            parentcon = cmds.container(q=True, fc=sel[0])
            if parentcon:
                # Look for the main asset
                maincon = cmds.container(q=True, fc=parentcon)
                if maincon:
                    # Look for identifier
                    if cmds.attributeQuery('modclass', node=maincon, ex=True):
                        # We found an asset
                        self.rig_info['mainasset'] = maincon

            elif cmds.nodeType(sel[0]) == 'container':
                maincon = cmds.container(q=True, fc=sel[0])
                if maincon:
                    # Look for identifier
                    if cmds.attributeQuery('modclass', node=maincon, ex=True):
                        # We found an asset
                        self.rig_info['mainasset'] = maincon

                else:
                    #We must have selected the main asset
                    if cmds.attributeQuery('modclass', node=sel[0], ex=True):
                        # We found an asset
                        self.rig_info['mainasset'] = maincon

            else:
                raise RuntimeError('No Valid Layout Found.')


    def createJoint( self, name, position, instance, *args):
        # Use a list comprehension to build joints.
        jnt_list = [cmds.joint(n=name[i].replace('_s_', instance), p=position[i]) for i in range(len(name)-1)]
        cmds.select(d=True)
        return (jnt_list)

    def createControl(self, ctrlinfo):
        control_info = []
        for info in ctrlinfo:
            # Create ik control
            # Get ws position of the joint
            pos = info[0]
            # Create circle control object
            ctrl_file = os.environ["RDOJO_DATA"] + 'controls/' + info[2]
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




