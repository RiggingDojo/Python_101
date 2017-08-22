import maya.cmds as cmds
rigData={}
rigData["ArmJoints"]=[
                      ["lf_shoulder_JNT", "lf_elbow_JNT", "lf_wrist_JNT","lf_wristEnd_JNT"],
                      ["rt_shoulder_JNT", "rt_elbow_JNT", "rt_wrist_JNT", "rt_wristEnd_JNT"]
                      ]
rigData["IK_ArmList"] = [
                         ["IK_lf_arm_CTRL", "IK_lf_arm_CTRL_srt", "rIK_lf_arm_Hndl", "rIK_lf_arm_Eff", "IK_lf_armPV_CTRL", "IK_lf_armPV_CTRL_srt"], 
                         ["IK_rt_arm_CTRL", "IK_rt_arm_CTRL_srt", "rIK_rt_arm_Hndl", "rIK_rt_arm_Eff", "IK_rt_armPV_CTRL", "IK_rt_armPV_CTRL_srt"]
                        ]
rigData["JointsPos"]=[
                     [[9.58574, 118.83508, -0.70541], [23.075005157215955, 101.68192524537305, -3.012311], [37.7333821711548, 83.04211007076694, -0.7054100000000001], [59.84439, 61.86297, 1.30086]],
                     [[-9.58574, 118.83508, -0.70541], [-23.075005157215955, 101.68192524537305, -3.012311], [-37.7333821711548, 83.04211007076694, -0.7054100000000001], [-59.84439, 61.86297, 1.30086]]
                     ]
rigData["FK_ArmList"] = [
                         ["FK_lf_shoulder_CTRL", "FK_lf_shoulder_CTRL_srt", "FK_lf_elbow_CTRL", "FK_lf_elbow_CTRL_srt", "FK_lf_wrist_CTRL", "FK_lf_wrist_CTRL_srt"], 
                         ["FK_rt_shoulder_CTRL", "FK_rt_shoulder_CTRL_srt", "FK_rt_elbow_CTRL", "FK_rt_elbow_CTRL_srt", "FK_rt_wrist_CTRL", "FK_rt_wrist_CTRL_srt"]
                         ]
rigData["HierarchyOrg"] = ["singer", "singer_GEO_hrc", "GlobalMove_CTRL_srt", "JNT_hrc", "IK_skeleton_hrc", "FK_skeleton_hrc", "skeleton_hrc", "extra_JNT_hrc", "ControlObjects_hrc", "ExtraNode_hrc",
"toHide_hrc", "toShow_hrc"]                    


