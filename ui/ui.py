import pymel.core as pm 

print 'UI'

def rigarm(*args):
	print 'Rig_Arm'

	import rig.rig_arm as rig_arm
	reload(rig_arm)

mymenu = pm.menu('RDojo_Menu', label='RDMenu', tearOff=True, parent='MayaWindow')
pm.menuItem(label='Rig_Arm', parent=mymenu, command=rigarm)
