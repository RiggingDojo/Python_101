import maya.cmds as cmds
import json
import tempfile
import os

def writeJson(fileName, data):
    with open(fileName, 'w') as outfile:
        json.dump(data, outfile)
    file.close(outfile)

def readJson(fileName):
    with open(fileName, 'r') as infile:
        data = (open(infile.name, 'r').read())
    return data


def createJoint(name, position, instance):
    # Use a list comprehension to build joints.
    jnt_list = [cmds.joint(n=name[i].replace('_s_', instance), p=position[i]) for i in range(len(name))]
    cmds.select(d=True)
    return(jnt_list)


def createControl(ctrlinfo):
    control_info = []
    for info in ctrlinfo:
        print
        # Create ik control
        # Get ws position of the joint
        pos = info[0]
        # Create circle control object
        ctrl_file = os.environ["RDOJO_DATA"]+ 'controls/' + info[2]
         # Import a control object
        cmds.file(ctrl_file, i=True)
        ctrl = info[1]
        ctrlgrp = 'grp_' + info[1]
        if cmds.objExists('grp_control') == True:
            cmds.rename('grp_control', ctrlgrp )
            cmds.rename('control', ctrl)
        # Move the group to the joint
        cmds.xform(ctrlgrp, t=pos, ws=True)
        control_info.append([ctrlgrp, ctrl])
    return(control_info)


def calculatePVPosition(jnts):
    from maya import cmds , OpenMaya
    start = cmds.xform(jnts[0] ,q=True ,ws=True, t=True)
    mid = cmds.xform(jnts[1] ,q=True ,ws=True, t=True)
    end = cmds.xform(jnts[2] ,q=True ,ws=True, t=True)
    startV = OpenMaya.MVector(start[0] ,start[1],start[2])
    midV = OpenMaya.MVector(mid[0] ,mid[1],mid[2])
    endV = OpenMaya.MVector(end[0] ,end[1],end[2])
    startEnd = endV - startV
    startMid = midV - startV
    dotP = startMid * startEnd
    proj = float(dotP) / float(startEnd.length())
    startEndN = startEnd.normal()
    projV = startEndN * proj
    arrowV = startMid - projV
    arrowV*= 0.5
    finalV = arrowV + midV
    return ([finalV.x , finalV.y ,finalV.z])

def connectThroughBC(parentsA, parentsB, children, instance, switchattr ):
    constraints = []
    for j in range(len(children)):
        switchPrefix = children[j].partition('_')[2]
        bcNodeT = cmds.shadingNode("blendColors", asUtility=True, n='bcNodeT_switch_' + switchPrefix)
        cmds.connectAttr(switchattr, bcNodeT  + '.blender')
        bcNodeR = cmds.shadingNode("blendColors", asUtility=True, n='bcNodeR_switch_' + switchPrefix)
        cmds.connectAttr(switchattr, bcNodeR  + '.blender')
        bcNodeS = cmds.shadingNode("blendColors", asUtility=True, n='bcNodeS_switch_' + switchPrefix)
        cmds.connectAttr(switchattr, bcNodeS  + '.blender')
        constraints.append([bcNodeT, bcNodeR, bcNodeS])
        # Input Parents
        cmds.connectAttr(parentsA[j] + '.translate', bcNodeT + '.color1')        
        cmds.connectAttr(parentsA[j] + '.rotate', bcNodeR + '.color1')       
        cmds.connectAttr(parentsA[j] + '.scale', bcNodeS + '.color1')
        if parentsB != 'None':
            cmds.connectAttr(parentsB[j] + '.translate', bcNodeT + '.color2')
            cmds.connectAttr(parentsB[j] + '.rotate', bcNodeR + '.color2')
            cmds.connectAttr(parentsB[j] + '.scale', bcNodeS + '.color2')
        # Output to Children
        cmds.connectAttr(bcNodeT + '.output', children[j] + '.translate')
        cmds.connectAttr(bcNodeR + '.output', children[j] + '.rotate')
        cmds.connectAttr(bcNodeS + '.output', children[j] + '.scale')
    return constraints

def match_ikfk(*args):
    print "Match"
    initializesj = cmds.scriptJob(runOnce=False, kws=False, e=["SelectionChanged", checkForSwitch])

def checkForSwitch(*args):
    print "Check"
    sel = cmds.ls(sl=True)[0]
    print sel
    print cmds.listAttrs(sel, k=True)
    if ".IK_FK" in cmds.listAttrs(cmds.ls(sl=True)[0], k=True):
        print "Has Switch"

def setupMatchScripts(*args):
    # Look for controls with IK_FK attributes and set scriptJobs on them.
    print "Setup Match"
