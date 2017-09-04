import maya.cmds as cmds
rigData={}
rigData["ArmJoints"]=[
                      ["lf_shoulder_JNT", "lf_elbow_JNT", "lf_wrist_JNT"],
                      ["rt_shoulder_JNT", "rt_elbow_JNT", "rt_wrist_JNT"]
                      ]
rigData["IK_ArmList"] = [
                         ["IK_lf_arm_CTRL", "IK_lf_arm_CTRL_srt", "rIK_lf_arm_Hndl", "rIK_lf_arm_Eff", "IK_lf_armPV_CTRL", "IK_lf_armPV_CTRL_srt"], 
                         ["IK_rt_arm_CTRL", "IK_rt_arm_CTRL_srt", "rIK_rt_arm_Hndl", "rIK_rt_arm_Eff", "IK_rt_armPV_CTRL", "IK_rt_armPV_CTRL_srt"]
                        ]
rigData["JointsPos"]=[
                     [[9.58574, 118.83508, -0.70541], [23.075005157215955, 101.68192524537305, -3.012311], [37.7333821711548, 83.04211007076694, -0.7054100000000001]],
                     [[-9.58574, 118.83508, -0.70541], [-23.075005157215955, 101.68192524537305, -3.012311], [-37.7333821711548, 83.04211007076694, -0.7054100000000001]]
                     ]
rigData["FK_ArmList"] = [
                         ["FK_lf_shoulder_CTRL", "FK_lf_shoulder_CTRL_srt", "FK_lf_elbow_CTRL", "FK_lf_elbow_CTRL_srt", "FK_lf_wrist_CTRL", "FK_lf_wrist_CTRL_srt"], 
                         ["FK_rt_shoulder_CTRL", "FK_rt_shoulder_CTRL_srt", "FK_rt_elbow_CTRL", "FK_rt_elbow_CTRL_srt", "FK_rt_wrist_CTRL", "FK_rt_wrist_CTRL_srt"]
                         ]   
                    
rigData["HierarchyOrg"] = ["singer", "singer_GEO_hrc", "GlobalMove_srt", "JNT_hrc", "skeleton_hrc", "extra_JNT_hrc", "ControlObjects_hrc", "ExtraNode_hrc",
                            "toHide_hrc", "toShow_hrc", "IKh_hrc", "World_CTRL_srt", "World_CTRL", "Local_CTRL_srt", "Local_CTRL", "IK_lf_Stretch_arm_hrc", "IK_rt_Stretch_arm_hrc" ]
rigData["StretchyIK"] = [
                              ["scaleComp_lf_uparm_dist_multDiv", "scaleComp_lf_lowarm_dist_multDiv", "stretch_lf_arm_multDiv", 
                              "scaleComp_lf_arm_dist_mdl", "stretch_lf_uparm_mdl", "stretch_lf_lowarm_mdl",
                              "scaleComp_lf_uparm_dist_cond", "scaleComp_lf_lowarm_dist_cond", "stretch_lf_uparm_cond", "stretch_lf_lowarm_cond",
                              "stretch_lf_uparm_elbowPin_blendAttr","stretch_lf_lowarm_elbowPin_blendAttr",
                              "stretch_lf_uparm_enable_blend", "stretch_lf_lowarm_enable_blend",
                              "scaleComp_lf_uparm_dist_Inverse_mdl", "scaleComp_lf_lowarm_dist_Inverse_mdl",
                              "lf_arm_distD", "lf_uparm_distD", "lf_lowarm_distD", "lf_shoulder_distLoc", "lf_elbow_distLoc", "lf_wrist_distLoc", "lf_wrist_distLoc"],
                              ["scaleComp_rt_uparm_dist_multDiv", "scaleComp_rt_lowarm_dist_multDiv", "stretch_rt_arm_multDiv", 
                              "scaleComp_rt_arm_dist_mdl", "stretch_rt_uparm_mdl", "stretch_rt_lowarm_mdl",
                              "scaleComp_rt_uparm_dist_cond", "scaleComp_rt_lowarm_dist_cond", "stretch_rt_uparm_cond", "stretch_rt_lowarm_cond",
                              "stretch_rt_uparm_elbowPin_blendAttr","stretch_rt_lowarm_elbowPin_blendAttr",
                              "stretch_rt_uparm_enable_blend", "stretch_rt_lowarm_enable_blend",
                              "scaleComp_rt_uparm_dist_Inverse_mdl", "scaleComp_rt_lowarm_dist_Inverse_mdl",
                              "rt_arm_distD", "rt_uparm_distD", "rt_lowarm_distD", "rt_shoulder_distLoc", "rt_elbow_distLoc", "rt_wrist_distLoc", "rt_wrist_distLoc"]
                               ]
rigData["IaF_Switch"] = [
                         ["IaF_lf_shoulder_pairB", "IaF_lf_elbow_pairB", "IaF_lf_wrist_pairB", "IaF_lf_arm_switch_CTRL", "IaF_lf_arm_switch_CTRL_srt"],
                         ["IaF_rt_shoulder_pairB", "IaF_rt_elbow_pairB", "IaF_rt_wrist_pairB", "IaF_rt_arm_switch_CTRL", "IaF_rt_arm_switch_CTRL_srt"]
                          ]
