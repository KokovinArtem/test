from dolfin import *

# Create mesh and define function space
mesh = UnitSquareMesh(32, 32)
V = FunctionSpace(mesh, "Lagrange", 1)

# Define Dirichlet boundary (x = 0 or x = 1)
def boundary(x):
    return x[0] < DOLFIN_EPS or x[0] > 1.0 - DOLFIN_EPS or x[1] < DOLFIN_EPS or x[1] > 1.0 - DOLFIN_EPS

# Define boundary condition
u0 = Expression('1/(pow(pow(x[0]-0.5,2) + pow(x[1]-0.5,2), 0.5))', degree = 2)
bc = DirichletBC(V, u0, boundary)

# Define variational problem
u = TrialFunction(V)
v = TestFunction(V)
f = Expression("((abs(x[1] - 0.5) < 0.3) && ((abs(x[1] - 0.5) > 0.1))) &&((abs(x[0] - 0.5) < 0.3) && ((abs(x[0] - 0.5) > 0.1)))  ? 4*pi : 0", degree = 0)
#g = Expression("sin(5*x[0])", degree=2)
a = inner(grad(u), grad(v))*dx
L = f*v*dx
# Compute solution
u = Function(V)
solve(a == L, u, bc)

# Save solution in VTK format
file = File("poisson/poisson.pvd")
file << u

# Plot solution
import matplotlib.pyplot as plt
plot(u)
plt.show()
