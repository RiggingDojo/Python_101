import maya.cmds as cmds
import os
import system.utils as utils
reload(utils)

print "Startup"


# Change the current time unit to ntsc
cmds.currentUnit( time='ntsc' )

# Change the current linear unit to inches
cmds.currentUnit( linear='cm' )

import ui.ui as ui
reload(ui)
ui.RDojo_UI()