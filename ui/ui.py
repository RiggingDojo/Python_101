import maya.cmds as mc
import rig.rig_arm as rig
from functools import partial
reload(rig)

null = rig.arm('null')

print 'UI'

class RDojo_UI:

    def __init__(self, *args):

        mi = mc.window('MayaWindow', ma=True, q=True)

        for m in mi:

            if m == 'RDojo_Menu':
                mc.deleteUI('RDojo_Menu', m=True)


        mymenu = mc.menu('RDojo_Menu', label='RDMenu', to=True, p='MayaWindow')
        mc.menuItem(label='Joint_Placement', sm=True, p=mymenu)
        mc.menuItem(label='Left_Arm_Placement',
                    c=partial(self.rigLocators, 'arm', 'L', 'x', True, False, 'shoulder', 'elbow', 'wrist'))
        mc.menuItem(label='Right_Arm_Placement',
                    c=partial(self.rigLocators, 'arm', 'R', '-x', True, False, 'shoulder', 'elbow', 'wrist'))
        mc.menuItem(label='Rig', c=self.rigAll, p=mymenu)
        mc.menuItem(label='Advanced Rig Tool', parent=mymenu, command=self.updateUI)

        self.windowName = 'RDojo_Advanced'
        self.UIElements = {}
        self.jointCount = 3

    def ui(self, *args):

        windowWidth = 350
        windowHeight = 400

        self.UIElements['window'] = mc.window(self.windowName, w=windowWidth, h = windowHeight, title = 'RDojo_UI', s=True)

        self.UIElements['mainColumn'] = mc.columnLayout('mainColumn', adj=True)
        self.UIElements['row01'] = mc.rowLayout('row01', numberOfColumns=5)

        mc.text(l='Name:', al='left')
        self.UIElements['name'] = mc.textField('name', text='arm', parent=self.UIElements['row01'])

        mc.separator(h=15, w=15, style="in", hr=False)

        mc.text(l='Side:', al='left')
        self.UIElements['side'] = mc.textField('side', text='', parent=self.UIElements['row01'])

        mc.separator(h=15, w=15, style='in', p=self.UIElements['mainColumn'])

        self.UIElements['row02'] = mc.rowLayout('row02', numberOfColumns=5, p=self.UIElements['mainColumn'])
        mc.text(l='Locator Orientation:', al='left', p=self.UIElements['row02'])

        self.UIElements['orientationRadio'] = mc.radioCollection('orientationRadio', p=self.UIElements['row02'])
        mc.radioButton('x', label='x', select=True, p=self.UIElements['row02'])
        mc.radioButton('y', label='y', p=self.UIElements['row02'])
        mc.radioButton('z', label='z', p=self.UIElements['row02'])

        self.UIElements['negative'] = mc.checkBox('negative', l='Negative Axis', v=False,
                                                  p=self.UIElements['mainColumn'])
        self.UIElements['alternate'] = mc.checkBox('alternate', l='Alternate', v=True, p=self.UIElements['mainColumn'])
        self.UIElements['endAim'] = mc.checkBox('endAim', l='End Aim Locator', v=True, p=self.UIElements['mainColumn'])


        mc.separator(h=15, w=15, style='in', p=self.UIElements['mainColumn'])

        mc.text(l='Joint Names:', al='left', p=self.UIElements['mainColumn'])
        for x in range(self.jointCount):
            jointName = 'joint_' + str(x)
            self.UIElements[jointName] = mc.textField(jointName, text=jointName, p=self.UIElements['mainColumn'])


        self.UIElements['row03'] = mc.rowLayout('row03', numberOfColumns=2, p=self.UIElements['mainColumn'])
        mc.button(l='Add Joint', c=self.addJoints, p=self.UIElements['row03'], w=windowWidth/2)
        #mc.separator(h=15, w=15, style="in", hr=False)
        mc.button(l='Remove Joint', c=self.removeJoints, p=self.UIElements['row03'], w=windowWidth/2)

        mc.button(l='Make Locators', c=self.makeLocators, p=self.UIElements['mainColumn'])
        mc.button(l='Rig', c=self.rigAll, p=self.UIElements['mainColumn'])

        mc.showWindow(self.windowName)
        print 'showing ui window'

    def makeLocators(self, *args):

        name = mc.textField(self.UIElements['name'], query = True, text = True)
        side = mc.textField(self.UIElements['side'], query = True, text = True)
        ori = mc.radioCollection(self.UIElements['orientationRadio'], q=True, sl=True)
        negative = mc.checkBox(self.UIElements['negative'], q=True, v=True)
        alt = mc.checkBox(self.UIElements['alternate'], q=True, v=True)
        endAim = mc.checkBox(self.UIElements['endAim'], q=True, v=True)

        sign = ''
        if negative == True:
            sign = sign + '-'

        jointNames = []
        for x in range(self.jointCount):
            jointNames.append(mc.textField(self.UIElements['joint_' + str(x)], query = True, text = True))

        hinge = rig.arm(name, side)
        hinge.locators(sign + ori, alt, endAim, jointNames)

    def rigAll(self, *args):

        for x in null.armList:
            if mc.objExists(x):
                null.rig_arm(x, 'bind_')

    def rigLocators(self, name, side, ori, alt, aim, *args):
        hinge = rig.arm(name, side)
        hinge.locators(ori, alt, aim, args)

    def addJoints(self, *args):
        self.jointCount = self.jointCount + 1
        self.updateUI()

    def removeJoints(self, *args):
        self.jointCount = self.jointCount - 1
        self.updateUI()

    def updateUI(self, *args):
        if mc.window(self.windowName, exists=True):
            mc.deleteUI(self.windowName)
            print 'deleted OLD UI'

        self.ui()

