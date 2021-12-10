# Use of lambda  : Method 4

import math

#Input:
# L : Beam Span,[m]
# W: Total Design Line Load(DL + LL),[kN/m]


#OutPut:

# BM:Beam Bending Moment: kN/m

BendingMoment_UDL = lambda W,L: "%.2f"%(W*L**2/8)
#BendingMoment_UDL = lambda W,L:math.ceil(W*L**2/8)


print(BendingMoment_UDL(4.3,7))


#"%.3f"%()

#math.floor(x)
#math.ceil(x)       
#math.floor(1.2)
#math.ceil(1.2)
#"%.2f"%()
