import gurobipy as gp

m = gp.Model()

x1 = m.addVar(vtype=gp.GRB.INTEGER, name="X1")
x2 = m.addVar(vtype=gp.GRB.INTEGER, name="X2")
x3 = m.addVar(vtype=gp.GRB.INTEGER, name="X3")
x4 = m.addVar(vtype=gp.GRB.INTEGER, name="X4")
x5 = m.addVar(vtype=gp.GRB.INTEGER, name="X5")
x6 = m.addVar(vtype=gp.GRB.INTEGER, name="X6")
x7 = m.addVar(vtype=gp.GRB.INTEGER, name="X7")
x8 = m.addVar(vtype=gp.GRB.INTEGER, name="X8")
x9 = m.addVar(vtype=gp.GRB.INTEGER, name="X9")
x10 = m.addVar(vtype=gp.GRB.INTEGER, name="X10")
x11 = m.addVar(vtype=gp.GRB.INTEGER, name="X11")
x12 = m.addVar(vtype=gp.GRB.INTEGER, name="X12")
x13 = m.addVar(vtype=gp.GRB.INTEGER, name="X13")
x14 = m.addVar(vtype=gp.GRB.INTEGER, name="X14")
x15 = m.addVar(vtype=gp.GRB.INTEGER, name="X15")
x16 = m.addVar(vtype=gp.GRB.INTEGER, name="X16")
x17 = m.addVar(vtype=gp.GRB.INTEGER, name="X17")
x18 = m.addVar(vtype=gp.GRB.INTEGER, name="X18")
x19 = m.addVar(vtype=gp.GRB.INTEGER, name="X19")
x20 = m.addVar(vtype=gp.GRB.INTEGER, name="X20")
x21 = m.addVar(vtype=gp.GRB.INTEGER, name="X21")
x22 = m.addVar(vtype=gp.GRB.INTEGER, name="X22")
x23 = m.addVar(vtype=gp.GRB.INTEGER, name="X23")
x24 = m.addVar(vtype=gp.GRB.INTEGER, name="X24")
x25 = m.addVar(vtype=gp.GRB.INTEGER, name="X25")
x26 = m.addVar(vtype=gp.GRB.INTEGER, name="X26")
x27 = m.addVar(vtype=gp.GRB.INTEGER, name="X27")
x28 = m.addVar(vtype=gp.GRB.INTEGER, name="X28")
x29 = m.addVar(vtype=gp.GRB.INTEGER, name="X29")
x30 = m.addVar(vtype=gp.GRB.INTEGER, name="X30")
x31 = m.addVar(vtype=gp.GRB.INTEGER, name="X31")
x32 = m.addVar(vtype=gp.GRB.INTEGER, name="X32")
x33 = m.addVar(vtype=gp.GRB.INTEGER, name="X33")
x34 = m.addVar(vtype=gp.GRB.INTEGER, name="X34")
x35 = m.addVar(vtype=gp.GRB.INTEGER, name="X35")
x36 = m.addVar(vtype=gp.GRB.INTEGER, name="X36")
x37 = m.addVar(vtype=gp.GRB.INTEGER, name="X37")
x38 = m.addVar(vtype=gp.GRB.INTEGER, name="X38")
x39 = m.addVar(vtype=gp.GRB.INTEGER, name="X39")
x40 = m.addVar(vtype=gp.GRB.INTEGER, name="X40")
x41 = m.addVar(vtype=gp.GRB.INTEGER, name="X41")
x42 = m.addVar(vtype=gp.GRB.INTEGER, name="X42")
x43 = m.addVar(vtype=gp.GRB.INTEGER, name="X43")
x44 = m.addVar(vtype=gp.GRB.INTEGER, name="X44")
x45 = m.addVar(vtype=gp.GRB.INTEGER, name="X45")
x46 = m.addVar(vtype=gp.GRB.INTEGER, name="X46")
x47 = m.addVar(vtype=gp.GRB.INTEGER, name="X47")
x48 = m.addVar(vtype=gp.GRB.INTEGER, name="X48")
x49 = m.addVar(vtype=gp.GRB.INTEGER, name="X49")
x50 = m.addVar(vtype=gp.GRB.INTEGER, name="X50")
x51 = m.addVar(vtype=gp.GRB.INTEGER, name="X51")
x52 = m.addVar(vtype=gp.GRB.INTEGER, name="X52")
x53 = m.addVar(vtype=gp.GRB.INTEGER, name="X53")
x54 = m.addVar(vtype=gp.GRB.INTEGER, name="X54")
x55 = m.addVar(vtype=gp.GRB.INTEGER, name="X55")
x56 = m.addVar(vtype=gp.GRB.INTEGER, name="X56")
x57 = m.addVar(vtype=gp.GRB.INTEGER, name="X57")
x58 = m.addVar(vtype=gp.GRB.INTEGER, name="X58")
x59 = m.addVar(vtype=gp.GRB.INTEGER, name="X59")
x60 = m.addVar(vtype=gp.GRB.INTEGER, name="X60")
x61 = m.addVar(vtype=gp.GRB.INTEGER, name="X61")
x62 = m.addVar(vtype=gp.GRB.INTEGER, name="X62")
x63 = m.addVar(vtype=gp.GRB.INTEGER, name="X63")
x64 = m.addVar(vtype=gp.GRB.INTEGER, name="X64")

