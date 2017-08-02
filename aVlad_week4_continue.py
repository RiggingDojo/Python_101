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
#Building joints___Function
def create_arm_jnt(jntType):
    for i in jntDict:
        for joint in jntDict[i]:
            cmds.joint(n=jntType+joint[0],p=joint[1])
            cmds.select(d=True)
            
#Orient Joints____Function
def arm_orientJoint(orntJnt, aimJnt, aimVec, upVec):
     cmds.spaceLocator()
     cmds.parent("locator1", orntJnt)
     cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
     cmds.parent("locator1", w=True)
     cmds.aimConstraint(aimJnt, orntJnt, offset = [0, 0, 0], weight = True, aimVector = aimVec ,
                                             upVector = upVec, worldUpType = "object" , worldUpObject = "locator1")
     cmds.delete(orntJnt+"_aimConstraint1")
     cmds.makeIdentity(orntJnt, apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)
     cmds.delete("locator1")
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
########################################################################################################################



#IK Handle making and control for (Right and Left Side)
cmds.ikHandle( n = "rIK_lf_arm_Hndl" , sj = "IK_lf_shoulder_JNT", ee = "IK_lf_wrist_JNT")
cmds.rename("effector1", "rIK_lf_arm_Eff")
cmds.ikHandle( n = "rIK_rt_arm_Hndl" , sj = "IK_rt_shoulder_JNT", ee = "IK_rt_wrist_JNT")
cmds.rename("effector1", "rIK_rt_arm_Eff")
cmds.parent("rIK_lf_arm_Hndl", "bn_lf_wrist_JNT" )
cmds.parent("rIK_rt_arm_Hndl", "bn_rt_wrist_JNT" )
cmds.makeIdentity("rIK_lf_arm_Hndl", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)
cmds.makeIdentity("rIK_rt_arm_Hndl", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)
cmds.parent("rIK_lf_arm_Hndl", w = True)
cmds.parent("rIK_rt_arm_Hndl", w = True)

