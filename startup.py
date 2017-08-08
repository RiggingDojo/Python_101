import maya.cmds as cmds
import os
import system.utils as utils
#reload(utils)

print "Startup"


# Change the current time unit to ntsc
cmds.currentUnit( time='ntsc' )

# Change the current linear unit to inches
cmds.currentUnit( linear='cm' )

# Set a system path to files.  We can do this with the os module
#os.environ["RDOJO_DATA"] = os.environ['RIGGING_TOOL'] + '/data'

import ui.ui as ui
#reload(ui)
ui.RDojo_UI()
