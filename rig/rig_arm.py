import maya.cmds as mc
import system.utils as utils


class arm:

    #whenever we instantiate our arm class, we will add the instance to our armList so that we can call all of them at once later on.
    armList = []

    def __init__(self, name, side = ''):
        self.name = name
        self.side = side
        if self.side != '':
            self.fullName = self.side + '_' + self.name
            self.armList.append(self.fullName)
        else:
            self.fullName = self.name
            self.armList.append(self.fullName)

    def rig_arm(self, name, prefix):

        # create our group nodes to keep everything tidy
        if utils.organizationGroupExists() == False:
            utils.organizationGroup()

        # makes joints based on the locator positions. Orient the joints down X, send the rotate values to joint orient, and parent the chain in a hierarchy
        bind_joints = utils.makeJointChain('joints_grp', prefix, name)
        utils.rotateToJointOrient(utils.orientChain(bind_joints, orientation='x'))
        utils.parentChain(bind_joints)

        # duplicate bind shoulder to make FK chain, make fk cntrls, connect fk cntrls to fk joints, make a volumetric scaling for FK
        FK_joints = utils.duplicateNewName(utils.getEnds(bind_joints)[0], prefix, 'FK_', 13)
        FK_cntrls = utils.cntrlHierarchy(FK_joints, 1, 13, toParent='cntrl_grp')
        utils.constrainLists(FK_cntrls, FK_joints, "yes", "yes", "none")
        utils.volumetricFK(FK_cntrls, FK_joints, orientation='x')

        # duplicate bind joints to make IK chain. Make cntrl for the end of the IK. make the IK then make the IK joints stretchy.
        IK_joints = utils.duplicateNewName(bind_joints[0], prefix, 'IK_', 15)
        IK_cntrls = utils.cntrlHierarchy(utils.getEnds(IK_joints)[1], 1.5, 24, toParent='cntrl_grp')
        utils.makeIK(IK_joints, IK_cntrls)
        utils.stretchyIK(IK_cntrls, IK_joints, orientation='x', global_cntrl='global_cntrl')

        # makes a blend between the fk and ik joints affecting the bind joints
        utils.blendThree(bind_joints, FK_joints, IK_joints, 'global_cntrl', 'FKIK', name)

    #function to make locators on screen. specify orientaion, if you want it to alternate, and the name of the locators
    def locators(self, orientation, alternating, *args):

        #it all start at the origin
        x = 0
        y = 0
        z = 0
        d1 = 6
        d2 = 2

        #this list will hold our locators so that we can keep track of them
        locList = []

        #make orientation capital to make it easier to compare
        orientation = orientation.upper()

        # we may be passing args in args, so this takes care of that
        argsList = list(args)

        for i in argsList[0]:
            print type(i)
            if isinstance(i, bool) == True:
                argsList = argsList[0]
                list2 = list(argsList)
                for n in list2:
                    if isinstance(n, bool) == True:
                        list2.remove(n)
                        argsList = list2

        #function to figure out the placement based on given orientation and distance
        def evaluate(ori, alt, oriDistance, aimDistance, o, k):
            if '-' in ori:
                o = o - oriDistance
                if alt == True:
                    if k == aimDistance:
                        k = 0
                    else:
                        k = aimDistance
            else:
                o = o + oriDistance
                if alt == True:
                    if k == aimDistance:
                        k = 0
                    else:
                        k = aimDistance

            returnList = []
            returnList.append(o)
            returnList.append(k)

            #return a list with o and k which are values
            return returnList

        #make a group to organize our locators and lock it.
        tempGrp = mc.createNode('transform', n=self.fullName)
        utils.lockHideAttr(tempGrp, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'visibility'], True, True)

        for object in argsList:

            print object
            #make a locator, place it whatever x, y, z is, center its pivot and add it to the list
            loc = mc.spaceLocator(p=[x, y, z], n=self.side + '_' + object, a=True)
            mc.xform(cp=True)
            locList.append(loc)

            #here is how to figure out x y z
            if orientation == 'X' or orientation == '-X':
                x = evaluate(orientation, alternating, d1, -d2, x, z)[0]
                z = evaluate(orientation, alternating, d1, -d2, x, z)[1]
            elif orientation == 'Y' or orientation == '-Y':
                y = evaluate(orientation, alternating, d1, d2, y, z)[0]
                z = evaluate(orientation, alternating, d1, d2, y, z)[1]
            elif orientation == 'Z' or orientation == '-Z':
                z = evaluate(orientation, alternating, d1, d2, z, y)[0]
                y = evaluate(orientation, alternating, d1, d2, z, y)[1]

        #reverse the list so we can start from the bottom and parent up
        locList.reverse()

        for i in range(len(locList)):

            #if the object is not the last object of the list(the top parent), then parent the object to the object after it in the list
            if locList[i] != locList[-1]:
                mc.parent(locList[i], locList[i + 1])

            #if the object is the last object in the list(the top parent), then parent the object to the group we made
            elif locList[i] == locList[-1]:
                mc.parent(locList[i], tempGrp)


