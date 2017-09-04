import maya.cmds as cmds
rigData = {}
rigData["ArmJoints"]=[
                      ["lf_shoulder_JNT", "lf_elbow_JNT", "lf_wrist_JNT"],
                      ["rt_shoulder_JNT", "rt_elbow_JNT", "rt_wrist_JNT"]
                      ]
rigData["FingerJoints"] = [["lf_pinky_fing_JNT_01", "lf_pinky_fing_JNT_02" , "lf_pinky_fing_JNT_03", "lf_pinky_fing_JNT_04", "lf_pinkyEnd_fing_JNT",
							"lf_ring_fing_JNT_01", "lf_ring_fing_JNT_02", "lf_ring_fing_JNT_03", "lf_ring_fing_JNT_04", "lf_ringEnd_fing_JNT",
							"lf_middle_fing_JNT_01", "lf_middle_fing_JNT_02", "lf_middle_fing_JNT_03", "lf_middle_fing_JNT_04", "lf_middleEnd_fing_JNT",
							"lf_point_fing_JNT_01", "lf_point_fing_JNT_02", "lf_point_fing_JNT_03", "lf_point_fing_JNT_04", "lf_pointEnd_fing_JNT",
							"lf_thumb_fing_JNT_01", "lf_thumb_fing_JNT_02", "lf_thumb_fing_JNT_03", "lf_thumbEnd_fing_JNT", "lf_wristBase_JNT" ],
							["rt_pinky_fing_JNT_01", "rt_pinky_fing_JNT_02" , "rt_pinky_fing_JNT_03", "rt_pinky_fing_JNT_04", "rt_pinkyEnd_fing_JNT",
							"rt_ring_fing_JNT_01", "rt_ring_fing_JNT_02", "rt_ring_fing_JNT_03", "rt_ring_fing_JNT_04", "rt_ringEnd_fing_JNT",
							"rt_middle_fing_JNT_01", "rt_middle_fing_JNT_02", "rt_middle_fing_JNT_03", "rt_middle_fing_JNT_04", "rt_middleEnd_fing_JNT",
							"rt_point_fing_JNT_01", "rt_point_fing_JNT_02", "rt_point_fing_JNT_03", "rt_point_fing_JNT_04", "rt_pointEnd_fing_JNT",
							"rt_thumb_fing_JNT_01", "rt_thumb_fing_JNT_02", "rt_thumb_fing_JNT_03", "rt_thumbEnd_fing_JNT", "rt_wristBase_JNT"]]

rigData["OrientFingerJoints"] = [[orient_lf_pinky_JNT]]
rigData["FingerPositions"] =  [[
					 #Pinky finger position
					 [40.55310942676585, 79.79846251826041, -3.568153414688018], [45.649525152069174, 75.40344289370071, -5.502497164321938],  [49.4594535424784, 70.02029486457198, -6.992340022065515],
					 [51.43805438300248, 66.579654145339, -7.779520908459524], [52.55821033299307, 63.78340319129973, -8.24288126058131],
					 #Ring finger position
					 [41.4865835616865, 78.99694309670801, -2.0761787778216387], [46.499994018892686, 75.412897556997, -2.8666746568454817],  [51.38722980513151, 69.37721712237699, -3.4117443677349835],
					 [54.06673858055266, 65.16337564923695, -3.6303178428481653], [55.97065447418994, 61.97861112031937, -3.768709982947997],
					 #Middle finger position
					 [41.86214846784703, 78.41444484433484, 0.28166705661428765], [47.11933641507468, 75.07941538620673, 0.5205155277235708],  [53.382430260997985, 69.35827288050227, 0.8841230314926976],
					 [57.35719576006904, 65.01145584547127, 1.147263118285252], [59.740276321355175, 61.62208144554866, 1.3404532306823458],
					 #Point finger position
					 [40.697602405541225, 78.81174272689951, 2.2795405816271948], [46.77853712126624, 75.32497467281438, 3.5664241328101896],  [52.301720284222355, 69.93520871679095, 4.968685014223203],
					 [55.504905709753885, 65.98208555306607, 5.868804377859389], [57.693775889506654, 62.96937017902901, 6.516590922836407],
					 #Thumb finger position
					 [39.86817960177429, 80.40977593508809, 1.8175510577848157], [41.37853328888797, 76.95432064879245, 5.2847920633299585], 
					 [42.60654091478241, 71.28784039516177, 9.118510007967839], [42.9455601015601, 66.64147516930633, 11.271451914337453]],
					 
					 
					 #Pinky finger position
					 [[-40.55310942676585, 79.79846251826041, -3.568153414688018], [-45.649525152069174, 75.40344289370071, -5.502497164321938],  [-49.4594535424784, 70.02029486457198, -6.992340022065515],
					 [-51.43805438300248, 66.579654145339, -7.779520908459524], [-52.55821033299307, 63.78340319129973, -8.24288126058131],
					 #Ring finger position
					 [-41.4865835616865, 78.99694309670801, -2.0761787778216387], [-46.499994018892686, 75.412897556997, -2.8666746568454817],  [-51.38722980513151, 69.37721712237699, -3.4117443677349835],
					 [-54.06673858055266, 65.16337564923695, -3.6303178428481653], [-55.97065447418994, 61.97861112031937, -3.768709982947997],
					 #Middle finger position
					 [-41.86214846784703, 78.41444484433484, 0.28166705661428765], [-47.11933641507468, 75.07941538620673, 0.5205155277235708],  [-53.382430260997985, 69.35827288050227, 0.8841230314926976],
					 [-57.35719576006904, 65.01145584547127, 1.147263118285252], [-59.740276321355175, 61.62208144554866, 1.3404532306823458],
					 #Point finger position
					 [-40.697602405541225, 78.81174272689951, 2.2795405816271948], [-46.77853712126624, 75.32497467281438, 3.5664241328101896],  [-52.301720284222355, 69.93520871679095, 4.968685014223203],
					 [-55.504905709753885, 65.98208555306607, 5.868804377859389], [-57.693775889506654, 62.96937017902901, 6.516590922836407],
					 #Thumb finger position
					 [-39.86817960177429, 80.40977593508809, 1.8175510577848157], [-41.37853328888797, 76.95432064879245, 5.2847920633299585], 
					 [-42.60654091478241, 71.28784039516177, 9.118510007967839], [-42.9455601015601, 66.64147516930633, 11.271451914337453]]]



