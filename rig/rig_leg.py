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
    def __init__(self, *args):
        print "Leg"

        self.numjnts = 6

    def install(self, uiinfo, datapath):
        self.rig_info = self.collectRigData(datapath, self.numjnts)
        hinge=rig_hinge.Rig_Hinge()
        hinge.install(uiinfo, datapath)