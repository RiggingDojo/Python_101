import maya.cmds as cmds

# The UI class
class RDojo_UI:

    def __init__(self, *args):
        print 'In RDojo_UI'
        mi = cmds.window('MayaWindow', ma=True, q=True)
        for m in mi:
            if m == 'RDojo_Menu':
                cmds.deleteUI('RDojo_Menu', m=True)

        mymenu = cmds.menu('RDojo_Menu', label='RDMenu', to=True, p='MayaWindow')
        cmds.menuItem(label='Rig Tool', parent=mymenu, command=self.ui)

        """ Create a dictionary to store UI elements.
        This will allow us to access these elements later. """
        self.UIElements = {}

    def ui(self, *args):
        """ Check to see if the UI exists """
        windowName = "Window"
        if cmds.window(windowName, exists=True):
            cmds.deleteUI(windowName)
        """ Define width and height for buttons and windows"""    
        windowWidth = 480
        windowHeight = 80
        buttonWidth = 100
        buttonHeight = 30

        self.UIElements["window"] = cmds.window(windowName, width=windowWidth, height=windowHeight, title="RDojo_UI", sizeable=True)

        self.UIElements["mainColLayout"] = cmds.columnLayout( adjustableColumn=True )
        self.UIElements["guiFrameLayout1"] = cmds.frameLayout( label='Layout', borderStyle='in', p=self.UIElements["mainColLayout"] )
        self.UIElements["guiFlowLayout1"] = cmds.flowLayout(v=False, width=windowWidth, height=windowHeight/2, wr=True, bgc=[0.2, 0.2, 0.2], p=self.UIElements["guiFrameLayout1"])
        
        # Menu listing all the layout files.
        cmds.separator(w=10, hr=True, st='none', p=self.UIElements["guiFlowLayout1"])
        self.UIElements["rig_button"] = cmds.button(label='rig arm', width=buttonWidth, height=buttonHeight, bgc=[0.2, 0.4, 0.2], p=self.UIElements["guiFlowLayout1"], c=self.rigarm) 

        """ Show the window"""
        cmds.showWindow(windowName)

        
    def rigarm(*args):
        import rig.rig_arm as rig_arm
        reload(rig_arm)
        rig_arm = rig_arm.Rig_Arm()
        rig_arm.rig_arm()


