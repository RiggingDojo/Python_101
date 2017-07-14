import maya.cmds as cmds
print cmds.joint("bn_rt_wrist_JNT", p=True, q=True)
#Creating bind left joints
cmds.joint(n="bn_lf_shoulder_JNT", p = [9.585747308067395, 118.83508463054183, -0.7054197788238525])
cmds.joint(n="bn_lf_elbow_JNT", p = [23.04832620389858, 101.66094761326656, -3.0123116805935153])
cmds.joint(n="bn_lf_wrist_JNT", p = [37.67443141283351, 82.99575130827552, -0.766004046678499])
cmds.joint(n="orient_JNT", p = [59.84439659118652, 61.86297798156738, 1.300861120223999])
cmds.parent("orient_JNT", w = True) 
cmds.select(d=True)

#Creating IK left joints
cmds.joint(n="IK_lf_shoulder_JNT", p = [9.585747308067395, 118.83508463054183, -0.7054197788238525])
cmds.joint(n="IK_lf_elbow_JNT", p = [23.04832620389858, 101.66094761326656, -3.0123116805935153])
cmds.joint(n="IK_lf_wrist_JNT", p = [37.67443141283351, 82.99575130827552, -0.766004046678499])
cmds.select(d=True)

#Creating FK left joints
cmds.joint(n="FK_lf_shoulder_JNT", p = [9.585747308067395, 118.83508463054183, -0.7054197788238525])
cmds.joint(n="FK_lf_elbow_JNT", p = [23.04832620389858, 101.66094761326656, -3.0123116805935153])
cmds.joint(n="FK_lf_wrist_JNT", p = [37.67443141283351, 82.99575130827552, -0.766004046678499])
cmds.select(d=True)

########################################################################################################################

#Unparent bind elbow and wrist for future orienting
cmds.parent("bn_lf_elbow_JNT", w=True)
cmds.parent("bn_lf_wrist_JNT", w=True)

