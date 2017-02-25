import maya.cmds as cmds
import json
import os
import system.utils as utils
reload(utils)

# We can use variables above the class level that can be read on class import
# This is also known as an attribute of a class
classname = 'Rig_Arm'
lytfile = 'arm.json'
numjnts = 4

class Rig_Arm:
    def __init__(self, *args):
        # Get our joint lists from a json file.
        print os.environ["RDOJO_DATA"]
        data_path = os.environ["RDOJO_DATA"] + '/rig/arm.json'
        # Use our readJson function
        data = utils.readJson(data_path)
        # Load the json into a dictionary
        self.module_info = json.loads( data )
        """ NOTE: If we wanted to build our arm from some set of joints
        in the scene, we could overwrite self.module_info['positions']"""
        # Make a new dictionary to store information about the arm rig.
        self.rig_info = {}

        # Here we will see if we have a selection to get new positions from.
        if len(cmds.ls(sl=True, type='joint')) == numjnts :
            sel=cmds.ls(sl=True, type='joint')
            positions = []
            for s in sel:
                positions.append(cmds.xform(s, q=True, ws=True, t=True))
            self.rig_info['positions']=positions

        else:
            self.rig_info['positions']=self.module_info['positions']

        """ Instead of the else:, we could just return a message that the selection
        does not meet requirements for an arm. """


        """ What if we want a left and a right arm?  For now we will set
        a temporary variable to override the name, but later we will build
        this into the UI """
        self.instance = '_L_'

        # Run rig_arm function
        self.rig_arm()


    def rig_arm(self):
        cmds.select(d=True)
        # Create Ik joints
        self.rig_info['ikjnts']=utils.createJoint(self.module_info['ikjnts'], self.rig_info['positions'], self.instance)

        # Create Fk joints
        self.rig_info['fkjnts']=utils.createJoint(self.module_info['fkjnts'], self.rig_info['positions'], self.instance)
 
        # Create Rig joints
        self.rig_info['rigjnts']=utils.createJoint(self.module_info['rigjnts'], self.rig_info['positions'], self.instance)
        

        # Create Ik Rig
        # Ik handle
        #"ikcontrols": ["ctrl_ik_arm, ikh_arm", "ctrl_pv_arm"
        # Generate a name for the ik handle using self.instance
        ikhname = self.module_info["ikcontrols"][1].replace('_s_', self.instance)
        self.rig_info['ikh']=cmds.ikHandle(n=ikhname, sj=self.rig_info['ikjnts'][0], ee=self.rig_info['ikjnts'][2], sol='ikRPsolver', p=2, w=1 )

        self.rig_info['ikcontrol']=utils.createControl([[self.rig_info['positions'][2], self.module_info["ikcontrols"][0]]])[0]

        pvpos = utils.calculatePVPosition([self.rig_info['ikjnts'][0], self.rig_info['ikjnts'][1], self.rig_info['ikjnts'][2]])

        self.rig_info['pvcontrol']=utils.createControl([[pvpos, self.module_info["ikcontrols"][2]]])[0]

        # Make a control for arm settings
        self.rig_info['setcontrol']=utils.createControl([[self.rig_info['positions'][2], 'ctrl_settings']])[0]
        cmds.addAttr(self.rig_info['setcontrol'][1], ln='IK_FK', at="enum", en="fk:ik:", k=True )

        # Parent ikh to ctrl
        cmds.parent(self.rig_info['ikh'][0], self.rig_info['ikcontrol'][1])

        # PV constraint
        cmds.poleVectorConstraint(self.rig_info['pvcontrol'][1], self.rig_info['ikh'][0])
    
        # orient constrain arm ik_wrist to ctrl_arm
        cmds.orientConstraint(self.rig_info['ikcontrol'][1], self.rig_info['ikjnts'][2], mo=True)

        # Create FK rig   
        self.rig_info['fkcontrols'] = utils.createControl([[self.rig_info['positions'][0], self.module_info["fkcontrols"][0]],
        [self.rig_info['positions'][1], self.module_info["fkcontrols"][1]],
        [self.rig_info['positions'][2], self.module_info["fkcontrols"][2]]])

        # Parent fk controls      
        cmds.parent(self.rig_info['fkcontrols'][2][0], self.rig_info['fkcontrols'][1][1])
        cmds.parent(self.rig_info['fkcontrols'][1][0], self.rig_info['fkcontrols'][0][1])

        # Connect Ik and Fk to Rig joints
        switchattr = self.rig_info['setcontrol'][1] + '.IK_FK'
        utils.connectThroughBC(self.rig_info['ikjnts'], self.rig_info['fkjnts'], self.rig_info['rigjnts'], self.instance, switchattr )
  
        # Constrain fk joints to controls.
        [cmds.parentConstraint(self.rig_info['fkcontrols'][i][1], self.rig_info['fkjnts'][i]) for i in range(len(self.rig_info['fkcontrols']))]





