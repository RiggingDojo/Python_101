import maya.cmds as mc
import pymel.core as pm


#function to get the top node of an object
def getRoot( object ):
    
    #set upParent to be object so the loop can start with it
    upParent = object
    
    #while the upParent has a parent, set the upParent to be the parent.
    while (True):
        theParent = mc.listRelatives( upParent, p = True )
        
        if not theParent:
            break;
            
        upParent = theParent[0]
        
    return upParent



#function to send rotate values to joint orient.
def rotateToJointOrient( list ):

    for object in list:
        #get rotation values of joint
        rx = mc.getAttr(object + '.rx')
        ry = mc.getAttr(object + '.ry')
        rz = mc.getAttr(object + '.rz')
        
        #set joint orient values to rotation values
        mc.setAttr(object + '.jointOrientX', rx)
        mc.setAttr(object + '.jointOrientY', ry)
        mc.setAttr(object + '.jointOrientZ', rz)
        
        #set rotation values to zero
        mc.xform(object, ro = [0, 0, 0])



#function to make a quad arrow
def create_quad_arrow( name ):
    control = mc.curve(d=1, p=[(1, 0, 1),(3, 0, 1),(3, 0, 2),(5, 0, 0),(3, 0, -2),(3, 0, -1),(1, 0, -1),(1, 0, -3),(2, 0, -3),(0, 0, -5),(-2, 0, -3),(-1, 0, -3),(-1, 0, -1),(-3, 0, -1),(-3, 0, -2),(-5, 0, 0),(-3, 0, 2),(-3, 0, 1),(-1, 0, 1),(-1, 0, 3),(-2, 0, 3),(0, 0, 5),( 2, 0, 3),(1, 0, 3),(1, 0, 1),], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
    mc.rename( name )
    #center pivot
    mc.xform(cp=True)
    #freeze transformation
    mc.makeIdentity(apply=True, t=True, r=True, s=True)
    #clear selection 
    mc.select(cl=True)



#function to duplicate an object and its children and assign new names
def duplicateNewName(object, search, replace, colour):
    
    #Make a new variable with the name of the original renamed with the replace
    objectSplit = object.split(search)
    newObject = objectSplit[0] + replace + objectSplit[1]

    #duplicate the original and name it accordingly
    mc.duplicate(object, n = newObject )
    #select its children so that they can be renamed too
    mc.select(newObject)
    
    if colour is not "none":
        mc.setAttr(newObject + '.overrideEnabled', 1)
        mc.setAttr(newObject + '.overrideColor', colour)
    
    mc.select(mc.listRelatives(ad = True, f = True))
    
    #rename the children
    for item in pm.selected():
        item.rename(item.name().replace(search, replace))
        
        
        
#make controls based on the hierarchy of a list
def cntrlHierarchy(list, radius, colour, toParent):

    cntrlList = []
    
    for object in list:
        
    
        #make a new control for object. Get the parent of the joint so that we know the order and in case it returns "None".
        cntrl = mc.circle(n = object + '_cntrl', nr = [1, 0, 0], r = radius)
        objectParent = mc.listRelatives(object, p=True)
        
        #create an empty node and parent constraint it to the object to match position and orientation
        mc.parentConstraint(object, mc.createNode ('transform', n='offset_' + object))
        mc.delete(mc.listRelatives(type='parentConstraint'))
        mc.delete('offset_' + object, ch = True)
        mc.select(cl=True)
        
        
        #parent constraint the control to the object for positionoing and orientation freeze transforms, delete history
        mc.parentConstraint(object, object + '_cntrl')
        mc.delete(mc.listRelatives(object + '_cntrl', type='parentConstraint'))
        mc.parent(object + '_cntrl', 'offset_' + object)
        mc.makeIdentity(object + '_cntrl', apply=True, t=True, r=True, s=True)
        mc.delete(object + '_cntrl', ch = True)
        
        #set the color
        mc.setAttr(object + '_cntrl' + '.overrideEnabled', 1)
        mc.setAttr(object + '_cntrl' + '.overrideColor', colour)
        
        #for the next part to work, we need the cntrls to be in the same order as the objects, so put the cntrls in a list    
        cntrlList.append(cntrl[0])
        
        
    for object, cntrl in zip(list, cntrlList):
        
        objectParent = mc.listRelatives(object, p=True)  
        
        #if the parent of selection is in the selectionAll list, parent the cntrl to the according offset (it should be the parent in the hierarchy + "cntrl")
        if objectParent is not None and objectParent[0] in list:
            mc.parent('offset_' + object, objectParent[0] + '_cntrl')
    
    #parent the root of the cntrls to specified parent        
    if toParent is not "none":
        mc.parent(getRoot(cntrlList[0]), toParent)
            
    return cntrlList



#a function to make empty group nodes to serve as offsets
def offsetCreator( list ):

    for object in list:
        
        mc.select(cl=True)
        mc.select(object)
        
        #get the objectsParent
        objectParent = mc.listRelatives(object, p=True)
        
        #create a empty transform node and parent it to the object to position and orient
        mc.parentConstraint(object, mc.createNode ('transform', n='offset_' + object))
        mc.delete(mc.listRelatives(type='parentConstraint'))
        mc.makeIdentity('offset_' + object, apply=True, t=True, r=True, s=True)
        mc.delete('offset_' + object, ch = True)
        mc.select(cl=True)
        
        #if the object has a parent, parent the offset under the object parents, and the parent the object under the offset
        if objectParent is not None:
            mc.parent('offset_' + object, objectParent)
            mc.parent(object, 'offset_' + object)
        
        #if the object doesnt have a parent it means that it is already in worldspace, in which case, just parent the object to the offset    
        elif objectParent is None:
            mc.parent(object, 'offset_' + object)            
    
#function to blend between two chains of things, such as a FK IK blend.
def blendThree(list1, list2, list3, controlToAttribute, attributeLongName):
    
    #if the lists arent the same length, spit out a warning
    if len(list1) != len(list2) and len(list3):
        mc.warning('The lists in blendThree dont have the same amount of objects') 
    
    #add the attribute to the specified object
    mc.addAttr(controlToAttribute, ln = attributeLongName, at = 'float', dv = 0, min = 0, max = 1, w = True, r = True, k = True)
    
    #list of the blend nodes we are about to make
    blendNodes = []
    
        
    for object in list1:
        
        #for all the objects in the list, make a translate and rotate blending node
        mc.shadingNode('blendColors', n = object + '_translate_' + attributeLongName + 'blend', au = True)
        mc.shadingNode('blendColors', n = object + '_rotate_' + attributeLongName + 'blend', au = True)
        
        #add the blending nodes to the list
        blendNodes.append(object + '_translate_' + attributeLongName + 'blend')
        blendNodes.append(object + '_rotate_' + attributeLongName + 'blend')  
        
        #connect the blends output to the list1 
        mc.connectAttr(object + '_translate_' + attributeLongName + 'blend.output', object + '.translate')
        mc.connectAttr(object + '_rotate_' + attributeLongName + 'blend.output', object + '.rotate')
        
        
    for object, object2 in zip(list1, list2):   
        
        #connect list 2 to the blends color2
        mc.connectAttr(object2 + '.translate', object + '_translate_' + attributeLongName + 'blend.color2')
        mc.connectAttr(object2 + '.rotate', object + '_rotate_' + attributeLongName + 'blend.color2')
        
    
    for object, object3 in zip(list1, list3):
        
        #connect list 3 to blends color 1
        mc.connectAttr(object3 + '.translate', object + '_translate_' + attributeLongName + 'blend.color1')
        mc.connectAttr(object3 + '.rotate', object + '_rotate_' + attributeLongName + 'blend.color1')
        
            
    for node in blendNodes:
        
        #connect the attribute we made to all of the blendColors "blender" attribute
        mc.connectAttr(controlToAttribute + '.' + attributeLongName, node + '.blender')

#function to constrain two lists, choose if you want a point, orient, and or scale constraint
def constrainLists(list1, list2, point, orient, size):
    
    #if statement in case you dont want a constraint
    if point is not 'none':
        
        #constraint the object of one list to the object of the other list
        for object1, object2 in zip(list1, list2):
            mc.pointConstraint(object1, object2, mo = False)
        
        
    if orient is not 'none':
        
        for object1, object2 in zip(list1, list2):
            mc.orientConstraint(object1, object2, mo = False)
    
    
    if size is not 'none':
        
        for object1, object2 in zip(list1, list2):
            mc.scaleConstraint(object1, object2, mo = False)




#makes a group for the arm rig and generates the global cntrl with an FK IK attribute, an FK stretch, and volumetric 
mc.group(n = 'arm_grp', em = True, w = True)
create_quad_arrow('global_cntrl')
mc.addAttr('global_cntrl', ln = 'FK_stretch', at = 'float', dv = 1, min = 0.01, w = True, r = True, k = True)
mc.addAttr('global_cntrl', ln = 'Volumetric', at = 'float', dv = 0, min = 0, max = 1, w = True, r = True, k = True)

#parent and group hierarchy to keep everything organized
mc.parent('global_cntrl', 'arm_grp')

mc.group(n = 'geo_grp', em = True, p = 'arm_grp')
mc.group(n = 'rig_grp', em = True, p = 'global_cntrl')
mc.group(n = 'IK_grp', em = True, p = 'rig_grp')
mc.group(n = 'joints_grp', em = True, p = 'rig_grp')
mc.group(n = 'cntrl_grp', em = True, p = 'rig_grp')
mc.select(cl=True)

#make bind shoulder joint, unselect
mc.joint(n = 'bind_shoulder', p = [2, 2, 0])
mc.select(cl= True )

#make bind elbow joint, unselect
mc.joint(n = 'bind_elbow', p = [7, 2, -1])
mc.select(cl= True )

#make bind wrist joint, unselect
mc.joint(n = 'bind_wrist', p = [12, 2, 0])
mc.select(cl= True )


#aim the elbow to the wrist so that it is correctly oriented
mc.aimConstraint('bind_wrist', 'bind_elbow', mo = False)
mc.select('bind_elbow')
mc.delete(mc.listRelatives(type="aimConstraint"))

#make list of joints you want to reorient and reorient them
reorientJointList = []
reorientJointList.append('bind_elbow')
rotateToJointOrient(reorientJointList)

#parent joints
mc.parent('bind_wrist', 'bind_elbow')
mc.parent('bind_elbow', 'bind_shoulder')
mc.parent('bind_shoulder', 'joints_grp')

#duplicate bind shoulder to make the FK and IK and replace the "bind_" accordingly
duplicateNewName('bind_shoulder', 'bind_', 'FK_', 13)
duplicateNewName('bind_shoulder', 'bind_', 'IK_', 15)

#Place the IK and FK joints in their respective lists to be able to call to them easily
joints = mc.ls(typ = 'joint')
FK_joints = []
IK_joints = []
bind_joints = []


for aJoint in joints:
    if 'FK_' in aJoint:
        FK_joints.append(aJoint)
        mc.setAttr(aJoint + '.radius', 1)
    
    if 'IK_' in aJoint:
        IK_joints.append(aJoint)
        mc.setAttr(aJoint + '.radius', 1.5)
        
    if 'bind_' in aJoint:
        bind_joints.append(aJoint)
        mc.setAttr(aJoint + '.radius', .25)
        

        
#make a hierarchy of controls copying the fk joints, set the radius to 1, the color to 13(red), and then use make offsets for those controls
FK_cntrls = cntrlHierarchy(FK_joints, 1, 13, 'cntrl_grp')

#Makes a control for the IK wrist
IK_wristList = ['IK_wrist']
IK_cntrls = cntrlHierarchy(IK_wristList, 1.5, 24, 'cntrl_grp')

#Makes the IK handle
mc.ikHandle( n = 'arm_IK', sj = 'IK_shoulder', ee = 'IK_wrist', sol = 'ikRPsolver', pw = 1, w = 1 )
mc.parent( 'arm_IK', 'IK_grp')

#makes a blend between the fk and ik joints affecting the bind joints
blendThree(bind_joints, FK_joints, IK_joints, 'global_cntrl', 'FKIK')

#add constrains to the joints so that the controls move them
constrainLists(FK_cntrls, FK_joints, "yes", "yes", "none")
constrainLists(IK_cntrls, IK_wristList, "none", "yes", "none")
mc.pointConstraint(IK_cntrls, 'arm_IK', mo = False)

#add and connect the twist attribute
mc.addAttr('IK_wrist_cntrl', ln = 'twist', at = 'float', dv = 0, w = True, r = True, k = True)
mc.connectAttr('IK_wrist_cntrl.twist', 'arm_IK.twist')


