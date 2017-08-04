import maya.cmds as cmds
#Joint Dictionary
jntDict = {}
jntDict = {"leftArm" : [
["lf_shoulder_JNT", [9.58574, 118.83508, -0.70541]], 
["lf_elbow_JNT", [23.075005157215955, 101.68192524537305, -3.012311]], 
["lf_wrist_JNT", [37.7333821711548, 83.04211007076694, -0.7054100000000001]], 
["lf_wristEnd_JNT",[59.84439, 61.86297, 1.30086]]],
"rightArm" : [
["rt_shoulder_JNT", [-9.58574, 118.83508, -0.70541]], 
["rt_elbow_JNT", [-23.075005157215955, 101.68192524537305, -3.012311]], 
["rt_wrist_JNT", [-37.7333821711548, 83.04211007076694, -0.7054100000000001]], 
["rt_wristEnd_JNT",[-59.84439, 61.86297, 1.30086]]
]}
#IK Ctrl List
lf_IKctrlList = [[jntDict["leftArm"][2][1], "IK_lf_arm_CTRL", "IK_lf_arm_CTRL_GRP"]]
rt_IKctrlList = [[jntDict["rightArm"][2][1], "IK_rt_arm_CTRL", "IK_rt_arm_CTRL_GRP"]]

#FK Ctrl List
lf_FKctrlList = [
[jntDict["leftArm"][0][1], "FK_lf_shoulder_CTRL", "FK_lf_shoulder_CTRL_GRP"],
[jntDict["leftArm"][1][1], "FK_lf_elbow_CTRL", "FK_lf_elbow_CTRL_GRP"],
[jntDict["leftArm"][2][1], "FK_lf_wrist_CTRL", "FK_lf_wrist_CTRL_GRP"]]
rt_FKctrlList = [
[jntDict["rightArm"][0][1], "FK_rt_shoulder_CTRL", "FK_rt_shoulder_CTRL_GRP"],
[jntDict["rightArm"][1][1], "FK_rt_elbow_CTRL", "FK_rt_elbow_CTRL_GRP"],
[jntDict["rightArm"][2][1], "FK_rt_wrist_CTRL", "FK_rt_wrist_CTRL_GRP"]]

class Rig_Arm:
    def rig_arm(self):

    #Building joints___Function
    def create_arm_jnt(jntType):
        for jnt in jntDict:
            for joint in jntDict[jnt]:
                cmds.joint(n=jntType+joint[0],p=joint[1])
                cmds.select(d=True)
                
    #Orient Joints____Function
    def arm_orientJoint(orntJnt, aimJnt, aimVec, upVec):
         loc = cmds.spaceLocator()
         cmds.parent(loc[0], orntJnt)
         cmds.setAttr(loc[0]+".translate", 0, 0, 5, type = "double3")
         cmds.parent(loc[0], w=True)
         cmds.aimConstraint(aimJnt, orntJnt, offset = [0, 0, 0], weight = True, aimVector = aimVec ,
                                                 upVector = upVec, worldUpType = "object" , worldUpObject = loc[0])
         cmds.delete(orntJnt+"_aimConstraint1")
         cmds.makeIdentity(orntJnt, apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)
         cmds.delete(loc[0])
         cmds.parent(aimJnt, orntJnt)
         
    vecList = ([1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0])     

    #Cleaning up joint orinet___Function    
    def cleanJntOrient(jntType, side):
        for i in range(len(jntDict[side])):
            if jntDict[side][i][0] == jntDict[side][0][0]:
                pass
            elif jntDict[side][i][0] == jntDict[side][3][0]:
                cmds.setAttr(jntType + jntDict[side][i][0] +".jointOrient", 0, 0, 0, type = "double3")
            elif jntDict[side][i][0] == jntDict[side][2][0]:
                cmds.setAttr(jntType + jntDict[side][i][0] +'.jointOrientX', 0)    
            else:
                cmds.setAttr(jntType + jntDict[side][i][0] +".jointOrientX", 0)
                cmds.setAttr(jntType + jntDict[side][i][0] +".jointOrientY", 0)

    #Making Controls___Function
    def ctrlCircle(ctrlinfo, ctrlNormal):
        for info in range(len(ctrlinfo)):
            pos = ctrlinfo[info][0]
            ctrlGRP = cmds.group(em = True, name = ctrlinfo[info][2])
            if ctrlinfo[info][1] == ctrlinfo[0][1]:
                ctrl = cmds.circle(n=ctrlinfo[info][1], r = 6, nr= (40, 0, 0), c=(0, 0, 0))
            else:
                ctrl = cmds.circle(n=ctrlinfo[info][1], r = 4, nr= ctrlNormal, c=(0, 0, 0))
            cmds.parent(ctrl, ctrlGRP)
            cmds.xform(ctrlGRP, t=pos, ws = True)


 