def HrcSetup():
     cmds.group(em = True, name = rigData["HierarchyOrg"][0])
     cmds.group(em = True, p = rigData["HierarchyOrg"][0], name = rigData["HierarchyOrg"][1])
     cmds.group(em = True, p = rigData["HierarchyOrg"][0], name = rigData["HierarchyOrg"][2])
     cmds.group(em = True, p = rigData["HierarchyOrg"][2], name = rigData["HierarchyOrg"][3])
     cmds.group(em = True, p = rigData["HierarchyOrg"][3], name = "bn_"+rigData["HierarchyOrg"][4])
     cmds.group(em = True, p = rigData["HierarchyOrg"][3], name = "IK_"+rigData["HierarchyOrg"][4])
     cmds.group(em = True, p = rigData["HierarchyOrg"][3], name = "FK_"+rigData["HierarchyOrg"][4])
     cmds.group(em = True, p = rigData["HierarchyOrg"][3], name = rigData["HierarchyOrg"][5])
     cmds.group(em = True, p = rigData["HierarchyOrg"][2], name = rigData["HierarchyOrg"][6])
     cmds.group(em = True, p = rigData["HierarchyOrg"][0], name = rigData["HierarchyOrg"][7])
     cmds.group(em = True, p = rigData["HierarchyOrg"][7], name = rigData["HierarchyOrg"][8])
     cmds.group(em = True, p = rigData["HierarchyOrg"][7], name = rigData["HierarchyOrg"][9])
     cmds.group(em = True, p = rigData["HierarchyOrg"][3], name = rigData["HierarchyOrg"][10])
     cmds.setAttr(rigData["HierarchyOrg"][8]+".v", 0) 
def createArmJnt(jntType):
    for i in range(len(rigData["ArmJoints"])):
            for o in range(len(rigData["ArmJoints"][i])):
                cmds.joint(n=jntType+rigData["ArmJoints"][i][o], p=rigData["JointsPos"][i][o])
                cmds.select(cl=True)

def arm_orientJoint(jntType, orntJnt, aimJnt, aimVec, upVec):
    loc = cmds.spaceLocator()
    cmds.parent(loc[0], jntType+orntJnt)
    cmds.setAttr(loc[0]+".translate", 0, 0, 5, type = "double3")
    cmds.parent(loc[0], w=True)
    cmds.aimConstraint(jntType+aimJnt, jntType+orntJnt, offset = [0, 0, 0], weight = True, aimVector = aimVec ,
                                                 upVector = upVec, worldUpType = "object" , worldUpObject = loc[0])
    cmds.delete(jntType+orntJnt+"_aimConstraint1")
    cmds.makeIdentity(jntType+orntJnt, apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)
    cmds.delete(loc[0])
  
    
    #Cleaning up joint orinet___Function    
def cleanJntOrientArm(jntType):
    for i in range(len(rigData["ArmJoints"])):
        
        cmds.parent(jntType+rigData["ArmJoints"][i][0], jntType+rigData["HierarchyOrg"][4])
        
        cmds.parent(jntType+rigData["ArmJoints"][i][1], jntType+rigData["ArmJoints"][i][0])
        cmds.setAttr(jntType+rigData["ArmJoints"][i][1]+".jointOrientX", 0)
        cmds.setAttr(jntType+rigData["ArmJoints"][i][1]+".jointOrientY", 0)
        cmds.setAttr(jntType+rigData["ArmJoints"][i][1]+".ty", 0)
        cmds.setAttr(jntType+rigData["ArmJoints"][i][1]+".tz", 0)

        
        cmds.parent(jntType+rigData["ArmJoints"][i][2], jntType+rigData["ArmJoints"][i][1])
        cmds.setAttr(jntType+rigData["ArmJoints"][i][2]+".jointOrient", 0, 0, 0, type = "double3")
        cmds.setAttr(jntType+rigData["ArmJoints"][i][2]+".ty", 0)
        cmds.setAttr(jntType+rigData["ArmJoints"][i][2]+".tz", 0)   
                
def IK_Create():
    for i in range(len(rigData["IK_ArmList"])):      
        IKH = cmds.ikHandle( n = rigData["IK_ArmList"][i][2] , sj = "IK_"+rigData["ArmJoints"][i][0], ee = "IK_" + rigData["ArmJoints"][i][2])
        IKE = cmds.rename(IKH[1], rigData["IK_ArmList"][i][3])
        #Orienting IK Handle
        cmds.parent(IKH[0], "bn_"+rigData["ArmJoints"][i][2])
        cmds.makeIdentity(IKH[0], apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)
        cmds.parent(IKH[0], rigData["HierarchyOrg"][10])
    
                  
                
def IK_CtrlMaker():
    for i in range(len(rigData["JointsPos"])):
        pos = rigData["JointsPos"][i][2]
        ctrlGRP = cmds.group(em = True, name = rigData["IK_ArmList"][i][1])
        if rigData["IK_ArmList"][i][0] == rigData["IK_ArmList"][0][0]:
            ctrl = cmds.circle(n=rigData["IK_ArmList"][i][0], r = 6, nr= (40, -50, 0), c=(0, 0, 0), ch=False)
        else:
            ctrl = cmds.circle(n=rigData["IK_ArmList"][i][0], r = 6, nr= (40, 50, 0), c=(0, 0, 0), ch=False)
        cmds.parent(ctrl, ctrlGRP)
        cmds.xform(ctrlGRP, t=pos, ws = True)
        cmds.parent(ctrlGRP, rigData["IK_ArmList"][i][2])
        cmds.makeIdentity(ctrlGRP, apply = True, t = 0, r = 1, s = 0, n = 0, pn = True)
        cmds.parent(ctrlGRP, rigData["HierarchyOrg"][6])
        cmds.pointConstraint(rigData["IK_ArmList"][i][0], rigData["IK_ArmList"][i][2])
        cmds.setAttr(rigData["IK_ArmList"][i][0]+".sx", l = True, k = False, cb = False) 
        cmds.setAttr(rigData["IK_ArmList"][i][0]+".sy", l = True, k = False, cb = False) 
        cmds.setAttr(rigData["IK_ArmList"][i][0]+".sz", l = True, k = False, cb = False) 
        cmds.setAttr(rigData["IK_ArmList"][i][0]+".rx", l = True, k = False, cb = False) 
        cmds.setAttr(rigData["IK_ArmList"][i][0]+".ry", l = True, k = False, cb = False) 
        cmds.setAttr(rigData["IK_ArmList"][i][0]+".rz", l = True, k = False, cb = False)
        cmds.addAttr(rigData["IK_ArmList"][i][0], ln = "__________", at = "enum", en = "ExtraCTRL", k = True)
        cmds.addAttr(rigData["IK_ArmList"][i][0], shortName="Stretch", longName="Stretch", defaultValue=0.0, minValue=0.0, maxValue=1, k = True )
        shape = cmds.listRelatives(rigData["IK_ArmList"][i][0], children = True)   
        cmds.setAttr(shape[0]+".overrideEnabled", 1)  
        if i == 0:
            cmds.setAttr(shape[0]+".overrideColor", 14)
        else:
            cmds.setAttr(shape[0]+".overrideColor", 13)

        
