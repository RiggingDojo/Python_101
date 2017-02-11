'''
Rhonda Ray

Description:  creates different shapes for controls

'''

import pymel.core as pm 

def circle(self, ctrlName):
	ctrl = pm.circle(name=ctrlName, normal=(1,0,0), center=(0,0,0), radius=1.5, constructionHistory=False)


def square(self, ctrlName):
	ctrl = pm.curve(name=ctrlName, degree=1, point=[(1.25, 0, 0), (0, 0, 0), (0, 0, 1.25), (1.25, 0, 1.25), (1.25, 0, 0)], knot=[0, 1, 2, 3, 4])
	pm.xform(scale=(1.5, 1.5, 1.5), rotation=(0, 0, 90), preserve=True, centerPivots=True)
	pm.makeIdentity(apply=True, translate=True, rotate=True, scale=True, normal=False, preserveNormals=True) 
	

def text(self, txt, ctrlName):
	ctrl = pm.textCurves(name=ctrlName, font='Courier', text=txt)

	# get curves
	nurbsShapes = pm.ls(pm.listRelatives(ctrl, allDescendents=True), type='nurbsCurve')

	# parent shapes to a single transform
	for letter in nurbsShapes:
	    nurbsTransforms = pm.listRelatives(letter, parent=True)[0]
	    nurbsTransforms = pm.parent(nurbsTransforms, world=True)
	    pm.makeIdentity(nurbsTransforms, apply=True, translate=True, rotate=True, scale=True, normal=False)

	    pm.parent(letter, ctrl[0], relative=True, shape=True)
	    pm.delete(nurbsTransforms)

	# delete unused transforms
	txtChildren = pm.listRelatives(ctrl, children=True, type='transform')
	if txtChildren:
		pm.delete(txtChildren)


return ctrl