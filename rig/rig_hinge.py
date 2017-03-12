import maya.cmds as cmds
import json
import os
#import system.rig as rig
import system.rig as rig
import system.utils as utils
reload(utils)
reload(rig)


# We can use variables above the class level that can be read on class import
# This is also known as an attribute of a class

CLASSNAME = 'Rig_Hinge'
TITLE = 'Hinge'
DATAPATH = os.environ["RDOJO_DATA"] + '/rig/hinge.json'

class Rig_Hinge(rig.Rig):
    def __init__(self, uiinfo, datapath, *args):
        self.numjnts = 4
        rig.Rig.__init__(self, uiinfo, datapath, self.numjnts)

    def install(self):

        rig.Rig.install(self)
        cmds.select(d=True)
        # Create Ik joints
        self.rig_info['ikjnts'] = rig.Rig.createJoint(self, self.module_info['ikjnts'], self.rig_info['positions'],
                                                        self.rig_info['instance'])

        # Create Fk joints
        self.rig_info['fkjnts'] = rig.Rig.createJoint(self, self.module_info['fkjnts'], self.rig_info['positions'],
                                                    self.rig_info['instance'])

        # Create Rig joints
        self.rig_info['rigjnts'] = rig.Rig.createJoint(self, self.module_info['rigjnts'], self.rig_info['positions'],
                                                     self.rig_info['instance'])

        # connect joint chains
        self.rig_info['bccons'] = rig.Rig.connectThroughBC(self, self.rig_info['ikjnts'], self.rig_info['fkjnts'], self.rig_info['rigjnts'], None, self.rig_info['instance'])

        for key, val in self.rig_info.iteritems():
            for item in self.rig_info[key]:
                try:
                    cmds.container(self.rig_info['mainasset'], edit=True, an=item)
                except:
                    pass
    def layout(self):
        rig.Rig.layout(self)

    def ui(self):
        print "hinge ui"
        uielements = []
        cb = cmds.checkBox(label='mirror')
        return ([cb, 'hinge_mirror_cb'])