def FK_CtrlMaker():     
    for o in range(len(rigData["JointsPos"])):
        for s in range(len(rigData["JointsPos"][o])):
            pos = rigData["JointsPos"][o][s]
            ctrlGRP = cmds.group(em = True, name = rigData["FK_ArmList"][o][1::2][s])
            cmds.parent(rigData["FK_ArmList"][o][0::2][s], ctrlGRP)
            cmds.xform(ctrlGRP, t=pos, ws = True)
            cmds.parent(ctrlGRP, "FK_"+rigData["ArmJoints"][o][s])   
            cmds.makeIdentity(ctrlGRP, apply=True, t=0, r=1, s=0, n=0, pn=True)
            if s!=0:
                cmds.parent(ctrlGRP, rigData["FK_ArmList"][o][0::2][s-1])
            else:
                cmds.parent(ctrlGRP, rigData["HierarchyOrg"][6])
            cmds.orientConstraint(rigData["FK_ArmList"][o][0::2][s], "FK_"+rigData["ArmJoints"][o][s])
            
def PV_CtrlMaker(lf_position, rt_position):
    for i in range(len(rigData["IK_ArmList"])):
        if i==0:
            pos = lf_position
        else:
            pos = rt_position
        ctrlGRP = cmds.group(em = True, name = rigData["IK_ArmList"][i][5])
       
        cmds.parent(rigData["IK_ArmList"][i][4], ctrlGRP)
        cmds.xform(ctrlGRP, t=pos, ws=True)
        cmds.parent(ctrlGRP, rigData["HierarchyOrg"][6])
        wPos = cmds.getAttr(rigData["IK_ArmList"][i][5]+".tz")
        cmds.setAttr(rigData["IK_ArmList"][i][5]+".tz", wPos-20)
        cmds.poleVectorConstraint(rigData["IK_ArmList"][i][4], rigData["IK_ArmList"][i][2])
        cmds.setAttr(rigData["IK_ArmList"][i][4]+".sx", l = True, k = False, cb = False)  
        cmds.setAttr(rigData["IK_ArmList"][i][4]+".sy", l = True, k = False, cb = False) 
        cmds.setAttr(rigData["IK_ArmList"][i][4]+".sz", l = True, k = False, cb = False) 
        cmds.setAttr(rigData["IK_ArmList"][i][4]+".rx", l = True, k = False, cb = False)
        cmds.setAttr(rigData["IK_ArmList"][i][4]+".ry", l = True, k = False, cb = False) 
        cmds.setAttr(rigData["IK_ArmList"][i][4]+".rz", l = True, k = False, cb = False)
        cmds.addAttr(rigData["IK_ArmList"][i][4], ln = "__________", at = "enum", en = "ExtraCTRL", k = True)
        cmds.addAttr(rigData["IK_ArmList"][i][4], shortName="ElbowPin", longName="ElbowPin", defaultValue=0.0, minValue=0.0, maxValue=1, k=True )  



def IaF_Switch_CtrlMaker():
  for i in range(len(rigData["IaF_Switch"])):
    pos = rigData["JointsPos"][i][2]
    ctrlGRP = cmds.group(em=True, name = rigData["IaF_Switch"][i][4])
    cmds.parent(rigData["IaF_Switch"][i][3], ctrlGRP)
    cmds.xform(ctrlGRP, t=pos, ws=True)
    cmds.parent(ctrlGRP, rigData["HierarchyOrg"][6])






def calculatePVPosition(jnts):
    from maya import cmds, OpenMaya
    start = cmds.xform(jnts[0], q= True, ws = True, t = True)
    mid = cmds.xform(jnts[1], q=True, ws=True, t = True)
    end = cmds.xform(jnts[2], q=True, ws=True, t= True)
    startV = OpenMaya.MVector(start[0], start[1], start[2])
    midV = OpenMaya.MVector(mid[0], mid[1], mid[2])
    endV = OpenMaya.MVector(end[0], end[1], end[2])
    startEnd = endV - startV
    startMid = midV - startV
    dotP = startMid * startEnd
    proj = float(dotP) / float(startEnd.length())
    startEndN = startEnd.normal()
    projV = startEndN * proj
    arrowV = startMid - projV
    arrowV*= 0.5
    finalV = arrowV + midV
    return ([finalV.x, finalV.y, finalV.z])               

