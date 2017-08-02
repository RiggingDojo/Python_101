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
    arrowV* = 0.5
    finalV = arrowV + midV
    return ([finalV.x, finalV.y, finalV.z])