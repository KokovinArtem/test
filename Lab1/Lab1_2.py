
import gmsh
import math
import os
import sys

gmsh.initialize()
path = os.path.dirname(os.path.abspath(__file__))
gmsh.merge(os.path.join(path, 'VDV.stl'))

gmsh.model.mesh.classifySurfaces(40 * math.pi / 100., True,
                                 True,
                                 180 * math.pi / 100.)

s = gmsh.model.getEntities(2)
l = gmsh.model.geo.addSurfaceLoop([s[i][1] for i in range(len(s))])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()
#gmsh.model.geo.synchronize()

# We specify element sizes imposed by a size field, just because we can :-)
funny = False
f = gmsh.model.mesh.field.add("MathEval")

if funny:
    gmsh.model.mesh.field.setString(f, "F", "2*Sin((x+y)/5) + 6")
else:
    gmsh.model.mesh.field.setString(f, "F", "10")

gmsh.model.mesh.field.setAsBackgroundMesh(f)

gmsh.model.mesh.generate(3)
gmsh.write('VDV.msh')

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()