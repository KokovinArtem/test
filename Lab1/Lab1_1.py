#gmsh.model.geo.addCircle(p1, center, p2)

import gmsh
import sys
import math
from array import *


curve_it = 0
lc = 1e-1

def horcircledots (centerx, centery, rad, z, it):
    dot_it = it * 4
    dot_it += 1
    gmsh.model.geo.addPoint (centerx - rad, centery, z, lc, dot_it)
    dot_it += 1
    gmsh.model.geo.addPoint (centerx, centery + rad, z, lc, dot_it)
    dot_it += 1
    gmsh.model.geo.addPoint (centerx + rad, centery, z, lc, dot_it)
    dot_it += 1
    gmsh.model.geo.addPoint (centerx, centery - rad, z, lc, dot_it)




gmsh.initialize()

gmsh.model.add("Torus")

gmsh.model.geo.addPoint(0, 0, 0, lc, 100)
gmsh.model.geo.addPoint(0, 0, .5, lc, 101)
gmsh.model.geo.addPoint(0, 0, -.5, lc, 102)



horcircledots(0, 0, 3, 0, 0)

horcircledots(0, 0, 2.5, 0, 1)

horcircledots(0, 0, 3.5, 0, 3)

horcircledots(0, 0, 3, 0.5, 2)

horcircledots(0, 0, 3, -0.5, 4)

for j in range (4):
    for i in range (4):
        if j == 0 or j == 2:
            gmsh.model.geo.addCircleArc((j + 1)*4 + i + 1, 100, (j + 1)*4 + (i + 1) % 4 + 1, (j) * 4 + i + 1)
        if j == 1:
            gmsh.model.geo.addCircleArc((j + 1)*4 + i + 1, 101, (j + 1)*4 + (i + 1) % 4 + 1, (j) * 4 + i + 1)
        if j == 3:
            gmsh.model.geo.addCircleArc((j + 1)*4 + i + 1, 102, (j + 1)*4 + (i + 1) % 4 + 1, (j) * 4 + i + 1)

for i in range (4):
    for j in range (4):
        gmsh.model.geo.addCircleArc((j + 1) * 4 + i + 1, i + 1, ((j + 1) % 4) * 4 + 4 + i + 1, (j) * 4 + i + 1 + 16)


#for i in range (4):
    #for j in range (4):
        #gmsh.model.geo.addCurveLoop([j * 4 + i + 1, i + 1 + 16, - ((j + 1) % 4) * 4 + i + 1, - (j)*4 + i + 1 + 16, - ((j + 2) % 4) * 4 + i + 1], j*4 + i + 1)

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(2)

gmsh.write("t3.msh")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()