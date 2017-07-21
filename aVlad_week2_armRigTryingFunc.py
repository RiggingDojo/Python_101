import maya.cmds as cmds
#Making Joints
LfBindJntList = [["lf_shoulder_JNT", [9.58574, 118.83508, -0.70541]], 
["lf_elbow_JNT", [23.075005157215955, 101.68192524537305, -3.012311]], 
["lf_wrist_JNT", [37.7333821711548, 83.04211007076694, -0.7054100000000001]], 
["lf_wristEnd_JNT",[59.84439, 61.86297, 1.30086]]]

RtBindJntList = [["rt_shoulder_JNT", [-9.58574, 118.83508, -0.70541]], 
["rt_elbow_JNT", [-23.075005157215955, 101.68192524537305, -3.012311]], 
["rt_wrist_JNT", [-37.7333821711548, 83.04211007076694, -0.7054100000000001]], 
["rt_wristEnd_JNT",[-59.84439, 61.86297, 1.30086]]]

def create_jnt(side):
    for i in range(len(RtBindJntList)):
        cmds.joint(n=side+RtBindJntList[i][0],p=RtBindJntList[i][1])
        cmds.select(d=True)
    
    for i in range(len(LfBindJntList)):
        cmds.joint(n=side+LfBindJntList[i][0],p=LfBindJntList[i][1])
        cmds.select(d=True)
create_jnt('IK_')
create_jnt('FK_')
create_jnt('bn_')

########################################################################################################################

#Orienting joints
def lf_orientJoint(lf_orntJnt, lf_aimJnt):
     cmds.spaceLocator()
     cmds.parent("locator1", lf_orntJnt)
     cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
     cmds.parent("locator1", w=True)
     cmds.aimConstraint(lf_aimJnt, lf_orntJnt, offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
     cmds.delete(lf_orntJnt+"_aimConstraint1")
     cmds.makeIdentity(lf_orntJnt, apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)
     cmds.delete("locator1")
     cmds.parent(lf_aimJnt, lf_orntJnt)

def rt_orientJoint(rt_orntJnt, rt_aimJnt):
     cmds.spaceLocator()
     cmds.parent("locator1", rt_orntJnt)
     cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
     cmds.parent("locator1", w=True)
     cmds.aimConstraint(rt_aimJnt, rt_orntJnt, offset = [0, 0, 0], weight = True, aimVector = [-1, 0, 0] , 
                                             upVector = [0, -1, 0], worldUpType = "object" , worldUpObject = "locator1")
     cmds.delete(rt_orntJnt+"_aimConstraint1")
     cmds.makeIdentity(rt_orntJnt, apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)
     cmds.delete("locator1")
     cmds.parent(rt_aimJnt, rt_orntJnt)


lf_orientJoint("bn_lf_shoulder_JNT","bn_lf_elbow_JNT")
lf_orientJoint("bn_lf_elbow_JNT","bn_lf_wrist_JNT")
lf_orientJoint("bn_lf_wrist_JNT","bn_lf_wristEnd_JNT")

lf_orientJoint("IK_lf_shoulder_JNT","IK_lf_elbow_JNT")
lf_orientJoint("IK_lf_elbow_JNT","IK_lf_wrist_JNT")
lf_orientJoint("IK_lf_wrist_JNT","IK_lf_wristEnd_JNT")

lf_orientJoint("FK_lf_shoulder_JNT","FK_lf_elbow_JNT")
lf_orientJoint("FK_lf_elbow_JNT","FK_lf_wrist_JNT")
lf_orientJoint("FK_lf_wrist_JNT","FK_lf_wristEnd_JNT")

rt_orientJoint("bn_rt_shoulder_JNT","bn_rt_elbow_JNT")
rt_orientJoint("bn_rt_elbow_JNT","bn_rt_wrist_JNT")
rt_orientJoint("bn_rt_wrist_JNT","bn_rt_wristEnd_JNT")

rt_orientJoint("IK_rt_shoulder_JNT","IK_rt_elbow_JNT")
rt_orientJoint("IK_rt_elbow_JNT","IK_rt_wrist_JNT")
rt_orientJoint("IK_rt_wrist_JNT","IK_rt_wristEnd_JNT")

rt_orientJoint("FK_rt_shoulder_JNT","FK_rt_elbow_JNT")
rt_orientJoint("FK_rt_elbow_JNT","FK_rt_wrist_JNT")
rt_orientJoint("FK_rt_wrist_JNT","FK_rt_wristEnd_JNT")

########################################################################################################################



#Making sure that bind arm is straight for IK to work properly 
cmds.setAttr("bn_lf_elbow_JNT.jointOrientX", 0)
cmds.setAttr("bn_lf_elbow_JNT.jointOrientY", 0)

#A little bit not sure about next one
"""This one can look weird, but I am using actual model to build an arm and my model hand oriented a little bit off , so I will leave untouched 
Y and Z so wrist will be oriented to the hand , I am newbie rigger also so if I am doing something wrong please tell me :)"""
cmds.setAttr("bn_lf_wrist_JNT.jointOrientX", 0)

########################################################################################################################


#Making sure that IK arm is straight for IK to work properly 
cmds.setAttr("IK_lf_elbow_JNT.jointOrientX", 0)
cmds.setAttr("IK_lf_elbow_JNT.jointOrientY", 0)
cmds.setAttr("IK_lf_wrist_JNT.jointOrientX", 0)

########################################################################################################################


#Making sure that FK arm is straight for IK to work properly 
cmds.setAttr("FK_lf_elbow_JNT.jointOrientX", 0)
cmds.setAttr("FK_lf_elbow_JNT.jointOrientY", 0)
cmds.setAttr("FK_lf_wrist_JNT.jointOrientX", 0)

########################################################################################################################
#Make Right Side
########################################################################################################################

########################################################################################################################


#Making sure that bind arm is straight for IK to work properly 
cmds.setAttr("bn_rt_elbow_JNT.jointOrientX", 0)
cmds.setAttr("bn_rt_elbow_JNT.jointOrientY", 0)

#A little bit not sure about next one
"""This one can look weird, but I am using actual model to build an arm and my model hand oriented a little bit off , so I will leave untouched 
Y and Z so wrist will be oriented to the hand , I am newbie rigger also so if I am doing something wrong please tell me :)"""
cmds.setAttr("bn_rt_wrist_JNT.jointOrientX", 0)

########################################################################################################################

#Making sure that IK arm is straight for IK to work properly 
cmds.setAttr("IK_rt_elbow_JNT.jointOrientX", 0)
cmds.setAttr("IK_rt_elbow_JNT.jointOrientY", 0)
cmds.setAttr("IK_rt_wrist_JNT.jointOrientX", 0)

########################################################################################################################

#Making sure that FK arm is straight for IK to work properly 
cmds.setAttr("FK_rt_elbow_JNT.jointOrientX", 0)
cmds.setAttr("FK_rt_elbow_JNT.jointOrientY", 0)
cmds.setAttr("FK_rt_wrist_JNT.jointOrientX", 0)

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

