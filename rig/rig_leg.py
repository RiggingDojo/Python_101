import maya.cmds as cmds
rigData={}
rigData["LegJoints"]=[
                      ["lf_thigh_JNT", "lf_knee_JNT", "lf_ankle_JNT", "lf_ball_JNT", "lf_toeEnd_JNT"],
                      ["rt_thigh_JNT", "rt_knee_JNT", "rt_ankle_JNT", "rt_ball_JNT", "rt_toeEnd_JNT"]
                      ]
rigData["IK_LegList"] = [
                         ["IK_lf_leg_CTRL", "IK_lf_leg_CTRL_srt", "rIK_lf_leg_Hndl", "rIK_lf_leg_Eff", "IK_lf_legPV_CTRL", "IK_lf_legPV_CTRL_srt"], 
                         ["IK_rt_leg_CTRL", "IK_rt_leg_CTRL_srt", "rIK_rt_leg_Hndl", "rIK_rt_leg_Eff", "IK_rt_legPV_CTRL", "IK_rt_legPV_CTRL_srt"]
                        ]
rigData["LegJointsPos"]=[
                     [[6.5, 84.50842991096013, 2.583954937334773] , [8.048305798026842, 44.32622875750865, 2.583954937334773] , 
                     [8.423001431704513, 7.229312198647769, -2.724704080082415] , [8.483672393266385, 1.222555256978227, 12.39703482553402] , [8.483672393266385, 1.2225552569782272, 22.039273239055735]],
                     [[-6.5, 84.50842991096013, 2.583954937334773] , [-8.048305798026842, 44.32622875750865, 2.583954937334773] , 
                     [-8.423001431704513, 7.229312198647769, -2.724704080082415] , [-8.483672393266385, 1.222555256978227, 12.39703482553402] , [-8.483672393266385, 1.2225552569782272, 22.039273239055735]]
                     ]
rigData["FK_LegList"] = [
                         ["FK_lf_thigh_CTRL", "FK_lf_thigh_CTRL_srt", "FK_lf_knee_CTRL", "FK_lf_knee_CTRL_srt", "FK_lf_ankle_CTRL", "FK_lf_ankle_CTRL_srt", "FK_lf_ball_CTRL", "FK_lf_ball_CTRL_srt", "FK_lf_toeEnd_CTRL", "FK_lf_toeEnd_CTRL_srt"], 
                         ["FK_rt_thigh_CTRL", "FK_rt_thigh_CTRL_srt", "FK_rt_knee_CTRL", "FK_rt_knee_CTRL_srt", "FK_rt_ankle_CTRL", "FK_rt_ankle_CTRL_srt", "FK_rt_ball_CTRL", "FK_rt_ball_CTRL_srt", "Fk_rt_toeEnd_CTRL", "FK_rt_toeEnd_CTRL_srt"]
                         ]   
                    
rigData["HierarchyOrg"] = ["singer", "singer_GEO_hrc", "GlobalMove_srt", "JNT_hrc", "skeleton_hrc", "extra_JNT_hrc", "ControlObjects_hrc", "ExtraNode_hrc",
                            "toHide_hrc", "toShow_hrc", "IKh_hrc", "World_CTRL_srt", "World_CTRL", "Local_CTRL_srt", "Local_CTRL", "IK_lf_Stretch_leg_hrc", "IK_rt_Stretch_leg_hrc" ]
rigData["LegStretchyIK"] = [
                              ["scaleComp_lf_upleg_dist_multDiv", "scaleComp_lf_lowleg_dist_multDiv", "stretch_lf_leg_multDiv", 
                              "scaleComp_lf_leg_dist_mdl", "stretch_lf_upleg_mdl", "stretch_lf_lowleg_mdl",
                              "scaleComp_lf_upleg_dist_cond", "scaleComp_lf_lowleg_dist_cond", "stretch_lf_upleg_cond", "stretch_lf_lowleg_cond",
                              "stretch_lf_upleg_kneePin_blendAttr","stretch_lf_lowleg_kneePin_blendAttr",
                              "stretch_lf_upleg_enable_blend", "stretch_lf_lowleg_enable_blend",
                              "scaleComp_lf_upleg_dist_Inverse_mdl", "scaleComp_lf_lowleg_dist_Inverse_mdl",
                              "lf_leg_distD", "lf_upleg_distD", "lf_lowleg_distD", "lf_thigh_distLoc", "lf_knee_distLoc", "lf_ankle_distLoc", "lf_ankle_distLoc"],
                              ["scaleComp_rt_upleg_dist_multDiv", "scaleComp_rt_lowleg_dist_multDiv", "stretch_rt_leg_multDiv", 
                              "scaleComp_rt_leg_dist_mdl", "stretch_rt_upleg_mdl", "stretch_rt_lowleg_mdl",
                              "scaleComp_rt_upleg_dist_cond", "scaleComp_rt_lowleg_dist_cond", "stretch_rt_upleg_cond", "stretch_rt_lowleg_cond",
                              "stretch_rt_upleg_elbowPin_blendAttr","stretch_rt_lowleg_elbowPin_blendAttr",
                              "stretch_rt_upleg_enable_blend", "stretch_rt_lowleg_enable_blend",
                              "scaleComp_rt_upleg_dist_Inverse_mdl", "scaleComp_rt_lowleg_dist_Inverse_mdl",
                              "rt_leg_distD", "rt_upleg_distD", "rt_lowleg_distD", "rt_thigh_distLoc", "rt_knee_distLoc", "rt_ankle_distLoc", "rt_ankle_distLoc"]
                               ]