#Building joints
create_arm_jnt("IK_")
create_arm_jnt("FK_")
create_arm_jnt("bn_")

#Orient Joints
arm_orientJoint("bn_lf_shoulder_JNT","bn_lf_elbow_JNT", vecList[0], vecList[2])
arm_orientJoint("bn_lf_elbow_JNT","bn_lf_wrist_JNT", vecList[0], vecList[2])
arm_orientJoint("bn_lf_wrist_JNT","bn_lf_wristEnd_JNT", vecList[0], vecList[2])
arm_orientJoint("IK_lf_shoulder_JNT","IK_lf_elbow_JNT", vecList[0], vecList[2])
arm_orientJoint("IK_lf_elbow_JNT","IK_lf_wrist_JNT", vecList[0], vecList[2])
arm_orientJoint("IK_lf_wrist_JNT","IK_lf_wristEnd_JNT", vecList[0], vecList[2])
arm_orientJoint("FK_lf_shoulder_JNT","FK_lf_elbow_JNT", vecList[0], vecList[2])
arm_orientJoint("FK_lf_elbow_JNT","FK_lf_wrist_JNT", vecList[0], vecList[2])
arm_orientJoint("FK_lf_wrist_JNT","FK_lf_wristEnd_JNT", vecList[0], vecList[2])

arm_orientJoint("bn_rt_shoulder_JNT","bn_rt_elbow_JNT", vecList[1], vecList[3])
arm_orientJoint("bn_rt_elbow_JNT","bn_rt_wrist_JNT", vecList[1], vecList[3])
arm_orientJoint("bn_rt_wrist_JNT","bn_rt_wristEnd_JNT", vecList[1], vecList[3])
arm_orientJoint("IK_rt_shoulder_JNT","IK_rt_elbow_JNT", vecList[1], vecList[3])
arm_orientJoint("IK_rt_elbow_JNT","IK_rt_wrist_JNT", vecList[1], vecList[3])
arm_orientJoint("IK_rt_wrist_JNT","IK_rt_wristEnd_JNT", vecList[1], vecList[3])
arm_orientJoint("FK_rt_shoulder_JNT","FK_rt_elbow_JNT", vecList[1], vecList[3])
arm_orientJoint("FK_rt_elbow_JNT","FK_rt_wrist_JNT", vecList[1], vecList[3])
arm_orientJoint("FK_rt_wrist_JNT","FK_rt_wristEnd_JNT", vecList[1], vecList[3])

#Cleaning Joint Orient 
cleanJntOrient("IK_", "leftArm")
cleanJntOrient("FK_", "leftArm")
cleanJntOrient("bn_", "leftArm")

cleanJntOrient("IK_", "rightArm")
cleanJntOrient("FK_", "rightArm")
cleanJntOrient("bn_", "rightArm")

#Making IK Handle 
lf_IKH = cmds.ikHandle( n = "rIK_lf_arm_Hndl" , sj = "IK_" + jntDict["leftArm"][0][0], ee = "IK_" + jntDict["leftArm"][2][0])
lf_IKE = cmds.rename(lf_IKH[1], "rIK_lf_arm_Eff")
rt_IKH = cmds.ikHandle( n = "rIK_rt_arm_Hndl" , sj = "IK_" + jntDict["rightArm"][0][0], ee = "IK_" + jntDict["rightArm"][2][0])
rt_IKE = cmds.rename(rt_IKH[1], "rIK_rt_arm_Eff")

#Orienting IK Handle
cmds.parent(lf_IKH[0], "bn_"+jntDict["leftArm"][2][0])
cmds.parent(rt_IKH[0], "bn_"+jntDict["rightArm"][2][0])
cmds.makeIdentity(lf_IKH[0], apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)
cmds.makeIdentity(rt_IKH[0], apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)
cmds.parent(lf_IKH[0], w = True)
cmds.parent(rt_IKH[0], w = True)

ctrlCircle(lf_IKctrlList, (40, -50, 0))
ctrlCircle(rt_IKctrlList, (40, 50, 0))