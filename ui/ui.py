import maya.cmds as cmds
import os
from functools import partial

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

        # This dictionary will store all of the available rigging modules.
        self.rigmodlst = []
        rigcontents = os.listdir(os.environ["RDOJO_DATA"]+ 'rig/')
        for mod in rigcontents:
            if '.pyc' not in mod or '.__init__' not in mod:
                self.rigmodlst.append(mod)
        print self.rigmodlst 

    def ui(self, *args):
        """ Check to see if the UI exists """
        windowName = "Window"
        if cmds.window(windowName, exists=True):
            cmds.deleteUI(windowName)
        """ Define width and height for buttons and windows"""    
        windowWidth = 480
        windowHeight = 80
        buttonWidth = 55
        buttonHeight = 30

        self.UIElements["window"] = cmds.window(windowName, width=windowWidth, height=windowHeight, title="RDojo_UI", sizeable=True)

        self.UIElements["mainColLayout"] = cmds.columnLayout( adjustableColumn=True )
        self.UIElements["guiFrameLayout1"] = cmds.frameLayout( label='Layout', borderStyle='in', p=self.UIElements["mainColLayout"] )
        self.UIElements["guiFlowLayout1"] = cmds.flowLayout(v=False, width=windowWidth, height=windowHeight/2, wr=True, bgc=[0.2, 0.2, 0.2], p=self.UIElements["guiFrameLayout1"])
        
        # Dynamically make a button for each rigging module.
        for mod in self.rigmodlst:
            buttonname = mod.replace('.py', '')
            cmds.separator(w=10, hr=True, st='none', p=self.UIElements["guiFlowLayout1"])
            self.UIElements[buttonname] = cmds.button(label=buttonname, width=buttonWidth, height=buttonHeight, bgc=[0.2, 0.4, 0.2], p=self.UIElements["guiFlowLayout1"], c=partial(self.rigmod, buttonname)) 
                                                                                                                                      

        """ Show the window"""
        cmds.showWindow(windowName)

        
    def rigmod(self, modfile, *args):
        """__import__ basically opens a module and reads some info from it 
            without actually loading the module in memory."""
        mod = __import__("rig."+modfile, {}, {}, [modfile])
        reload(mod)
        # getattr will get an attribute from a class
        moduleClass = getattr(mod, mod.classname)
        moduleInstance = moduleClass()