def FK_CtrlShape():
        for i in range(len(rigData["FK_ArmList"])):
            for o in range(len(rigData["FK_ArmList"][i][0::2])):            
                crv = cmds.curve( degree = 1,\
                                knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\
                                        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,\
                                        39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],\
                                point = [(0, 1, 0),\
                                         (0, 0.92388000000000003, 0.382683),\
                                         (0, 0.70710700000000004, 0.70710700000000004),\
                                         (0, 0.382683, 0.92388000000000003),\
                                         (0, 0, 1),\
                                         (0, -0.382683, 0.92388000000000003),\
                                         (0, -0.70710700000000004, 0.70710700000000004),\
                                         (0, -0.92388000000000003, 0.382683),\
                                         (0, -1, 0),\
                                         (0, -0.92388000000000003, -0.382683),\
                                         (0, -0.70710700000000004, -0.70710700000000004),\
                                         (0, -0.382683, -0.92388000000000003),\
                                         (0, 0, -1),\
                                         (0, 0.382683, -0.92388000000000003),\
                                         (0, 0.70710700000000004, -0.70710700000000004),\
                                         (0, 0.92388000000000003, -0.382683),\
                                         (0, 1, 0),\
                                         (0.382683, 0.92388000000000003, 0),\
                                         (0.70710700000000004, 0.70710700000000004, 0),\
                                         (0.92388000000000003, 0.382683, 0),\
                                         (1, 0, 0),\
                                         (0.92388000000000003, -0.382683, 0),\
                                         (0.70710700000000004, -0.70710700000000004, 0),\
                                         (0.382683, -0.92388000000000003, 0),\
                                         (0, -1, 0),\
                                         (-0.382683, -0.92388000000000003, 0),\
                                         (-0.70710700000000004, -0.70710700000000004, 0),\
                                         (-0.92388000000000003, -0.382683, 0),\
                                         (-1, 0, 0),\
                                         (-0.92388000000000003, 0.382683, 0),\
                                         (-0.70710700000000004, 0.70710700000000004, 0),\
                                         (-0.382683, 0.92388000000000003, 0),\
                                         (0, 1, 0),\
                                         (0, 0.92388000000000003, -0.382683),\
                                         (0, 0.70710700000000004, -0.70710700000000004),\
                                         (0, 0.382683, -0.92388000000000003),\
                                         (0, 0, -1),\
                                         (-0.382683, 0, -0.92388000000000003),\
                                         (-0.70710700000000004, 0, -0.70710700000000004),\
                                         (-0.92388000000000003, 0, -0.382683),\
                                         (-1, 0, 0),\
                                         (-0.92388000000000003, 0, 0.382683),\
                                         (-0.70710700000000004, 0, 0.70710700000000004),\
                                         (-0.382683, 0, 0.92388000000000003),\
                                         (0, 0, 1),\
                                         (0.382683, 0, 0.92388000000000003),\
                                         (0.70710700000000004, 0, 0.70710700000000004),\
                                         (0.92388000000000003, 0, 0.382683),\
                                         (1, 0, 0),\
                                         (0.92388000000000003, 0, -0.382683),\
                                         (0.70710700000000004, 0, -0.70710700000000004),\
                                         (0.382683, 0, -0.92388000000000003),\
                                         (0, 0, -1)]\
                              )
                              
                cmds.setAttr(crv+".scale", 0, 5.5, 5.5, type = "double3")
                if rigData["FK_ArmList"][i][0::2][o] == rigData["FK_ArmList"][1][0::2][o]:
                    cmds.setAttr(crv+".rz", 45)
                else:
                    cmds.setAttr(crv+".rz", -45)
                    
                cmds.makeIdentity(crv, apply = True, t = 0,  r = 1, s = 1, n = 0, pn = True)
                cmds.rename(crv, rigData["FK_ArmList"][i][0::2][o])
                shape = cmds.listRelatives(rigData["FK_ArmList"][i][0::2][o], children = True)   
                cmds.setAttr(shape[0]+".overrideEnabled", 1)  
                if i == 0:
                    cmds.setAttr(shape[0]+".overrideColor", 14)
                else:
                    cmds.setAttr(shape[0]+".overrideColor", 13)
def PV_CtrlShape():
    for i in range(len(rigData["IK_ArmList"])):      
        crv = cmds.curve( degree = 1,\
                    knot = [0, 1, 2, 3, 4, 5, 6, 7],\
                    point = [(-2, 0, 0),\
                             (1, 0, 1),\
                             (1, 0, -1),\
                             (-2, 0, 0),\
                             (1, 1, 0),\
                             (1, 0, 0),\
                             (1, -1, 0),\
                             (-2, 0, 0)]\
                  )
        
        cmds.setAttr(crv+".ry", -90)             
        cmds.makeIdentity(crv, apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)
        cmds.rename(crv, rigData["IK_ArmList"][i][4])          
        shape = cmds.listRelatives(rigData["IK_ArmList"][i][4], children = True)   
        cmds.setAttr(shape[0]+".overrideEnabled", 1)  
        if i == 0:
            cmds.setAttr(shape[0]+".overrideColor", 14)
        else:
            cmds.setAttr(shape[0]+".overrideColor", 13)
            
