import system.utils as utils 

fileName = 'C:/Users/rhondaray/Documents/GitHub/Python_101_S2_2015/layout/data.json'

rig_data = {}
rig_data['bodyPlacement'] = ['lt_', 'rt_']
rig_data['jntType'] = ['ik_', 'fk_', 'rig_', 'bind_']
rig_data['armJnts']	= ['shoulder_jnt', 'elbow_jnt', 'wrist_jnt', 'wristEND_jnt']
rig_data['armIKCtrls']	= ['ctrl_ikWrist', 'ikh_arm', 'ctrl_PV_arm', 'ctrl_ikHand']
rig_data['armFKCtrls']	= ['ctrl_fkShoulder', 'ctrl_fkElbow', 'ctrl_fkWrist']
rig_data['armGrps'] = ['grp_ctrl_ikWrist', 'grp_ctrl_fkShoulder', 'grp_ctrl_fkElbow', 'grp_ctrl_fkWrist', 'grp_arm']
rig_data['armPos'] = [[-7, 0, 2], [-1, 0, 0], [4, 0, 2], [7, 0, 3]]

utils.writeJson(fileName, rig_data)

inputData = utils.readJson(fileName)