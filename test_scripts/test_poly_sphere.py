import maya.cmds as cmds

# Create a sphere, with 10 subdivisions in the X direction,
# and 15 subdivisions in the Y direction,
# the radius of the sphere is 20.
# sphere1 = cmds.polySphere(sx=10, sy=15, r=20)

# Create a sphere, called "mySphere", on each direction there are 5 subdivisions.
sphere2 = cmds.polySphere(n='mySphere', sx=5, sy=5)
print(sphere2)

# Query the radius of the new sphere
# r = cmds.polySphere( 'mySphere', q=True, sx=True )