def GlobalCtrlSetup(scl, name, GRPname):   
    crv = cmds.curve( degree = 1,\
                knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],\
                point = [(-4.5, 0, 0),\
                         (-2.5, 0, -2),\
                         (-2.5, 0, -1.5),\
                         (-1.5, 0, -1.5),\
                         (-1.5, 0, -2.5),\
                         (-2, 0, -2.5),\
                         (0, 0, -4.5),\
                         (2, 0, -2.5),\
                         (1.5, 0, -2.5),\
                         (1.5, 0, -1.5),\
                         (2.5, 0, -1.5),\
                         (2.5, 0, -2),\
                         (4.5, 0, 0),\
                         (2.5, 0, 2),\
                         (2.5, 0, 1.5),\
                         (1.5, 0, 1.5),\
                         (1.5, 0, 2.5),\
                         (2, 0, 2.5),\
                         (0, 0, 4.5),\
                         (-2, 0, 2.5),\
                         (-1.5, 0, 2.5),\
                         (-1.5, 0, 1.5),\
                         (-2.5, 0, 1.5),\
                         (-2.5, 0, 2),\
                         (-4.5, 0, 0)]\
              )
    ctrlGRP = cmds.group(em = True, name = GRPname)
    cmds.setAttr(crv+".sx", scl) 
    cmds.setAttr(crv+".sy", scl) 
    cmds.setAttr(crv+".sz", scl)             
    cmds.makeIdentity(crv, apply = True, t = 0,  r = 0, s = 1, n = 0, pn = True)
    cmds.parent(crv, ctrlGRP)
    shape = cmds.listRelatives(crv, children = True)   
    cmds.setAttr(shape[0]+".overrideEnabled", 1)   
    if name == rigData["HierarchyOrg"][12]:
        cmds.parent(ctrlGRP, rigData["HierarchyOrg"][2])
        cmds.addAttr(crv, shortName="CharScale", longName="CharScale", defaultValue=1, k=True)
        cmds.connectAttr(crv+".CharScale", crv+".scaleX")
        cmds.connectAttr(crv+".CharScale", crv+".scaleY")
        cmds.connectAttr(crv+".CharScale", crv+".scaleZ")
        cmds.setAttr(crv+".sx", l = True, k = False, cb = False)
        cmds.setAttr(crv+".sy", l = True, k = False, cb = False)
        cmds.setAttr(crv+".sz", l = True, k = False, cb = False)
        cmds.setAttr(shape[0]+".overrideColor", 15)
    else:
        cmds.parent(ctrlGRP, rigData["HierarchyOrg"][12])
        cmds.parent(rigData["HierarchyOrg"][6], crv)
        cmds.parent(rigData["HierarchyOrg"][3], crv)
        cmds.setAttr(crv+".sx", l = True, k = False, cb = False)
        cmds.setAttr(crv+".sy", l = True, k = False, cb = False)
        cmds.setAttr(crv+".sz", l = True, k = False, cb = False)
        cmds.setAttr(crv+".visibility", l = True, k = False, cb = False)
        cmds.setAttr(shape[0]+".overrideColor", 17)
    cmds.rename(crv, name)

            
def IaF_Switch_CtrlShape():
  for i in range(len(rigData["IaF_Switch"])):
    crv = cmds.curve( degree = 1,\
                knot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,\
                        16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],\
                point = [(0, 0, 0),\
                         (6.8580220752251786e-016, 5.6000000000000005, 0),\
                         (0.20683760000000073, 5.6279536000000006, 0),\
                         (0.39966240000000075, 5.7078255999999996, 0),\
                         (0.56568960000000068, 5.8343100000000003, 0),\
                         (0.69217500000000076, 6.0003378000000005, 0),\
                         (0.77204560000000089, 6.1931621999999997, 0),\
                         (0.80000600000000066, 6.4000000461260003, 0),\
                         (0, 6.4000000000000004, 0),\
                         (6.8580220752251786e-016, 5.6000000000000005, 0),\
                         (-0.20683759999999932, 5.6279536000000006, 0),\
                         (-0.39966239999999931, 5.7078256000000005, 0),\
                         (-0.56568959999999924, 5.8343100000000003, 0),\
                         (-0.69217499999999932, 6.0003378000000005, 0),\
                         (-0.77204559999999933, 6.1931622000000006, 0),\
                         (-0.80000599999999933, 6.4000000461260003, 0),\
                         (-0.77204559999999933, 6.6068376000000004, 0),\
                         (-0.69217499999999921, 6.7996623999999999, 0),\
                         (-0.56568959999999913, 6.965689600000001, 0),\
                         (-0.39966239999999914, 7.092175000000001, 0),\
                         (-0.20683759999999915, 7.1720456000000006, 0),\
                         (8.8174643017417381e-016, 7.200006000000001, 0),\
                         (0.20683760000000093, 7.1720456000000006, 0),\
                         (0.39966240000000092, 7.092175000000001, 0),\
                         (0.5656896000000009, 6.965689600000001, 0),\
                         (0.69217500000000098, 6.7996623999999999, 0),\
                         (0.77204560000000089, 6.6068376000000004, 0),\
                         (0.80000600000000066, 6.4000000461260003, 0),\
                         (-0.80000599999999933, 6.4000000461260003, 0),\
                         (0, 6.4000000000000004, 0),\
                         (8.8174643017417381e-016, 7.200006000000001, 0)]\
              )
    if i == 0:
      cmds.setAttr(crv+".rz", -45)
    else: 
      cmds.setAttr(crv+".rz", 45)
    cmds.setAttr(crv+".scale", 2, 2, 2, type = "double3")
    cmds.makeIdentity(crv, apply = True, t = 0,  r = 1, s = 1, n = 0, pn = True)
    cmds.rename(crv, rigData["IaF_Switch"][i][3])
    axis = ["x", "y", "z"]
    attrs = ["t", "r", "s"]
    for ax in axis:
      for attr in attrs:
        cmds.setAttr(rigData["IaF_Switch"][i][3]+"."+attr+ax, l = True, k = False, cb = False)
    cmds.setAttr(rigData["IaF_Switch"][i][3]+".v", l = True, k = False, cb = False)
    cmds.addAttr(rigData["IaF_Switch"][i][3], ln = "__________", at = "enum", en = "switchCTRL", k = True)
    cmds.addAttr(rigData["IaF_Switch"][i][3], shortName="IK_FK", longName="IK_FK", defaultValue=0.0, minValue=0.0, maxValue=1, k=True)
    shape = cmds.listRelatives(rigData["IaF_Switch"][i][3], children = True)   
    cmds.setAttr(shape[0]+".overrideEnabled", 1)  
    if i == 0:
        cmds.setAttr(shape[0]+".overrideColor", 14)
    else:
        cmds.setAttr(shape[0]+".overrideColor", 13)