def finger_createJnt(jntType):
    for i in range(len(rigData["FingerJoints"])):
            for o in range(len(rigData["FingerJoints"][i])):
            	if o!=24:
	                cmds.joint(n=jntType+rigData["FingerJoints"][i][o], p=rigData["FingerPositions"][i][o])
	                cmds.select(cl=True)
                else:
                	pos = cmds.xform(rigData["ArmJoints"][i][0], q=True, piv=True, ws=True)
                	cmds.joint(n=jntType+rigData["FingerJoints"][i][o], p=pos)

def finger_orientJoint(jntType):
    for i in range(len(rigData["FingerJoints"])):
        for o in range(len(rigData["FingerJoints"][i])):
            if o==5 or o==10 or o==15 or o==20 or o==24:
                pass
            else:		        
                loc = cmds.spaceLocator()
                cmds.parent(loc[0], jntType+rigData["FingerJoints"][i][o-1])
                cmds.setAttr(loc[0]+".translate", 0, -5, 0, type = "double3")
                cmds.parent(loc[0], w=True)
                vecList = ([1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0])
                if o==0:
                	if i==0
                		cmds.aimConstraint(jntType+rigData["FingerJoints"][i][5], jntType+rigData["FingerJoints"][i][10], jntType+rigData["FingerJoints"][i][o-1], offset = [0, 0, 0], weight = True, aimVector = vecList[0] ,
		                                                 upVector = vecList[2], worldUpType = "object" , worldUpObject = loc[0])
                	else:
                		cmds.aimConstraint(jntType+rigData["FingerJoints"][i][5], jntType+rigData["FingerJoints"][i][10], jntType+rigData["FingerJoints"][i][o-1], offset = [0, 0, 0], weight = True, aimVector = vecList[1] ,
		                                                 upVector = vecList[3], worldUpType = "object" , worldUpObject = loc[0])
		        if o!=0: 
                	if i==0:	
                    	cmds.aimConstraint(jntType+rigData["FingerJoints"][i][o], jntType+rigData["FingerJoints"][i][o-1], offset = [0, 0, 0], weight = True, aimVector = vecList[0] ,
		                                                 upVector = vecList[2], worldUpType = "object" , worldUpObject = loc[0])
                	else:
                    	cmds.aimConstraint(jntType+rigData["FingerJoints"][i][o+1], jntType+rigData["FingerJoints"][i][o-1], offset = [0, 0, 0], weight = True, aimVector = vecList[1] ,
		                                                 upVector = vecList[3], worldUpType = "object" , worldUpObject = loc[0])
                cmds.delete(jntType+rigData["FingerJoints"][i][o-1]+"_aimConstraint1")
                cmds.makeIdentity(jntType+rigData["FingerJoints"][i][o-1], apply = True, t = 0,  r = 1, s = 0, n = 0, pn = True)
                cmds.delete(loc[0])
def finger_cleanJntOrient(jntType):
    for i in range(len(rigData["FingerJoints"])):
        for o in range(len(rigData["FingerJoints"][i])):
            if o==4 or o==9 or o==14 or o==19 or o==23:
                cmds.parent(jntType+rigData["FingerJoints"][i][o], jntType+rigData["FingerJoints"][i][o-1])
                cmds.setAttr(jntType+rigData["FingerJoints"][i][o]+".jointOrient", 0, 0, 0, type = "double3")
                cmds.setAttr(jntType+rigData["FingerJoints"][i][o]+".ty", 0)
                cmds.setAttr(jntType+rigData["FingerJoints"][i][o]+".tz", 0)  
            elif o==0 or o==5 or o==10 or o==15 or o==20:
                cmds.parent(jntType+rigData["FingerJoints"][i][o], jntType+rigData["FingerJoints"][i][24])
            elif o==24:
            	pass
            else:
                cmds.parent(jntType+rigData["FingerJoints"][i][o], jntType+rigData["FingerJoints"][i][o-1])
                cmds.setAttr(jntType+rigData["FingerJoints"][i][1]+".jointOrientX", 0)
                cmds.setAttr(jntType+rigData["FingerJoints"][i][1]+".jointOrientY", 0)
                cmds.setAttr(jntType+rigData["FingerJoints"][i][1]+".ty", 0)
                cmds.setAttr(jntType+rigData["FingerJoints"][i][1]+".tz", 0)

finger_createJnt("bn_")
finger_orientJoint("bn_")
finger_cleanJntOrient("bn_")