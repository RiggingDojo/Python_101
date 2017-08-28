import maya.cmds as mc
import rig.rig_arm as rig
from functools import partial

null = rig.arm('null')

def rigAll(*args):

    for x in null.armList:
        if mc.objExists(x):
            null.rig_arm(x, 'bind_')

def rigLocators(name, side, ori, alt, *args):
    hinge = rig.arm(name, side)
    hinge.locators(ori, alt, args)

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
                    c=partial(rigLocators, 'arm', 'L', 'x', True, 'shoulder', 'elbow', 'wrist'))
        mc.menuItem(label='Right_Arm_Placement',
                    c=partial(rigLocators, 'arm', 'R', '-x', True, 'shoulder', 'elbow', 'wrist'))
        mc.menuItem(label='Rig', c=rigAll, p=mymenu)
        mc.menuItem(label='Advanced Rig Tool', parent=mymenu, command=self.ui)

        self.UIElements = {}

    def ui(self, *args):
        windowName = 'RDojo_Advanced'
        windowWidth = 500
        windowHeight = 500

        if mc.window(windowName, exists=True):
            mc.deleteUI(windowName)

        self.UIElements['window'] = mc.window(windowName, w=windowWidth, h = windowHeight, title = 'RDojo_UI', s=True)

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

        mc.separator(h=15, w=15, style='in', p=self.UIElements['mainColumn'])

        mc.text(l='Joint Names:', al='left', p=self.UIElements['mainColumn'])
        self.UIElements['joint01'] = mc.textField('joint01', text='shoulder', p=self.UIElements['mainColumn'])
        self.UIElements['joint02'] = mc.textField('joint02', text='elbow', p=self.UIElements['mainColumn'])
        self.UIElements['joint03'] = mc.textField('joint03', text='wrist', p=self.UIElements['mainColumn'])

        mc.button(l='Make Locators', c=self.makeLocators, p=self.UIElements['mainColumn'])
        mc.button(l='Rig', c=rigAll, p=self.UIElements['mainColumn'])

        mc.showWindow(windowName)

    def makeLocators(self, *args):
        name = mc.textField(self.UIElements['name'], query = True, text = True)
        side = mc.textField(self.UIElements['side'], query = True, text = True)
        ori = mc.radioCollection(self.UIElements['orientationRadio'], q=True, sl=True)
        negative = mc.checkBox(self.UIElements['negative'], q=True, v=True)
        alt = mc.checkBox(self.UIElements['alternate'], q=True, v=True)
        joint01 = mc.textField(self.UIElements['joint01'], query = True, text = True)
        joint02 = mc.textField(self.UIElements['joint02'], query = True, text = True)
        joint03 = mc.textField(self.UIElements['joint03'], query = True, text = True)
        sign = ''

        if negative == True:
            sign = sign + '-'

        hinge = rig.arm(name, side)
        hinge.locators(sign + ori, alt, joint01, joint02, joint03)


