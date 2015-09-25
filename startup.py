import maya.cmds as cmds

print "Startup"

# Change the current time unit to ntsc
cmds.currentUnit( time='ntsc' )

# Change the current linear unit to inches
cmds.currentUnit( linear='cm' )

import ui.ui as ui
reload(ui)