def StretchyIK():
  for i in range(len(rigData["StretchyIK"])):

    shoulder = cmds.xform("IK_"+rigData["ArmJoints"][i][0], q=True, ws=True, t=True)
    elbow = cmds.xform("IK_"+rigData["ArmJoints"][i][1], q=True, ws=True, t=True)
    wrist = cmds.xform("IK_"+rigData["ArmJoints"][i][2], q=True, ws=True, t=True)

    shldDist = cmds.distanceDimension(sp = shoulder, ep = wrist)
    elbowDist = cmds.distanceDimension(sp = shoulder, ep = elbow)
    wristDist = cmds.distanceDimension(sp = elbow, ep = wrist)

    shldDistDim = cmds.listRelatives(shldDist, p=True)
    elbowDistDim = cmds.listRelatives(elbowDist, p=True)
    wristDistDim = cmds.listRelatives(wristDist, p=True)

    shldDistLoc = cmds.listConnections(shldDist)
    elbowDistLoc = cmds.listConnections(elbowDist)
    
    

    cmds.shadingNode("multiplyDivide", asUtility=True, n=rigData["StretchyIK"][i][0])
    cmds.shadingNode("multiplyDivide", asUtility=True, n=rigData["StretchyIK"][i][1])
    cmds.shadingNode("multiplyDivide", asUtility=True, n=rigData["StretchyIK"][i][2])

    cmds.shadingNode("multDoubleLinear", asUtility=True, n=rigData["StretchyIK"][i][3])
    cmds.shadingNode("multDoubleLinear", asUtility=True, n=rigData["StretchyIK"][i][4])
    cmds.shadingNode("multDoubleLinear", asUtility=True, n=rigData["StretchyIK"][i][5])

    cmds.shadingNode("condition", asUtility=True, n=rigData["StretchyIK"][i][6])
    cmds.shadingNode("condition", asUtility=True, n=rigData["StretchyIK"][i][7])
    cmds.shadingNode("condition", asUtility=True, n=rigData["StretchyIK"][i][8])
    cmds.shadingNode("condition", asUtility=True, n=rigData["StretchyIK"][i][9])

    cmds.shadingNode("blendTwoAttr", asUtility=True, n=rigData["StretchyIK"][i][10])
    cmds.shadingNode("blendTwoAttr", asUtility=True, n=rigData["StretchyIK"][i][11])

    cmds.shadingNode("blendColors", asUtility=True, n=rigData["StretchyIK"][i][12])
    cmds.shadingNode("blendColors", asUtility=True, n=rigData["StretchyIK"][i][13])

    if i == 1:
      cmds.shadingNode("multDoubleLinear", asUtility=True, n=rigData["StretchyIK"][i][14])
      cmds.shadingNode("multDoubleLinear", asUtility=True, n=rigData["StretchyIK"][i][15])
    else:
      pass
    cmds.setAttr(rigData["StretchyIK"][i][0]+".operation", 2)
    cmds.setAttr(rigData["StretchyIK"][i][1]+".operation", 2)
    cmds.setAttr(rigData["StretchyIK"][i][2]+".operation", 2)

    cmds.setAttr(rigData["StretchyIK"][i][6]+".operation", 3)
    cmds.setAttr(rigData["StretchyIK"][i][7]+".operation", 3)
    cmds.setAttr(rigData["StretchyIK"][i][8]+".operation", 3)
    cmds.setAttr(rigData["StretchyIK"][i][9]+".operation", 3)

    cmds.connectAttr(elbowDist+".distance", rigData["StretchyIK"][i][0]+".input1X")
    cmds.connectAttr(wristDist+".distance", rigData["StretchyIK"][i][1]+".input1X")
    cmds.connectAttr(shldDist+".distance", rigData["StretchyIK"][i][2]+".input1X")

    cmds.connectAttr(rigData["StretchyIK"][i][3]+".output", rigData["StretchyIK"][i][2]+".input2X")
    cmds.connectAttr(rigData["StretchyIK"][i][2]+".outputX", rigData["StretchyIK"][i][4]+".input1")
    cmds.connectAttr(rigData["StretchyIK"][i][2]+".outputX", rigData["StretchyIK"][i][5]+".input1")

    cmds.connectAttr(rigData["StretchyIK"][i][0]+".outputX", rigData["StretchyIK"][i][6]+".colorIfTrueR")
    cmds.connectAttr(rigData["StretchyIK"][i][1]+".outputX", rigData["StretchyIK"][i][7]+".colorIfTrueR")

    cmds.connectAttr(shldDist+".distance", rigData["StretchyIK"][i][8]+".firstTerm")
    cmds.connectAttr(shldDist+".distance", rigData["StretchyIK"][i][9]+".firstTerm")
    cmds.connectAttr(rigData["StretchyIK"][i][3]+".output", rigData["StretchyIK"][i][8]+".secondTerm")
    cmds.connectAttr(rigData["StretchyIK"][i][3]+".output", rigData["StretchyIK"][i][9]+".secondTerm")
    cmds.connectAttr(rigData["StretchyIK"][i][4]+".output", rigData["StretchyIK"][i][8]+".colorIfTrueR")
    cmds.connectAttr(rigData["StretchyIK"][i][5]+".output", rigData["StretchyIK"][i][9]+".colorIfTrueR")

    if i == 1:
      cmds.connectAttr(rigData["StretchyIK"][i][6]+".outColorR", rigData["StretchyIK"][i][14]+".input1")
      cmds.connectAttr(rigData["StretchyIK"][i][7]+".outColorR", rigData["StretchyIK"][i][15]+".input1")
      cmds.connectAttr(rigData["StretchyIK"][i][14]+".output", rigData["StretchyIK"][i][10]+".input[1]")
      cmds.connectAttr(rigData["StretchyIK"][i][15]+".output", rigData["StretchyIK"][i][11]+".input[1]")
    else:
      cmds.connectAttr(rigData["StretchyIK"][i][6]+".outColorR", rigData["StretchyIK"][i][10]+".input[1]")
      cmds.connectAttr(rigData["StretchyIK"][i][7]+".outColorR", rigData["StretchyIK"][i][11]+".input[1]")

    cmds.connectAttr(rigData["StretchyIK"][i][8]+".outColorR", rigData["StretchyIK"][i][10]+".input[0]")
    cmds.connectAttr(rigData["StretchyIK"][i][9]+".outColorR", rigData["StretchyIK"][i][11]+".input[0]")

    cmds.connectAttr(rigData["StretchyIK"][i][10]+".output", rigData["StretchyIK"][i][12]+".color1R")
    cmds.connectAttr(rigData["StretchyIK"][i][11]+".output", rigData["StretchyIK"][i][13]+".color1R")

    uparm_dist = cmds.getAttr(elbowDist+".distance")
    lowarm_dist = cmds.getAttr(wristDist+".distance")
    uparm_len = cmds.getAttr("IK_"+rigData["ArmJoints"][i][1]+".tx")
    lowarm_len = cmds.getAttr("IK_"+rigData["ArmJoints"][i][2]+".tx")
    
    cmds.setAttr(rigData["StretchyIK"][i][3]+".input1", uparm_dist+lowarm_dist)
    cmds.setAttr(rigData["StretchyIK"][i][6]+".secondTerm", 1)
    cmds.setAttr(rigData["StretchyIK"][i][7]+".secondTerm", 1)
    cmds.setAttr(rigData["StretchyIK"][i][6]+".colorIfFalseR", uparm_len)
    cmds.setAttr(rigData["StretchyIK"][i][7]+".colorIfFalseR", lowarm_len)

    cmds.setAttr(rigData["StretchyIK"][i][4]+".input2", uparm_len)
    cmds.setAttr(rigData["StretchyIK"][i][5]+".input2", lowarm_len)

    cmds.setAttr(rigData["StretchyIK"][i][8]+".colorIfFalseR", uparm_len)
    cmds.setAttr(rigData["StretchyIK"][i][9]+".colorIfFalseR", lowarm_len)

    cmds.setAttr(rigData["StretchyIK"][i][12]+".color2R", uparm_len)
    cmds.setAttr(rigData["StretchyIK"][i][13]+".color2R", lowarm_len)
    if i == 1:
      cmds.setAttr(rigData["StretchyIK"][i][14]+".input2", -1)
      cmds.setAttr(rigData["StretchyIK"][i][15]+".input2", -1)
    
    cmds.connectAttr(rigData["HierarchyOrg"][12]+".CharScale", rigData["StretchyIK"][i][3]+".input2")
    cmds.connectAttr(rigData["HierarchyOrg"][12]+".CharScale", rigData["StretchyIK"][i][0]+".input2X")
    cmds.connectAttr(rigData["HierarchyOrg"][12]+".CharScale", rigData["StretchyIK"][i][1]+".input2X")
    cmds.connectAttr(rigData["HierarchyOrg"][12]+".CharScale", rigData["StretchyIK"][i][6]+".firstTerm")
    cmds.connectAttr(rigData["HierarchyOrg"][12]+".CharScale", rigData["StretchyIK"][i][7]+".firstTerm")
    
    cmds.rename(shldDistDim, rigData["StretchyIK"][i][16])
    cmds.rename(elbowDistDim, rigData["StretchyIK"][i][17])
    cmds.rename(wristDistDim, rigData["StretchyIK"][i][18])
    cmds.rename(shldDistLoc[0], rigData["StretchyIK"][i][19])
    cmds.rename(elbowDistLoc[1], rigData["StretchyIK"][i][20])
    cmds.rename(shldDistLoc[1], rigData["StretchyIK"][i][21])
    cmds.connectAttr(rigData["StretchyIK"][i][12]+".outputR", "IK_"+rigData["ArmJoints"][i][1]+".tx")
    cmds.connectAttr(rigData["StretchyIK"][i][13]+".outputR", "IK_"+rigData["ArmJoints"][i][2]+".tx")
    
    
    cmds.pointConstraint(rigData["IK_ArmList"][i][0], rigData["StretchyIK"][i][21])
    cmds.pointConstraint(rigData["IK_ArmList"][i][4], rigData["StretchyIK"][i][20])
    
    cmds.connectAttr(rigData["IK_ArmList"][i][4]+".ElbowPin", rigData["StretchyIK"][i][10]+".attributesBlender")
    cmds.connectAttr(rigData["IK_ArmList"][i][4]+".ElbowPin", rigData["StretchyIK"][i][11]+".attributesBlender")
    cmds.connectAttr(rigData["IK_ArmList"][i][0]+".Stretch", rigData["StretchyIK"][i][12]+".blender")
    cmds.connectAttr(rigData["IK_ArmList"][i][0]+".Stretch", rigData["StretchyIK"][i][13]+".blender")
    if i == 0:
        ctrlGRP = cmds.group(em = True, p = rigData["HierarchyOrg"][8] ,name = rigData["HierarchyOrg"][15])
    else:
        ctrlGRP = cmds.group(em = True, p = rigData["HierarchyOrg"][8] ,name = rigData["HierarchyOrg"][16])
        
    cmds.parent(rigData["StretchyIK"][i][16], ctrlGRP)
    cmds.parent(rigData["StretchyIK"][i][17], ctrlGRP)
    cmds.parent(rigData["StretchyIK"][i][18], ctrlGRP)
    cmds.parent(rigData["StretchyIK"][i][19], ctrlGRP)
    cmds.parent(rigData["StretchyIK"][i][20], ctrlGRP)
    cmds.parent(rigData["StretchyIK"][i][21], ctrlGRP)


