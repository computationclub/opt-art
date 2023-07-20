# Solve the following MIP:
#  maximize
#        8 * X1 + 11 * X2 + 15 * X3
#  subject to
#        2 * X1 + 2 * X2 + 2 * X3 <= 25
#        1 * X1 + 2 * X2 + 3 * X3 <= 19
#        X1, X2, X3 >= 0

import gurobipy as gp

# Create a new model
m = gp.Model()

# Create variables
x1 = m.addVar(vtype=gp.GRB.INTEGER, name="X1")
x2 = m.addVar(vtype=gp.GRB.INTEGER, name="X2")
x3 = m.addVar(vtype=gp.GRB.INTEGER, name="X3")

# Set objective function
m.setObjective(8 * x1 + 11 * x2 + 15 * x3, gp.GRB.MAXIMIZE)

# Add constraints
m.addConstr(2 * x1 + 2 * x2 + 2 * x3 <= 25)
m.addConstr(x1 + 2 * x2 + 3 * x3 <= 19)
m.addConstr(x1 >= 0)
m.addConstr(x2 >= 0)
m.addConstr(x3 >= 0)

# Solve it!
m.optimize()

print(f"Optimal objective value: {m.objVal}")
print(f"Solution values: x={x1.X}, y={x2.X}, z={x3.X}")
