import maya.cmds as cmds
import json
import os
import system.utils as utils
reload(utils)

import system.rig as rig

# We can use variables above the class level that can be read on class import
# This is also known as an attribute of a class

CLASSNAME = 'Rig_Hinge'
TITLE = 'Hinge'
DATAPATH = os.environ["RDOJO_DATA"] + '/rig/hinge.json'

class Rig_Hinge(rig.Rig):
    def __init__(self, *args):
        print "Hinge"

        self.numjnts = 4

    def install(self, uiinfo, datapath):
        self.rig_info = self.collectRigData(datapath, self.numjnts)
        print self.rig_info

        cmds.select(d=True)
        # Create Ik joints
        self.rig_info['ikjnts'] = self.createJoint(self.module_info['ikjnts'], self.rig_info['positions'],
                                                        self.instance)

        # Create Fk joints
        self.rig_info['fkjnts'] = self.createJoint(self.module_info['fkjnts'], self.rig_info['positions'],
                                                    self.instance)

        # Create Rig joints
        self.rig_info['rigjnts'] = self.createJoint(self.module_info['rigjnts'], self.rig_info['positions'],
                                                     self.instance)


        # connect joint chains
        self.connectThroughBC(self.rig_info['ikjnts'], self.rig_info['fkjnts'], self.rig_info['rigjnts'], None, '_01')


    def layout(self, uiinfo, datapath):
        self.rig_info = self.collectRigData(datapath, self.numjnts)
        self.createLayout(self.module_info["rootname"], self.numjnts)