rigData["IaF_SwitchLeg"] = [
                         ["IaF_lf_thigh_pairB", "IaF_lf_knee_pairB", "IaF_lf_ankle_pairB", "IaF_lf_leg_switch_CTRL", "IaF_lf_leg_switch_CTRL_srt"],
                         ["IaF_rt_thigh_pairB", "IaF_rt_knee_pairB", "IaF_rt_ankle_pairB", "IaF_rt_leg_switch_CTRL", "IaF_rt_leg_switch_CTRL_srt"]
                          ]


class Rig_Leg:
    def rig_leg(self):
        self.createLegJnt("IK_")
        self.createLegJnt("FK_")
        self.createLegJnt("bn_")

        vecList = ([1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0])
        self.leg_orientJoint("bn_", rigData["LegJoints"][0][0], rigData["LegJoints"][0][1], vecList[0], vecList[2])
        self.leg_orientJoint("bn_", rigData["LegJoints"][0][1], rigData["LegJoints"][0][2], vecList[0], vecList[2])
        self.leg_orientJoint("bn_", rigData["LegJoints"][0][3], rigData["LegJoints"][0][4], vecList[0], vecList[2])


        self.leg_orientJoint("IK_", rigData["LegJoints"][0][0], rigData["LegJoints"][0][1], vecList[0], vecList[2])
        self.leg_orientJoint("IK_", rigData["LegJoints"][0][1], rigData["LegJoints"][0][2], vecList[0], vecList[2])
        self.leg_orientJoint("IK_", rigData["LegJoints"][0][3], rigData["LegJoints"][0][4], vecList[0], vecList[2])


        self.leg_orientJoint("FK_", rigData["LegJoints"][0][0], rigData["LegJoints"][0][1], vecList[0], vecList[2])
        self.leg_orientJoint("FK_", rigData["LegJoints"][0][1], rigData["LegJoints"][0][2], vecList[0], vecList[2])
        self.leg_orientJoint("FK_", rigData["LegJoints"][0][3], rigData["LegJoints"][0][4], vecList[0], vecList[2])


        self.leg_orientJoint("IK_", rigData["LegJoints"][1][0], rigData["LegJoints"][1][1], vecList[1], vecList[3])
        self.leg_orientJoint("IK_", rigData["LegJoints"][1][1], rigData["LegJoints"][1][2], vecList[1], vecList[3])
        self.leg_orientJoint("IK_", rigData["LegJoints"][1][3], rigData["LegJoints"][1][4], vecList[1], vecList[3])


        self.leg_orientJoint("bn_", rigData["LegJoints"][1][0], rigData["LegJoints"][1][1], vecList[1], vecList[3])
        self.leg_orientJoint("bn_", rigData["LegJoints"][1][1], rigData["LegJoints"][1][2], vecList[1], vecList[3])
        self.leg_orientJoint("bn_", rigData["LegJoints"][1][3], rigData["LegJoints"][1][4], vecList[1], vecList[3])

        self.leg_orientJoint("FK_", rigData["LegJoints"][1][0], rigData["LegJoints"][1][1], vecList[1], vecList[3])
        self.leg_orientJoint("FK_", rigData["LegJoints"][1][1], rigData["LegJoints"][1][2], vecList[1], vecList[3])
        self.leg_orientJoint("FK_", rigData["LegJoints"][1][3], rigData["LegJoints"][1][4], vecList[1], vecList[3])


        self.cleanJntOrientLeg("IK_")
        self.cleanJntOrientLeg("FK_")
        self.cleanJntOrientLeg("bn_")


        self.IK_LegCreate()
        self.IK_LegCtrlMaker()
        lf_pvpos = self.leg_calculatePVPosition(["IK_"+rigData["LegJoints"][0][0], "IK_"+rigData["LegJoints"][0][1], "IK_"+rigData["LegJoints"][0][2]])
        lf_pvctrlinfo = lf_pvpos
        rt_pvpos = self.leg_calculatePVPosition(["IK_"+rigData["LegJoints"][1][0], "IK_"+rigData["LegJoints"][1][1], "IK_"+rigData["LegJoints"][1][2]])
        rt_pvctrlinfo = rt_pvpos
        self.PV_LegCtrlShape()
        self.PV_LegCtrlMaker(lf_pvctrlinfo, rt_pvctrlinfo)
        self.FK_LegCtrlShape()
        self.FK_LegCtrlMaker()
        self.LegStretchyIK()
        self.IaF_SwitchLeg_CtrlShape()
        self.IaF_SwitchLeg_CtrlMaker()
        self.IaF_leg_switch()






    def createLegJnt(self, jntType):
        for i in range(len(rigData["LegJoints"])):
                for o in range(len(rigData["LegJoints"][i])):
                    cmds.joint(n=jntType+rigData["LegJoints"][i][o], p=rigData["LegJointsPos"][i][o])
                    cmds.select(cl=True)

    def leg_orientJoint(self, jntType, orntJnt, aimJnt, aimVec, upVec):
        loc = cmds.spaceLocator()
        cmds.parent(loc[0], jntType+orntJnt)
        if orntJnt==rigData["LegJoints"][0][3] or orntJnt==rigData["LegJoints"][1][3]:
            cmds.setAttr(loc[0]+".translate", 0, 5, 0, type = "double3")
        else:    
            cmds.setAttr(loc[0]+".translate", 0, 0, 5, type = "double3")
        cmds.parent(loc[0], w=True)
        cmds.aimConstraint(jntType+aimJnt, jntType+orntJnt, offset = [0, 0, 0], weight = True, aimVector = aimVec ,
                                                     upVector = upVec, worldUpType = "object" , worldUpObject = loc[0])
        cmds.delete(jntType+orntJnt+"_aimConstraint1")
        cmds.makeIdentity(jntType+orntJnt, apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)
        cmds.delete(loc[0])
  
    
    #Cleaning up joint orinet___Function    
    def cleanJntOrientLeg(self, jntType):
        for i in range(len(rigData["LegJoints"])):
            
            cmds.parent(jntType+rigData["LegJoints"][i][0], jntType+rigData["HierarchyOrg"][4])
            
            cmds.parent(jntType+rigData["LegJoints"][i][1], jntType+rigData["LegJoints"][i][0])
            if i==1:
                cmds.setAttr(jntType+rigData["LegJoints"][i][2]+".jointOrient", -90, 0, 90, type = "double3")
            else:
                cmds.setAttr(jntType+rigData["LegJoints"][i][2]+".jointOrient", 90, 0, -90, type = "double3")
            cmds.parent(jntType+rigData["LegJoints"][i][2], jntType+rigData["LegJoints"][i][1])
            cmds.setAttr(jntType+rigData["LegJoints"][i][1]+".jointOrientX", 0)
            cmds.setAttr(jntType+rigData["LegJoints"][i][1]+".jointOrientY", 0)
            cmds.setAttr(jntType+rigData["LegJoints"][i][1]+".ty", 0)
            cmds.setAttr(jntType+rigData["LegJoints"][i][1]+".tz", 0)    
            
            
            cmds.parent(jntType+rigData["LegJoints"][i][3], jntType+rigData["LegJoints"][i][2])
            cmds.setAttr(jntType+rigData["LegJoints"][i][3]+".tz", 0)
            
            cmds.setAttr(jntType+rigData["LegJoints"][i][3]+".jointOrientX", 0)
            cmds.setAttr(jntType+rigData["LegJoints"][i][3]+".jointOrientY", 0)
            cmds.setAttr(jntType+rigData["LegJoints"][i][2]+".ty", 0)
            cmds.setAttr(jntType+rigData["LegJoints"][i][2]+".tz", 0)
            cmds.setAttr(jntType+rigData["LegJoints"][i][3]+".tz", 0)
            
            
            
            cmds.parent(jntType+rigData["LegJoints"][i][4], jntType+rigData["LegJoints"][i][3])
            cmds.setAttr(jntType+rigData["LegJoints"][i][4]+".jointOrient", 0, 0, 0, type = "double3")
            cmds.setAttr(jntType+rigData["LegJoints"][i][4]+".ty", 0)
            cmds.setAttr(jntType+rigData["LegJoints"][i][4]+".tz", 0)



                
    def IK_LegCreate(self):
        for i in range(len(rigData["IK_LegList"])):      
            IKH = cmds.ikHandle( n = rigData["IK_LegList"][i][2] , sj = "IK_"+rigData["LegJoints"][i][0], ee = "IK_" + rigData["LegJoints"][i][2])
            IKE = cmds.rename(IKH[1], rigData["IK_LegList"][i][3])
            #Orienting IK Handle
            cmds.parent(IKH[0], "bn_"+rigData["LegJoints"][i][2])
            cmds.makeIdentity(IKH[0], apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)
            cmds.parent(IKH[0], rigData["HierarchyOrg"][10])
    
                  
                
    def IK_LegCtrlMaker(self):
        for i in range(len(rigData["LegJointsPos"])):
            pos = cmds.joint("IK_"+rigData["LegJoints"][i][2], q=True, p=True)
            ctrlGRP = cmds.group(em = True, name = rigData["IK_LegList"][i][1])
            ctrl = cmds.circle(n=rigData["IK_LegList"][i][0], r = 6, nr= (0, 90, 0), c=(0, 0, 0), ch=False)
            cmds.parent(ctrl, ctrlGRP)
            cmds.xform(ctrlGRP, t=pos, ws = True)
            cmds.parent(ctrlGRP, rigData["IK_LegList"][i][2])
            cmds.makeIdentity(ctrlGRP, apply = True, t = 0, r = 1, s = 0, n = 0, pn = True)
            cmds.parent(ctrlGRP, rigData["HierarchyOrg"][6])
            cmds.pointConstraint(rigData["IK_LegList"][i][0], rigData["IK_LegList"][i][2])
            cmds.setAttr(rigData["IK_LegList"][i][0]+".sx", l = True, k = False, cb = False) 
            cmds.setAttr(rigData["IK_LegList"][i][0]+".sy", l = True, k = False, cb = False) 
            cmds.setAttr(rigData["IK_LegList"][i][0]+".sz", l = True, k = False, cb = False) 
            cmds.setAttr(rigData["IK_LegList"][i][0]+".rx", l = True, k = False, cb = False) 
            cmds.setAttr(rigData["IK_LegList"][i][0]+".ry", l = True, k = False, cb = False) 
            cmds.setAttr(rigData["IK_LegList"][i][0]+".rz", l = True, k = False, cb = False)
            cmds.addAttr(rigData["IK_LegList"][i][0], ln = "__________", at = "enum", en = "ExtraCTRL", k = True)
            cmds.addAttr(rigData["IK_LegList"][i][0], shortName="Stretch", longName="Stretch", defaultValue=0.0, minValue=0.0, maxValue=1, k = True )
            shape = cmds.listRelatives(rigData["IK_LegList"][i][0], children = True)   
            cmds.setAttr(shape[0]+".overrideEnabled", 1)  
            if i == 0:
                cmds.setAttr(shape[0]+".overrideColor", 14)
            else:
                cmds.setAttr(shape[0]+".overrideColor", 13)

        
    def FK_LegCtrlMaker(self):     
        for o in range(len(rigData["LegJointsPos"])):
            for s in range(len(rigData["LegJointsPos"][o])):
                pos = cmds.joint("FK_"+rigData["LegJoints"][o][s], q=True, p=True)
                ctrlGRP = cmds.group(em = True, name = rigData["FK_LegList"][o][1::2][s])
                cmds.parent(rigData["FK_LegList"][o][0::2][s], ctrlGRP)
                cmds.xform(ctrlGRP, t=pos, ws = True)
                cmds.parent(ctrlGRP, "FK_"+rigData["LegJoints"][o][s])   
                cmds.makeIdentity(ctrlGRP, apply=True, t=0, r=1, s=0, n=0, pn=True)
                if s!=0:
                    cmds.parent(ctrlGRP, rigData["FK_LegList"][o][0::2][s-1])
                else:
                    cmds.parent(ctrlGRP, rigData["HierarchyOrg"][6])
                cmds.orientConstraint(rigData["FK_LegList"][o][0::2][s], "FK_"+rigData["LegJoints"][o][s])
            
    def PV_LegCtrlMaker(self, lf_position, rt_position):
        for i in range(len(rigData["IK_LegList"])):
            if i==0:
                pos = lf_position
            else:
                pos = rt_position
            ctrlGRP = cmds.group(em = True, name = rigData["IK_LegList"][i][5])
           
            cmds.parent(rigData["IK_LegList"][i][4], ctrlGRP)
            cmds.xform(ctrlGRP, t=pos, ws=True)
            cmds.parent(ctrlGRP, rigData["HierarchyOrg"][6])
            wPos = cmds.getAttr(rigData["IK_LegList"][i][5]+".tz")
            cmds.setAttr(rigData["IK_LegList"][i][5]+".tz", wPos+20)
            cmds.poleVectorConstraint(rigData["IK_LegList"][i][4], rigData["IK_LegList"][i][2])
            cmds.setAttr(rigData["IK_LegList"][i][4]+".sx", l = True, k = False, cb = False)  
            cmds.setAttr(rigData["IK_LegList"][i][4]+".sy", l = True, k = False, cb = False) 
            cmds.setAttr(rigData["IK_LegList"][i][4]+".sz", l = True, k = False, cb = False) 
            cmds.setAttr(rigData["IK_LegList"][i][4]+".rx", l = True, k = False, cb = False)
            cmds.setAttr(rigData["IK_LegList"][i][4]+".ry", l = True, k = False, cb = False) 
            cmds.setAttr(rigData["IK_LegList"][i][4]+".rz", l = True, k = False, cb = False)
            cmds.addAttr(rigData["IK_LegList"][i][4], ln = "__________", at = "enum", en = "ExtraCTRL", k = True)
            cmds.addAttr(rigData["IK_LegList"][i][4], shortName="ElbowPin", longName="ElbowPin", defaultValue=0.0, minValue=0.0, maxValue=1, k=True )  



    def IaF_SwitchLeg_CtrlMaker(self):
        for i in range(len(rigData["IaF_SwitchLeg"])):
            pos = rigData["LegJointsPos"][i][2]
            ctrlGRP = cmds.group(em=True, name = rigData["IaF_SwitchLeg"][i][4])
            cmds.parent(rigData["IaF_SwitchLeg"][i][3], ctrlGRP)
            cmds.xform(ctrlGRP, t=pos, ws=True)
            cmds.parent(ctrlGRP, rigData["HierarchyOrg"][6])






    def leg_calculatePVPosition(self, jnts):
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

    def FK_LegCtrlShape(self):
        for i in range(len(rigData["FK_LegList"])):
            for o in range(len(rigData["FK_LegList"][i][0::2])):            
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
                
                cmds.rename(crv, rigData["FK_LegList"][i][0::2][o])
                if rigData["FK_LegList"][i][0::2][o]==rigData["FK_LegList"][i][::2][:4][0] or rigData["FK_LegList"][i][0::2][o]==rigData["FK_LegList"][i][::2][:3][1] or rigData["FK_LegList"][i][0::2][o]==rigData["FK_LegList"][i][::2][:3][2]:
                    cmds.setAttr(rigData["FK_LegList"][i][0::2][o]+".rz", 90)
                else:
                    cmds.setAttr(rigData["FK_LegList"][i][0::2][o]+".ry", 90)
                    
                cmds.makeIdentity(rigData["FK_LegList"][i][0::2][o], apply = True, t = 0,  r = 1, s = 1, n = 0, pn = True)
                shape = cmds.listRelatives(rigData["FK_LegList"][i][0::2][o], children = True)   
                cmds.setAttr(shape[0]+".overrideEnabled", 1)  
                if i == 0:
                    cmds.setAttr(shape[0]+".overrideColor", 14)
                else:
                    cmds.setAttr(shape[0]+".overrideColor", 13)
                    

 
                    
    def PV_LegCtrlShape(self):
        for i in range(len(rigData["IK_LegList"])):      
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
            
            cmds.setAttr(crv+".ry", 90)             
            cmds.makeIdentity(crv, apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)
            cmds.rename(crv, rigData["IK_LegList"][i][4])          
            shape = cmds.listRelatives(rigData["IK_LegList"][i][4], children = True)   
            cmds.setAttr(shape[0]+".overrideEnabled", 1)  
            if i == 0:
                cmds.setAttr(shape[0]+".overrideColor", 14)
            else:
                cmds.setAttr(shape[0]+".overrideColor", 13)

            
    def IaF_SwitchLeg_CtrlShape(self):
        for i in range(len(rigData["IaF_SwitchLeg"])):
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
              cmds.setAttr(crv+".rz", -90)
            else: 
              cmds.setAttr(crv+".rz", 90)
            cmds.setAttr(crv+".scale", 2, 2, 2, type = "double3")
            cmds.makeIdentity(crv, apply = True, t = 0,  r = 1, s = 1, n = 0, pn = True)
            cmds.rename(crv, rigData["IaF_SwitchLeg"][i][3])
            axis = ["x", "y", "z"]
            attrs = ["t", "r", "s"]
            for ax in axis:
              for attr in attrs:
                cmds.setAttr(rigData["IaF_SwitchLeg"][i][3]+"."+attr+ax, l = True, k = False, cb = False)
            cmds.setAttr(rigData["IaF_SwitchLeg"][i][3]+".v", l = True, k = False, cb = False)
            cmds.addAttr(rigData["IaF_SwitchLeg"][i][3], ln = "__________", at = "enum", en = "switchCTRL", k = True)
            cmds.addAttr(rigData["IaF_SwitchLeg"][i][3], shortName="IK_FK", longName="IK_FK", defaultValue=0.0, minValue=0.0, maxValue=1, k=True)
            shape = cmds.listRelatives(rigData["IaF_SwitchLeg"][i][3], children = True)   
            cmds.setAttr(shape[0]+".overrideEnabled", 1)  
            if i == 0:
                cmds.setAttr(shape[0]+".overrideColor", 14)
            else:
                cmds.setAttr(shape[0]+".overrideColor", 13)



    def LegStretchyIK(self):
        for i in range(len(rigData["LegStretchyIK"])):

            shoulder = cmds.xform("IK_"+rigData["LegJoints"][i][0], q=True, ws=True, t=True)
            elbow = cmds.xform("IK_"+rigData["LegJoints"][i][1], q=True, ws=True, t=True)
            wrist = cmds.xform("IK_"+rigData["LegJoints"][i][2], q=True, ws=True, t=True)

            shldDist = cmds.distanceDimension(sp = shoulder, ep = wrist)
            elbowDist = cmds.distanceDimension(sp = shoulder, ep = elbow)
            wristDist = cmds.distanceDimension(sp = elbow, ep = wrist)

            shldDistDim = cmds.listRelatives(shldDist, p=True)
            elbowDistDim = cmds.listRelatives(elbowDist, p=True)
            wristDistDim = cmds.listRelatives(wristDist, p=True)

            shldDistLoc = cmds.listConnections(shldDist)
            elbowDistLoc = cmds.listConnections(elbowDist)
            
            

            cmds.shadingNode("multiplyDivide", asUtility=True, n=rigData["LegStretchyIK"][i][0])
            cmds.shadingNode("multiplyDivide", asUtility=True, n=rigData["LegStretchyIK"][i][1])
            cmds.shadingNode("multiplyDivide", asUtility=True, n=rigData["LegStretchyIK"][i][2])

            cmds.shadingNode("multDoubleLinear", asUtility=True, n=rigData["LegStretchyIK"][i][3])
            cmds.shadingNode("multDoubleLinear", asUtility=True, n=rigData["LegStretchyIK"][i][4])
            cmds.shadingNode("multDoubleLinear", asUtility=True, n=rigData["LegStretchyIK"][i][5])

            cmds.shadingNode("condition", asUtility=True, n=rigData["LegStretchyIK"][i][6])
            cmds.shadingNode("condition", asUtility=True, n=rigData["LegStretchyIK"][i][7])
            cmds.shadingNode("condition", asUtility=True, n=rigData["LegStretchyIK"][i][8])
            cmds.shadingNode("condition", asUtility=True, n=rigData["LegStretchyIK"][i][9])

            cmds.shadingNode("blendTwoAttr", asUtility=True, n=rigData["LegStretchyIK"][i][10])
            cmds.shadingNode("blendTwoAttr", asUtility=True, n=rigData["LegStretchyIK"][i][11])

            cmds.shadingNode("blendColors", asUtility=True, n=rigData["LegStretchyIK"][i][12])
            cmds.shadingNode("blendColors", asUtility=True, n=rigData["LegStretchyIK"][i][13])

            if i == 1:
                cmds.shadingNode("multDoubleLinear", asUtility=True, n=rigData["LegStretchyIK"][i][14])
                cmds.shadingNode("multDoubleLinear", asUtility=True, n=rigData["LegStretchyIK"][i][15])
            else:
                pass
            cmds.setAttr(rigData["LegStretchyIK"][i][0]+".operation", 2)
            cmds.setAttr(rigData["LegStretchyIK"][i][1]+".operation", 2)
            cmds.setAttr(rigData["LegStretchyIK"][i][2]+".operation", 2)

            cmds.setAttr(rigData["LegStretchyIK"][i][6]+".operation", 3)
            cmds.setAttr(rigData["LegStretchyIK"][i][7]+".operation", 3)
            cmds.setAttr(rigData["LegStretchyIK"][i][8]+".operation", 3)
            cmds.setAttr(rigData["LegStretchyIK"][i][9]+".operation", 3)

            cmds.connectAttr(elbowDist+".distance", rigData["LegStretchyIK"][i][0]+".input1X")
            cmds.connectAttr(wristDist+".distance", rigData["LegStretchyIK"][i][1]+".input1X")
            cmds.connectAttr(shldDist+".distance", rigData["LegStretchyIK"][i][2]+".input1X")

            cmds.connectAttr(rigData["LegStretchyIK"][i][3]+".output", rigData["LegStretchyIK"][i][2]+".input2X")
            cmds.connectAttr(rigData["LegStretchyIK"][i][2]+".outputX", rigData["LegStretchyIK"][i][4]+".input1")
            cmds.connectAttr(rigData["LegStretchyIK"][i][2]+".outputX", rigData["LegStretchyIK"][i][5]+".input1")

            cmds.connectAttr(rigData["LegStretchyIK"][i][0]+".outputX", rigData["LegStretchyIK"][i][6]+".colorIfTrueR")
            cmds.connectAttr(rigData["LegStretchyIK"][i][1]+".outputX", rigData["LegStretchyIK"][i][7]+".colorIfTrueR")

            cmds.connectAttr(shldDist+".distance", rigData["LegStretchyIK"][i][8]+".firstTerm")
            cmds.connectAttr(shldDist+".distance", rigData["LegStretchyIK"][i][9]+".firstTerm")
            cmds.connectAttr(rigData["LegStretchyIK"][i][3]+".output", rigData["LegStretchyIK"][i][8]+".secondTerm")
            cmds.connectAttr(rigData["LegStretchyIK"][i][3]+".output", rigData["LegStretchyIK"][i][9]+".secondTerm")
            cmds.connectAttr(rigData["LegStretchyIK"][i][4]+".output", rigData["LegStretchyIK"][i][8]+".colorIfTrueR")
            cmds.connectAttr(rigData["LegStretchyIK"][i][5]+".output", rigData["LegStretchyIK"][i][9]+".colorIfTrueR")

            if i == 1:
                cmds.connectAttr(rigData["LegStretchyIK"][i][6]+".outColorR", rigData["LegStretchyIK"][i][14]+".input1")
                cmds.connectAttr(rigData["LegStretchyIK"][i][7]+".outColorR", rigData["LegStretchyIK"][i][15]+".input1")
                cmds.connectAttr(rigData["LegStretchyIK"][i][14]+".output", rigData["LegStretchyIK"][i][10]+".input[1]")
                cmds.connectAttr(rigData["LegStretchyIK"][i][15]+".output", rigData["LegStretchyIK"][i][11]+".input[1]")
            else:
                cmds.connectAttr(rigData["LegStretchyIK"][i][6]+".outColorR", rigData["LegStretchyIK"][i][10]+".input[1]")
                cmds.connectAttr(rigData["LegStretchyIK"][i][7]+".outColorR", rigData["LegStretchyIK"][i][11]+".input[1]")

            cmds.connectAttr(rigData["LegStretchyIK"][i][8]+".outColorR", rigData["LegStretchyIK"][i][10]+".input[0]")
            cmds.connectAttr(rigData["LegStretchyIK"][i][9]+".outColorR", rigData["LegStretchyIK"][i][11]+".input[0]")

            cmds.connectAttr(rigData["LegStretchyIK"][i][10]+".output", rigData["LegStretchyIK"][i][12]+".color1R")
            cmds.connectAttr(rigData["LegStretchyIK"][i][11]+".output", rigData["LegStretchyIK"][i][13]+".color1R")

            upleg_dist = cmds.getAttr(elbowDist+".distance")
            lowleg_dist = cmds.getAttr(wristDist+".distance")
            upleg_len = cmds.getAttr("IK_"+rigData["LegJoints"][i][1]+".tx")
            lowleg_len = cmds.getAttr("IK_"+rigData["LegJoints"][i][2]+".tx")
            
            cmds.setAttr(rigData["LegStretchyIK"][i][3]+".input1", upleg_dist+lowleg_dist)
            cmds.setAttr(rigData["LegStretchyIK"][i][6]+".secondTerm", 1)
            cmds.setAttr(rigData["LegStretchyIK"][i][7]+".secondTerm", 1)
            cmds.setAttr(rigData["LegStretchyIK"][i][6]+".colorIfFalseR", upleg_len)
            cmds.setAttr(rigData["LegStretchyIK"][i][7]+".colorIfFalseR", lowleg_len)

            cmds.setAttr(rigData["LegStretchyIK"][i][4]+".input2", upleg_len)
            cmds.setAttr(rigData["LegStretchyIK"][i][5]+".input2", lowleg_len)

            cmds.setAttr(rigData["LegStretchyIK"][i][8]+".colorIfFalseR", upleg_len)
            cmds.setAttr(rigData["LegStretchyIK"][i][9]+".colorIfFalseR", lowleg_len)

            cmds.setAttr(rigData["LegStretchyIK"][i][12]+".color2R", upleg_len)
            cmds.setAttr(rigData["LegStretchyIK"][i][13]+".color2R", lowleg_len)
            if i == 1:
                cmds.setAttr(rigData["LegStretchyIK"][i][14]+".input2", -1)
                cmds.setAttr(rigData["LegStretchyIK"][i][15]+".input2", -1)
            
            cmds.connectAttr(rigData["HierarchyOrg"][12]+".CharScale", rigData["LegStretchyIK"][i][3]+".input2")
            cmds.connectAttr(rigData["HierarchyOrg"][12]+".CharScale", rigData["LegStretchyIK"][i][0]+".input2X")
            cmds.connectAttr(rigData["HierarchyOrg"][12]+".CharScale", rigData["LegStretchyIK"][i][1]+".input2X")
            cmds.connectAttr(rigData["HierarchyOrg"][12]+".CharScale", rigData["LegStretchyIK"][i][6]+".firstTerm")
            cmds.connectAttr(rigData["HierarchyOrg"][12]+".CharScale", rigData["LegStretchyIK"][i][7]+".firstTerm")
            
            cmds.rename(shldDistDim, rigData["LegStretchyIK"][i][16])
            cmds.rename(elbowDistDim, rigData["LegStretchyIK"][i][17])
            cmds.rename(wristDistDim, rigData["LegStretchyIK"][i][18])
            cmds.rename(shldDistLoc[0], rigData["LegStretchyIK"][i][19])
            cmds.rename(elbowDistLoc[1], rigData["LegStretchyIK"][i][20])
            cmds.rename(shldDistLoc[1], rigData["LegStretchyIK"][i][21])
            cmds.connectAttr(rigData["LegStretchyIK"][i][12]+".outputR", "IK_"+rigData["LegJoints"][i][1]+".tx")
            cmds.connectAttr(rigData["LegStretchyIK"][i][13]+".outputR", "IK_"+rigData["LegJoints"][i][2]+".tx")
            
            
            cmds.pointConstraint(rigData["IK_LegList"][i][0], rigData["LegStretchyIK"][i][21])
            cmds.pointConstraint(rigData["IK_LegList"][i][4], rigData["LegStretchyIK"][i][20])
            
            cmds.connectAttr(rigData["IK_LegList"][i][4]+".ElbowPin", rigData["LegStretchyIK"][i][10]+".attributesBlender")
            cmds.connectAttr(rigData["IK_LegList"][i][4]+".ElbowPin", rigData["LegStretchyIK"][i][11]+".attributesBlender")
            cmds.connectAttr(rigData["IK_LegList"][i][0]+".Stretch", rigData["LegStretchyIK"][i][12]+".blender")
            cmds.connectAttr(rigData["IK_LegList"][i][0]+".Stretch", rigData["LegStretchyIK"][i][13]+".blender")
            if i == 0:
                ctrlGRP = cmds.group(em = True, p = rigData["HierarchyOrg"][8] ,name = rigData["HierarchyOrg"][15])
            else:
                ctrlGRP = cmds.group(em = True, p = rigData["HierarchyOrg"][8] ,name = rigData["HierarchyOrg"][16])
                
            cmds.parent(rigData["LegStretchyIK"][i][16], ctrlGRP)
            cmds.parent(rigData["LegStretchyIK"][i][17], ctrlGRP)
            cmds.parent(rigData["LegStretchyIK"][i][18], ctrlGRP)
            cmds.parent(rigData["LegStretchyIK"][i][19], ctrlGRP)
            cmds.parent(rigData["LegStretchyIK"][i][20], ctrlGRP)
            cmds.parent(rigData["LegStretchyIK"][i][21], ctrlGRP)


    def IaF_leg_switch(self):
        for i in range(len(rigData["IaF_SwitchLeg"])):
            for o in range(len(rigData["IaF_SwitchLeg"][i][:3])):
                pairB = cmds.shadingNode("pairBlend", asUtility=True, n=rigData["IaF_SwitchLeg"][i][o])
                cmds.connectAttr("IK_"+rigData["LegJoints"][i][o]+".translate", pairB+".inTranslate1")
                cmds.connectAttr("FK_"+rigData["LegJoints"][i][o]+".translate", pairB+".inTranslate2")
                cmds.connectAttr("IK_"+rigData["LegJoints"][i][o]+".rotate", pairB+".inRotate1")
                cmds.connectAttr("FK_"+rigData["LegJoints"][i][o]+".rotate", pairB+".inRotate2")
                cmds.connectAttr(pairB+".outTranslate", "bn_"+rigData["LegJoints"][i][o]+".translate")
                cmds.connectAttr(pairB+".outRotate", "bn_"+rigData["LegJoints"][i][o]+".rotate")
                cmds.connectAttr(rigData["IaF_SwitchLeg"][i][3]+".IK_FK", pairB+".weight")
                cmds.connectAttr(rigData["IaF_SwitchLeg"][i][3]+".IK_FK", rigData["FK_LegList"][i][0::2][o]+".visibility")

            cmds.setDrivenKeyframe(rigData["IK_LegList"][i][0]+".v", rigData["IK_LegList"][i][4]+".v", cd = rigData["IaF_SwitchLeg"][i][3]+".IK_FK")
            cmds.setAttr(rigData["IaF_SwitchLeg"][i][3]+".IK_FK", 1)
            cmds.setAttr(rigData["IK_LegList"][i][4]+".v", 0)
            cmds.setAttr(rigData["IK_LegList"][i][0]+".v", 0)
            cmds.setDrivenKeyframe(rigData["IK_LegList"][i][0]+".v", rigData["IK_LegList"][i][0]+".v", cd = rigData["IaF_SwitchLeg"][i][3]+".IK_FK")
    



     
