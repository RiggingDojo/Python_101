import maya.cmds as mc

print 'UI'

mymenu = mc.menu('RDojo_Menu', label='RDMenu', to=True, p='MayaWindow')
mc.menuItem(label='Joint_Placement', sm = True, p=mymenu)
mc.menuItem(label='Left_Arm_Placement', c='import rig.rig_arm as rig; rig.locators(\'arm\', \'L\', True, \'shoulder\', \'elbow\', \'wrist\')')
mc.menuItem(label='Right_Arm_Placement', c='import rig.rig_arm as rig; rig.locators(\'arm\', \'R\', True, \'shoulder\', \'elbow\', \'wrist\')')
mc.menuItem(label='Arm_Placement', c='import rig.rig_arm as rig; rig.locators(\'arm\', \'\', True, \'shoulder\', \'elbow\', \'wrist\')')
mc.menuItem(label='Rig', p=mymenu, sm=True)
mc.menuItem(label='Rig_Left_Arm', c='import rig.rig_arm as rig; rig.rig_arm(\'arm\', \'L\', \'bind_\')')
mc.menuItem(label='Rig_Right_Arm', c='import rig.rig_arm as rig; rig.rig_arm(\'arm\', \'R\', \'bind_\')')
mc.menuItem(label='Rig_Generic_Arm', c='import rig.rig_arm as rig; rig.rig_arm(\'arm\', \'\', \'bind_\')')
