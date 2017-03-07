import maya.cmds as cmds
import json
import os
import rig_hinge as rig_hinge

import system.utils as utils
reload(utils)


# We can use variables above the class level that can be read on class import
# This is also known as an attribute of a class

CLASSNAME = 'Rig_Arm'
TITLE = 'Arm'
DATAPATH = os.environ["RDOJO_DATA"] + '/rig/arm.json'

class Rig_Arm(rig_hinge.Rig_Hinge):
    def __init__(self, *args):
        print "Arm"

        self.numjnts = 4

    def install(self, uiinfo, datapath):
        self.rig_info = self.collectRigData(datapath, self.numjnts)
        hinge=rig_hinge.Rig_Hinge()
        hinge.install(uiinfo, datapath)
        cmds.select(d=True)