def IaF_arm_switch():
  for i in range(len(rigData["IaF_Switch"])):
    for o in range(len(rigData["IaF_Switch"][i][:3])):
      pairB = cmds.shadingNode("pairBlend", asUtility=True, n=rigData["IaF_Switch"][i][o])
      cmds.connectAttr("IK_"+rigData["ArmJoints"][i][o]+".translate", pairB+".inTranslate1")
      cmds.connectAttr("FK_"+rigData["ArmJoints"][i][o]+".translate", pairB+".inTranslate2")
      cmds.connectAttr("IK_"+rigData["ArmJoints"][i][o]+".rotate", pairB+".inRotate1")
      cmds.connectAttr("FK_"+rigData["ArmJoints"][i][o]+".rotate", pairB+".inRotate2")
      cmds.connectAttr(pairB+".outTranslate", "bn_"+rigData["ArmJoints"][i][o]+".translate")
      cmds.connectAttr(pairB+".outRotate", "bn_"+rigData["ArmJoints"][i][o]+".rotate")
      cmds.connectAttr(rigData["IaF_Switch"][i][3]+".IK_FK", pairB+".weight")
      cmds.connectAttr(rigData["IaF_Switch"][i][3]+".IK_FK", rigData["FK_ArmList"][i][0::2][o]+".visibility")

    cmds.setDrivenKeyframe(rigData["IK_ArmList"][i][0]+".v", rigData["IK_ArmList"][i][4]+".v", cd = rigData["IaF_Switch"][i][3]+".IK_FK")
    cmds.setAttr(rigData["IaF_Switch"][i][3]+".IK_FK", 1)
    cmds.setAttr(rigData["IK_ArmList"][i][4]+".v", 0)
    cmds.setAttr(rigData["IK_ArmList"][i][0]+".v", 0)
    cmds.setDrivenKeyframe(rigData["IK_ArmList"][i][0]+".v", rigData["IK_ArmList"][i][0]+".v", cd = rigData["IaF_Switch"][i][3]+".IK_FK")
    