#Orient bind left shoulder
cmds.spaceLocator()
cmds.parent("locator1", "bn_lf_shoulder_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("bn_lf_elbow_JNT", "bn_lf_shoulder_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("bn_lf_shoulder_JNT_aimConstraint1")
cmds.makeIdentity("bn_lf_shoulder_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Orient bind left elbow
cmds.parent("locator1", "bn_lf_elbow_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("bn_lf_wrist_JNT", "bn_lf_elbow_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("bn_lf_elbow_JNT_aimConstraint1")
cmds.makeIdentity("bn_lf_elbow_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Orient bind left wrist
cmds.parent("locator1", "bn_lf_wrist_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("orient_JNT", "bn_lf_wrist_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("bn_lf_wrist_JNT_aimConstraint1")
cmds.makeIdentity("bn_lf_wrist_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Parent back bind arm
cmds.parent("bn_lf_elbow_JNT", "bn_lf_shoulder_JNT")
cmds.parent("bn_lf_wrist_JNT", "bn_lf_elbow_JNT")

#Making sure that bind arm is straight for IK to work properly 
cmds.setAttr("bn_lf_elbow_JNT.jointOrientX", 0)
cmds.setAttr("bn_lf_elbow_JNT.jointOrientY", 0)

#A little bit not sure about next one
"""This one can look weird, but I am using actual model to build an arm and my model hand oriented a little bit off , so I will leave untouched 
Y and Z so wrist will be oriented to the hand , I am newbie rigger also so if I am doing something wrong please tell me :)"""
cmds.setAttr("bn_lf_wrist_JNT.jointOrientX", 0)

########################################################################################################################


#Unparent IK elbow and wrist for future orienting
cmds.parent("IK_lf_elbow_JNT", w=True)
cmds.parent("IK_lf_wrist_JNT", w=True)

#Orient IK left shoulder
cmds.parent("locator1", "IK_lf_shoulder_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("IK_lf_elbow_JNT", "IK_lf_shoulder_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("IK_lf_shoulder_JNT_aimConstraint1")
cmds.makeIdentity("IK_lf_shoulder_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Orient IK left elbow
cmds.parent("locator1", "IK_lf_elbow_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("IK_lf_wrist_JNT", "IK_lf_elbow_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("IK_lf_elbow_JNT_aimConstraint1")
cmds.makeIdentity("IK_lf_elbow_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Orient IK left wrist
cmds.parent("locator1", "IK_lf_wrist_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("orient_JNT", "IK_lf_wrist_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("IK_lf_wrist_JNT_aimConstraint1")
cmds.makeIdentity("IK_lf_wrist_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Parent back IK arm
cmds.parent("IK_lf_elbow_JNT", "IK_lf_shoulder_JNT")
cmds.parent("IK_lf_wrist_JNT", "IK_lf_elbow_JNT")

#Making sure that IK arm is straight for IK to work properly 
cmds.setAttr("IK_lf_elbow_JNT.jointOrientX", 0)
cmds.setAttr("IK_lf_elbow_JNT.jointOrientY", 0)
cmds.setAttr("IK_lf_wrist_JNT.jointOrientX", 0)

########################################################################################################################

#Unparent FK elbow and wrist for future orienting
cmds.parent("FK_lf_elbow_JNT", w=True)
cmds.parent("FK_lf_wrist_JNT", w=True)

#Orient FK left shoulder
cmds.parent("locator1", "FK_lf_shoulder_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("FK_lf_elbow_JNT", "FK_lf_shoulder_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("FK_lf_shoulder_JNT_aimConstraint1")
cmds.makeIdentity("FK_lf_shoulder_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Orient FK left elbow
cmds.parent("locator1", "FK_lf_elbow_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("FK_lf_wrist_JNT", "FK_lf_elbow_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("FK_lf_elbow_JNT_aimConstraint1")
cmds.makeIdentity("FK_lf_elbow_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Orient FK left wrist
cmds.parent("locator1", "FK_lf_wrist_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("orient_JNT", "FK_lf_wrist_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("FK_lf_wrist_JNT_aimConstraint1")
cmds.makeIdentity("FK_lf_wrist_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Parent back FK arm
cmds.parent("FK_lf_elbow_JNT", "FK_lf_shoulder_JNT")
cmds.parent("FK_lf_wrist_JNT", "FK_lf_elbow_JNT")

#Making sure that FK arm is straight for IK to work properly 
cmds.setAttr("FK_lf_elbow_JNT.jointOrientX", 0)
cmds.setAttr("FK_lf_elbow_JNT.jointOrientY", 0)
cmds.setAttr("FK_lf_wrist_JNT.jointOrientX", 0)

########################################################################################################################
# Making right Side 
########################################################################################################################

cmds.mirrorJoint("bn_lf_shoulder_JNT", mirrorYZ = True, mirrorBehavior = True, searchReplace = ("_lf_", "_rt_"))







import maya.cmds as cmds
print cmds.joint("bn_rt_wrist_JNT", p=True, q=True)
#Creating bind left joints
cmds.joint(n="bn_lf_shoulder_JNT", p = [9.585747308067395, 118.83508463054183, -0.7054197788238525])
cmds.joint(n="bn_lf_elbow_JNT", p = [23.04832620389858, 101.66094761326656, -3.0123116805935153])
cmds.joint(n="bn_lf_wrist_JNT", p = [37.67443141283351, 82.99575130827552, -0.766004046678499])
cmds.joint(n="orient_JNT", p = [59.84439659118652, 61.86297798156738, 1.300861120223999])
cmds.parent("orient_JNT", w = True) 
cmds.select(d=True)

#Creating IK left joints
cmds.joint(n="IK_lf_shoulder_JNT", p = [9.585747308067395, 118.83508463054183, -0.7054197788238525])
cmds.joint(n="IK_lf_elbow_JNT", p = [23.04832620389858, 101.66094761326656, -3.0123116805935153])
cmds.joint(n="IK_lf_wrist_JNT", p = [37.67443141283351, 82.99575130827552, -0.766004046678499])
cmds.select(d=True)

#Creating FK left joints
cmds.joint(n="FK_lf_shoulder_JNT", p = [9.585747308067395, 118.83508463054183, -0.7054197788238525])
cmds.joint(n="FK_lf_elbow_JNT", p = [23.04832620389858, 101.66094761326656, -3.0123116805935153])
cmds.joint(n="FK_lf_wrist_JNT", p = [37.67443141283351, 82.99575130827552, -0.766004046678499])
cmds.select(d=True)

########################################################################################################################

#Unparent bind elbow and wrist for future orienting
cmds.parent("bn_lf_elbow_JNT", w=True)
cmds.parent("bn_lf_wrist_JNT", w=True)

#Orient bind left shoulder
cmds.spaceLocator()
cmds.parent("locator1", "bn_lf_shoulder_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("bn_lf_elbow_JNT", "bn_lf_shoulder_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("bn_lf_shoulder_JNT_aimConstraint1")
cmds.makeIdentity("bn_lf_shoulder_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Orient bind left elbow
cmds.parent("locator1", "bn_lf_elbow_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("bn_lf_wrist_JNT", "bn_lf_elbow_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("bn_lf_elbow_JNT_aimConstraint1")
cmds.makeIdentity("bn_lf_elbow_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Orient bind left wrist
cmds.parent("locator1", "bn_lf_wrist_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("orient_JNT", "bn_lf_wrist_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("bn_lf_wrist_JNT_aimConstraint1")
cmds.makeIdentity("bn_lf_wrist_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Parent back bind arm
cmds.parent("bn_lf_elbow_JNT", "bn_lf_shoulder_JNT")
cmds.parent("bn_lf_wrist_JNT", "bn_lf_elbow_JNT")

#Making sure that bind arm is straight for IK to work properly 
cmds.setAttr("bn_lf_elbow_JNT.jointOrientX", 0)
cmds.setAttr("bn_lf_elbow_JNT.jointOrientY", 0)

#A little bit not sure about next one
"""This one can look weird, but I am using actual model to build an arm and my model hand oriented a little bit off , so I will leave untouched 
Y and Z so wrist will be oriented to the hand , I am newbie rigger also so if I am doing something wrong please tell me :)"""
cmds.setAttr("bn_lf_wrist_JNT.jointOrientX", 0)

########################################################################################################################


#Unparent IK elbow and wrist for future orienting
cmds.parent("IK_lf_elbow_JNT", w=True)
cmds.parent("IK_lf_wrist_JNT", w=True)

#Orient IK left shoulder
cmds.parent("locator1", "IK_lf_shoulder_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("IK_lf_elbow_JNT", "IK_lf_shoulder_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("IK_lf_shoulder_JNT_aimConstraint1")
cmds.makeIdentity("IK_lf_shoulder_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Orient IK left elbow
cmds.parent("locator1", "IK_lf_elbow_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("IK_lf_wrist_JNT", "IK_lf_elbow_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("IK_lf_elbow_JNT_aimConstraint1")
cmds.makeIdentity("IK_lf_elbow_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Orient IK left wrist
cmds.parent("locator1", "IK_lf_wrist_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("orient_JNT", "IK_lf_wrist_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("IK_lf_wrist_JNT_aimConstraint1")
cmds.makeIdentity("IK_lf_wrist_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Parent back IK arm
cmds.parent("IK_lf_elbow_JNT", "IK_lf_shoulder_JNT")
cmds.parent("IK_lf_wrist_JNT", "IK_lf_elbow_JNT")

#Making sure that IK arm is straight for IK to work properly 
cmds.setAttr("IK_lf_elbow_JNT.jointOrientX", 0)
cmds.setAttr("IK_lf_elbow_JNT.jointOrientY", 0)
cmds.setAttr("IK_lf_wrist_JNT.jointOrientX", 0)

########################################################################################################################

#Unparent FK elbow and wrist for future orienting
cmds.parent("FK_lf_elbow_JNT", w=True)
cmds.parent("FK_lf_wrist_JNT", w=True)

#Orient FK left shoulder
cmds.parent("locator1", "FK_lf_shoulder_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("FK_lf_elbow_JNT", "FK_lf_shoulder_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("FK_lf_shoulder_JNT_aimConstraint1")
cmds.makeIdentity("FK_lf_shoulder_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Orient FK left elbow
cmds.parent("locator1", "FK_lf_elbow_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("FK_lf_wrist_JNT", "FK_lf_elbow_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("FK_lf_elbow_JNT_aimConstraint1")
cmds.makeIdentity("FK_lf_elbow_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Orient FK left wrist
cmds.parent("locator1", "FK_lf_wrist_JNT")
cmds.setAttr("locator1.translate", 0, 0, 5, type = "double3")
cmds.parent("locator1", w=True)
cmds.aimConstraint("orient_JNT", "FK_lf_wrist_JNT", offset = [0, 0, 0], weight = True, aimVector = [1, 0, 0] , 
                                             upVector = [0, 1, 0], worldUpType = "object" , worldUpObject = "locator1")
cmds.delete("FK_lf_wrist_JNT_aimConstraint1")
cmds.makeIdentity("FK_lf_wrist_JNT", apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)

#Parent back FK arm
cmds.parent("FK_lf_elbow_JNT", "FK_lf_shoulder_JNT")
cmds.parent("FK_lf_wrist_JNT", "FK_lf_elbow_JNT")

#Making sure that FK arm is straight for IK to work properly 
cmds.setAttr("FK_lf_elbow_JNT.jointOrientX", 0)
cmds.setAttr("FK_lf_elbow_JNT.jointOrientY", 0)
cmds.setAttr("FK_lf_wrist_JNT.jointOrientX", 0)

########################################################################################################################
# Making right Side 
########################################################################################################################

cmds.mirrorJoint("bn_lf_shoulder_JNT", mirrorYZ = True, mirrorBehavior = True, searchReplace = ("_lf_", "_rt_"))







