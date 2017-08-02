import maya.cmds as cmds
#List of leg joints
LfLegJntList = [["lf_thigh_JNT", [7.3841949715898885, 80, 1.4933439236321089]], 
["lf_knee_JNT", [7.913337468606758, 45.00400011118629, 1.4933439236321089]], 
["lf_ankle_JNT", [8.48125965974247, 7.443220075773034, -2.254893934189369]], 
["lf_ball_JNT", [9.73326931846742, 1.3015547126171416, 9.629198761937829]],
["lf_toeEnd_JNT", [11.086394550152109, 1.3015547126171443, 22.300869551214134]]]

RtLegJntList = [["rt_thigh_JNT", [-7.3841949715898885, 80, 1.4933439236321089]], 
["rt_knee_JNT", [-7.913337468606758, 45.00400011118629, 1.4933439236321089]], 
["rt_ankle_JNT", [-8.48125965974247, 7.443220075773034, -2.254893934189369]], 
["rt_ball_JNT", [-9.73326931846742, 1.3015547126171416, 9.629198761937829]],
["rt_toeEnd_JNT", [-11.086394550152109, 1.3015547126171443, 22.300869551214134]]]
#Making joints 
def create_leg_jnt(side):
    for i in range(len(RtLegJntList)):
        cmds.joint(n=side+RtLegJntList[i][0],p=RtLegJntList[i][1])
        cmds.select(d=True)
    
    for i in range(len(LfLegJntList)):
        cmds.joint(n=side+LfLegJntList[i][0],p=LfLegJntList[i][1])
        cmds.select(d=True)
create_leg_jnt('IK_')
create_leg_jnt('FK_')
create_leg_jnt('bn_')

#Orienting joints
def lf_leg_orientJoint(lf_orntJnt, lf_aimJnt):
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

def rt_leg_orientJoint(rt_orntJnt, rt_aimJnt):
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

def lf_ankle_orient(lf_orntJnt, lf_parentJnt):
	cmds.setAttr(lf_orntJnt+".jointOrient", 90, 0, -90, type="double3")
	cmds.parent(lf_parentJnt, lf_orntJnt)

def rt_ankle_orient(rt_orntJnt, rt_parentJnt):
	cmds.setAttr(rt_orntJnt+".jointOrient", -90, 0, 90, type="double3")
	cmds.parent(rt_parentJnt, rt_orntJnt)

lf_leg_orientJoint("bn_lf_thigh_JNT","bn_lf_knee_JNT")
lf_leg_orientJoint("bn_lf_knee_JNT","bn_lf_ankle_JNT")
lf_ankle_orient("bn_lf_ankle_JNT","bn_lf_ball_JNT")
lf_leg_orientJoint("bn_lf_ball_JNT","bn_lf_toeEnd_JNT")

lf_leg_orientJoint("IK_lf_thigh_JNT","IK_lf_knee_JNT")
lf_leg_orientJoint("IK_lf_knee_JNT","IK_lf_ankle_JNT")
lf_ankle_orient("IK_lf_ankle_JNT","IK_lf_ball_JNT")
lf_leg_orientJoint("IK_lf_ball_JNT","IK_lf_toeEnd_JNT")

lf_leg_orientJoint("FK_lf_thigh_JNT","FK_lf_knee_JNT")
lf_leg_orientJoint("FK_lf_knee_JNT","FK_lf_ankle_JNT")
lf_ankle_orient("FK_lf_ankle_JNT","FK_lf_ball_JNT")
lf_leg_orientJoint("FK_lf_ball_JNT","FK_lf_toeEnd_JNT")

rt_leg_orientJoint("bn_rt_thigh_JNT","bn_rt_knee_JNT")
rt_leg_orientJoint("bn_rt_knee_JNT","bn_rt_ankle_JNT")
rt_ankle_orient("bn_rt_ankle_JNT","bn_rt_ball_JNT")
rt_leg_orientJoint("bn_rt_ball_JNT","bn_rt_toeEnd_JNT")

rt_leg_orientJoint("IK_rt_thigh_JNT","IK_rt_knee_JNT")
rt_leg_orientJoint("IK_rt_knee_JNT","IK_rt_ankle_JNT")
rt_ankle_orient("IK_rt_ankle_JNT","IK_rt_ball_JNT")
rt_leg_orientJoint("IK_rt_ball_JNT","IK_rt_toeEnd_JNT")

rt_leg_orientJoint("FK_rt_thigh_JNT","FK_rt_knee_JNT")
rt_leg_orientJoint("FK_rt_knee_JNT","FK_rt_ankle_JNT")
rt_ankle_orient("FK_rt_ankle_JNT","FK_rt_ball_JNT")
rt_leg_orientJoint("FK_rt_ball_JNT","FK_rt_toeEnd_JNT")
