import maya.cmds as mc
import system.utils as utils

def rig_arm(name, side, prefix):

    fullName = side + '_' + name

    #create our group nodes to keep everything tidy
    if utils.organizationGroupExists() == False:
        utils.organizationGroup()

    #makes joints based on the locator positions. Orient the joints down X, send the rotate values to joint orient, and parent the chain in a hierarchy
    bind_joints = utils.makeJointChain('joints_grp', prefix, fullName)
    utils.rotateToJointOrient(utils.orientChain(bind_joints, orientation='x'))
    utils.parentChain(bind_joints)

    #duplicate bind shoulder to make FK chain, make fk cntrls, connect fk cntrls to fk joints, make a volumetric scaling for FK
    FK_joints = utils.duplicateNewName(utils.getEnds(bind_joints)[0], prefix, 'FK_', 13)
    FK_cntrls = utils.cntrlHierarchy(FK_joints, 1, 13, toParent='cntrl_grp')
    utils.constrainLists(FK_cntrls, FK_joints, "yes", "yes", "none")
    utils.volumetricFK(FK_cntrls, FK_joints, orientation='x')

    #duplicate bind joints to make IK chain. Make cntrl for the end of the IK. make the IK then make the IK joints stretchy.
    IK_joints = utils.duplicateNewName(bind_joints[0], prefix, 'IK_', 15)
    IK_cntrls = utils.cntrlHierarchy(utils.getEnds(IK_joints)[1], 1.5, 24, toParent='cntrl_grp')
    utils.makeIK(IK_joints, IK_cntrls)
    utils.stretchyIK(IK_cntrls, IK_joints, orientation='x', global_cntrl='global_cntrl')

    #makes a blend between the fk and ik joints affecting the bind joints
    utils.blendThree(bind_joints, FK_joints, IK_joints, 'global_cntrl', 'FKIK', fullName)


def locators(name, side, alternating, *args):
    i = 0
    alt = 0
    list = []

    fullName = side + '_' + name

    tempGrp = mc.createNode('transform', n=fullName)
    utils.lockHideAttr(tempGrp, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'visibility'], True, True)

    for object in args:
        loc = mc.spaceLocator(p=[i, 0, alt], n=side + '_' + object, a=True)
        mc.xform(cp=True)
        list.append(loc)
        if side == 'r' or side == 'R' or side == 'right' or side == 'Right' or side == 'RIGHT':
            i = i - 6
        else:
            i = i + 6

        if alternating == True:
            if alt == -2:
                alt = 0
            else:
                alt = -2

    list.reverse()

    for x in range(len(list)):
        if list[x] != list[-1]:
            mc.parent(list[x], list[x + 1])
        elif list[x] == list[-1]:
            mc.parent(list[x], tempGrp)