HrcSetup()

GlobalCtrlSetup(17, rigData["HierarchyOrg"][12], rigData["HierarchyOrg"][11])
GlobalCtrlSetup(12, rigData["HierarchyOrg"][14], rigData["HierarchyOrg"][13])
     
createArmJnt("IK_")
createArmJnt("FK_")
createArmJnt("bn_")

vecList = ([1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0])
arm_orientJoint("bn_", rigData["ArmJoints"][0][0], rigData["ArmJoints"][0][1], vecList[0], vecList[2])
arm_orientJoint("bn_", rigData["ArmJoints"][0][1], rigData["ArmJoints"][0][2], vecList[0], vecList[2])

arm_orientJoint("IK_", rigData["ArmJoints"][0][0], rigData["ArmJoints"][0][1], vecList[0], vecList[2])
arm_orientJoint("IK_", rigData["ArmJoints"][0][1], rigData["ArmJoints"][0][2], vecList[0], vecList[2])

arm_orientJoint("FK_", rigData["ArmJoints"][0][0], rigData["ArmJoints"][0][1], vecList[0], vecList[2])
arm_orientJoint("FK_", rigData["ArmJoints"][0][1], rigData["ArmJoints"][0][2], vecList[0], vecList[2])

arm_orientJoint("IK_", rigData["ArmJoints"][1][0], rigData["ArmJoints"][1][1], vecList[1], vecList[3])
arm_orientJoint("IK_", rigData["ArmJoints"][1][1], rigData["ArmJoints"][1][2], vecList[1], vecList[3])

arm_orientJoint("bn_", rigData["ArmJoints"][1][0], rigData["ArmJoints"][1][1], vecList[1], vecList[3])
arm_orientJoint("bn_", rigData["ArmJoints"][1][1], rigData["ArmJoints"][1][2], vecList[1], vecList[3])

arm_orientJoint("FK_", rigData["ArmJoints"][1][0], rigData["ArmJoints"][1][1], vecList[1], vecList[3])
arm_orientJoint("FK_", rigData["ArmJoints"][1][1], rigData["ArmJoints"][1][2], vecList[1], vecList[3])

cleanJntOrientArm("IK_")
cleanJntOrientArm("FK_")
cleanJntOrientArm("bn_")


IK_Create()
IK_CtrlMaker()
lf_pvpos = calculatePVPosition(["IK_"+rigData["ArmJoints"][0][0], "IK_"+rigData["ArmJoints"][0][1], "IK_"+rigData["ArmJoints"][0][2]])
lf_pvctrlinfo = lf_pvpos
rt_pvpos = calculatePVPosition(["IK_"+rigData["ArmJoints"][1][0], "IK_"+rigData["ArmJoints"][1][1], "IK_"+rigData["ArmJoints"][1][2]])
rt_pvctrlinfo = rt_pvpos
PV_CtrlShape()
PV_CtrlMaker(lf_pvctrlinfo, rt_pvctrlinfo)
FK_CtrlShape()
FK_CtrlMaker()
StretchyIK()
IaF_Switch_CtrlShape()
IaF_Switch_CtrlMaker()
IaF_arm_switch()
 