chessboard = [
    [x1, x2, x3, x4, x5, x6, x7, x8],
    [x9, x10, x11, x12, x13, x14, x15, x16],
    [x17, x18, x19, x20, x21, x22, x23, x24],
    [x25, x26, x27, x28, x29, x30, x31, x32],
    [x33, x34, x35, x36, x37, x38, x39, x40],
    [x41, x42, x43, x44, x45, x46, x47, x48],
    [x49, x50, x51, x52, x53, x54, x55, x56],
    [x57, x58, x59, x60, x61, x62, x63, x64],
]

#m.setObjective(8 * x1 + 11 * x2 + 15 * x3, gp.GRB.MAXIMIZE)

for row in chessboard:
    m.addConstr(sum(row) == 1)

for column in zip(*chessboard):
    m.addConstr(sum(column) == 1)

for i1, row1 in enumerate(chessboard):
    for j1, cell1 in enumerate(row1):
        for i2, row2 in enumerate(chessboard):
            for j2, cell2 in enumerate(row2):
                if abs(i1 - i2) == abs(j1 - j2):
                    pass # TODO: figure out how to model diagonals
                    #m.addConstr(cell1 + cell2 <= 1)


# Solve it!
m.optimize()

#print(f"Optimal objective value: {m.objVal}")

print(f"{x1.X }, {x2.X }, {x3.X }, {x4.X }, {x5.X }, {x6.X }, {x7.X }, {x8.X }")
print(f"{x9.X }, {x10.X}, {x11.X}, {x12.X}, {x13.X}, {x14.X}, {x15.X}, {x16.X}")
print(f"{x17.X}, {x18.X}, {x19.X}, {x20.X}, {x21.X}, {x22.X}, {x23.X}, {x24.X}")
print(f"{x25.X}, {x26.X}, {x27.X}, {x28.X}, {x29.X}, {x30.X}, {x31.X}, {x32.X}")
print(f"{x33.X}, {x34.X}, {x35.X}, {x36.X}, {x37.X}, {x38.X}, {x39.X}, {x40.X}")
print(f"{x41.X}, {x42.X}, {x43.X}, {x44.X}, {x45.X}, {x46.X}, {x47.X}, {x48.X}")
print(f"{x49.X}, {x50.X}, {x51.X}, {x52.X}, {x53.X}, {x54.X}, {x55.X}, {x56.X}")
print(f"{x57.X}, {x58.X}, {x59.X}, {x60.X}, {x61.X}, {x62.X}, {x63.X}, {x64.X}")
