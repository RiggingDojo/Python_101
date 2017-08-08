import maya.cmds as cmds
import json
import os
import rig_hinge as rig_hinge

import system.utils as utils
reload(utils)


# We can use variables above the class level that can be read on class import
# This is also known as an attribute of a class

CLASSNAME = 'Rig_Leg'
TITLE = 'Leg'
DATAPATH = os.environ["RDOJO_DATA"] + '/rig/leg.json'

class Rig_Leg(rig_hinge.Rig_Hinge):
    def __init__(self, uiinfo, *args):
        print "Leg"

        self.numjnts = 6
        rig_hinge.Rig_Hinge.__init__(self, uiinfo, self.numjnts)

    def install(self):
        rig_hinge.Rig_Hinge.install(self)

    def layout(self):
        rig_hinge.Rig_Hinge.layout(self)

    def ui(self, parentlyt):
        print "Leg UI"
        uielements = []
        cb = cmds.checkBox(label='mirror', p=parentlyt)
        return ([[cb, 'mirror_cb']])