class Rig_Arm:
    def rig_arm(self):
        self.HrcSetup()
            #Building joints
        self.createArmJnt("IK_")
        self.createArmJnt("FK_")
        self.createArmJnt("bn_")

            #Orient Joints
        vecList = ([1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0]) 
        self.arm_orientJoint("bn_"+rigData["ArmJoints"][0][0],"bn_"+rigData["ArmJoints"][0][1], vecList[0], vecList[2])
        self.arm_orientJoint("bn_"+rigData["ArmJoints"][0][1],"bn_"+rigData["ArmJoints"][0][2], vecList[0], vecList[2])
        self.arm_orientJoint("bn_"+rigData["ArmJoints"][0][2],"bn_"+rigData["ArmJoints"][0][3], vecList[0], vecList[2])

        self.arm_orientJoint("IK_"+rigData["ArmJoints"][0][0],"IK_"+rigData["ArmJoints"][0][1], vecList[0], vecList[2])
        self.arm_orientJoint("IK_"+rigData["ArmJoints"][0][1],"IK_"+rigData["ArmJoints"][0][2], vecList[0], vecList[2])
        self.arm_orientJoint("IK_"+rigData["ArmJoints"][0][2],"IK_"+rigData["ArmJoints"][0][3], vecList[0], vecList[2])

        self.arm_orientJoint("FK_"+rigData["ArmJoints"][0][0],"FK_"+rigData["ArmJoints"][0][1], vecList[0], vecList[2])
        self.arm_orientJoint("FK_"+rigData["ArmJoints"][0][1],"FK_"+rigData["ArmJoints"][0][2], vecList[0], vecList[2])
        self.arm_orientJoint("FK_"+rigData["ArmJoints"][0][2],"FK_"+rigData["ArmJoints"][0][3], vecList[0], vecList[2])

        self.arm_orientJoint("IK_"+rigData["ArmJoints"][1][0],"IK_"+rigData["ArmJoints"][1][1], vecList[1], vecList[3])
        self.arm_orientJoint("IK_"+rigData["ArmJoints"][1][1],"IK_"+rigData["ArmJoints"][1][2], vecList[1], vecList[3])
        self.arm_orientJoint("IK_"+rigData["ArmJoints"][1][2],"IK_"+rigData["ArmJoints"][1][3], vecList[1], vecList[3])

        self.arm_orientJoint("bn_"+rigData["ArmJoints"][1][0],"bn_"+rigData["ArmJoints"][1][1], vecList[1], vecList[3])
        self.arm_orientJoint("bn_"+rigData["ArmJoints"][1][1],"bn_"+rigData["ArmJoints"][1][2], vecList[1], vecList[3])
        self.arm_orientJoint("bn_"+rigData["ArmJoints"][1][2],"bn_"+rigData["ArmJoints"][1][3], vecList[1], vecList[3])

        self.arm_orientJoint("FK_"+rigData["ArmJoints"][1][0],"FK_"+rigData["ArmJoints"][1][1], vecList[1], vecList[3])
        self.arm_orientJoint("FK_"+rigData["ArmJoints"][1][1],"FK_"+rigData["ArmJoints"][1][2], vecList[1], vecList[3])
        self.arm_orientJoint("FK_"+rigData["ArmJoints"][1][2],"FK_"+rigData["ArmJoints"][1][3], vecList[1], vecList[3])

            #Cleaning Joint Orient 
        self.cleanJntOrientArm("IK_")
        self.cleanJntOrientArm("FK_")
        self.cleanJntOrientArm("bn_")
        
            #Making IK
        self.IK_Create()
            
            #Making IK Controls
        self.IK_CtrlMaker()
            # PV Position 
        
        lf_pvpos = self.calculatePVPosition(["IK_"+rigData["ArmJoints"][0][0], "IK_"+rigData["ArmJoints"][0][1], "IK_"+rigData["ArmJoints"][0][2]])
        lf_pvctrlinfo = [
        [lf_pvpos, rigData["IK_ArmList"][0][4], rigData["IK_ArmList"][0][5]]
        ]
        rt_pvpos = self.calculatePVPosition(["IK_"+rigData["ArmJoints"][1][0], "IK_"+rigData["ArmJoints"][1][1], "IK_"+rigData["ArmJoints"][1][2]])
        rt_pvctrlinfo = [
        [rt_pvpos, rigData["IK_ArmList"][1][4], rigData["IK_ArmList"][1][5]]
        ]
        self.FK_CtrlShape()
        self.FK_CtrlMaker()
    def HrcSetup(self):
         cmds.group(em = True, name = rigData["HierarchyOrg"][0])
         cmds.group(em = True, p = rigData["HierarchyOrg"][0], name = rigData["HierarchyOrg"][1])
         cmds.group(em = True, p = rigData["HierarchyOrg"][0], name = rigData["HierarchyOrg"][2])
         cmds.group(em = True, p = rigData["HierarchyOrg"][2], name = rigData["HierarchyOrg"][3])
         cmds.group(em = True, p = rigData["HierarchyOrg"][3], name = rigData["HierarchyOrg"][4])
         cmds.group(em = True, p = rigData["HierarchyOrg"][3], name = rigData["HierarchyOrg"][5])
         cmds.group(em = True, p = rigData["HierarchyOrg"][3], name = rigData["HierarchyOrg"][6])
         cmds.group(em = True, p = rigData["HierarchyOrg"][3], name = rigData["HierarchyOrg"][7])
         cmds.group(em = True, p = rigData["HierarchyOrg"][2], name = rigData["HierarchyOrg"][8])
         cmds.group(em = True, p = rigData["HierarchyOrg"][0], name = rigData["HierarchyOrg"][9])
         cmds.group(em = True, p = rigData["HierarchyOrg"][9], name = rigData["HierarchyOrg"][10])
         cmds.group(em = True, p = rigData["HierarchyOrg"][9], name = rigData["HierarchyOrg"][11])    
    #Building joints___Function
    def createArmJnt(self, jntType):
        for i in range(len(rigData["ArmJoints"])):
            for o in range(len(rigData["ArmJoints"][i])):
                cmds.joint(n=jntType+rigData["ArmJoints"][i][o], p=rigData["JointsPos"][i][o])        
                cmds.select(cl=True)
                
    #Orient Joints____Function
    def arm_orientJoint(self, orntJnt, aimJnt, aimVec, upVec):
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
         
        

    #Cleaning up joint orinet___Function    
    def cleanJntOrientArm(self, jntType):
        for i in range(len(rigData["ArmJoints"])):
            for o in range(len(rigData["ArmJoints"][i])):
                if rigData["ArmJoints"][i][o] == rigData["ArmJoints"][0][0] or rigData["ArmJoints"][i][o] == rigData["ArmJoints"][1][0]:
                    pass
                elif rigData["ArmJoints"][i][o] == rigData["ArmJoints"][0][3] or rigData["ArmJoints"][i][o] == rigData["ArmJoints"][1][3]:
                    cmds.delete(jntType+rigData["ArmJoints"][i][o])
                    
                elif rigData["ArmJoints"][i][o] == rigData["ArmJoints"][0][2] or rigData["ArmJoints"][i][o] == rigData["ArmJoints"][1][2]:
                    cmds.setAttr(jntType+rigData["ArmJoints"][i][o] +'.jointOrientX', 0)    
                else:
                    cmds.setAttr(jntType+rigData["ArmJoints"][i][o] +".jointOrientX", 0)
                    cmds.setAttr(jntType+rigData["ArmJoints"][i][o] +".jointOrientY", 0)

    #Making Controls___Function
    
    def IK_CtrlMaker(self):
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
            cmds.parent(ctrlGRP, rigData["HierarchyOrg"][8])

    def IK_Create(self):
        lf_IKH = cmds.ikHandle( n = rigData["IK_ArmList"][0][2] , sj = "IK_"+rigData["ArmJoints"][0][0], ee = "IK_" + rigData["ArmJoints"][0][2])
        lf_IKE = cmds.rename(lf_IKH[1], rigData["IK_ArmList"][0][3])
        rt_IKH = cmds.ikHandle( n = rigData["IK_ArmList"][1][2] , sj = "IK_"+rigData["ArmJoints"][1][0], ee = "IK_" + rigData["ArmJoints"][1][2])
        rt_IKE = cmds.rename(rt_IKH[1], rigData["IK_ArmList"][1][3])

        #Orienting IK Handle
        cmds.parent(lf_IKH[0], "bn_"+rigData["ArmJoints"][0][2])
        cmds.makeIdentity(lf_IKH[0], apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)
        cmds.parent(lf_IKH[0], w = True)
        
        cmds.parent(rt_IKH[0], "bn_"+rigData["ArmJoints"][1][2])
        cmds.makeIdentity(rt_IKH[0], apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)
        cmds.parent(rt_IKH[0], w = True)   
    
    def calculatePVPosition(self, jnts):
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
    
    def FK_CtrlMaker(self):     
        for o in range(len(rigData["JointsPos"])):
            for s in range(len(rigData["JointsPos"][o])):
                pos = rigData["JointsPos"][o][s]
                ctrlGRP = cmds.group(em = True, name = rigData["FK_ArmList"][o][1::2][s])
                cmds.parent(rigData["FK_ArmList"][o][0::2][s], ctrlGRP)
                cmds.xform(ctrlGRP, t=pos, ws = True)
                cmds.parent(ctrlGRP, "FK_"+rigData["ArmJoints"][o][s])   
                cmds.makeIdentity(ctrlGRP, apply=True, t=0, r=1, s=0, n=0, pn=True)
                cmds.parent(ctrlGRP, rigData["HierarchyOrg"][8])
     
    def FK_CtrlShape(self):
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

    def PV_CtrlShape(self):
        cmds.curve( degree = 1,\
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