"""
Meshing the Omega aka. BERT logo
================================

This is an example illustrating the possibility to hand over matplotlib path
objects to the TriangleWrapper.
"""

import matplotlib.pyplot as plt
import matplotlib.textpath
import pygimli as pg

###############################################################################
# We start by generating a matplotlib path respresenting the :math:`\Omega`
# character.

logo_path = matplotlib.textpath.TextPath((0,0), '$\Omega$', size=1)
patch = matplotlib.patches.PathPatch(logo_path)

###############################################################################
# The vertices of the path are defined as mesh nodes and connected with edges.

nodes = patch.get_verts() * 50
poly = pg.Mesh(2)

for node in nodes:
    poly.createNode(node[0], node[1], 0.0)

for i in range(poly.nodeCount() - 1):
    poly.createEdge(poly.node(i), poly.node(i + 1))

poly.createEdge(poly.node(poly.nodeCount() - 1), poly.node(0))

###############################################################################
# We call the TriangleWrapper to generate the mesh and set the x values as the
# data for a color transition.

tri = pg.TriangleWrapper(poly)
mesh = pg.Mesh(2)
tri.setSwitches('-pzeAfa5q31')
tri.generate(mesh)

data = []
for cell in mesh.cells():
    data.append(cell.center().x())

fig, ax = plt.subplots()
ax.axis('off')
ax.text(3.5, -10, 'BERT', fontsize=80, fontweight='bold')
pg.show(mesh, data, axes=ax, cmap='RdBu', logScale=False, showLater=True)
pg.show(mesh, axes=ax)
ax.set_ylim(-10, mesh.ymax())
