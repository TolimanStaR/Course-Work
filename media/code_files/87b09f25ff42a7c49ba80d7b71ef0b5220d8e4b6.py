import math
D, Rad, Orb = map(int, input().split())
MBKS_cor = (-Orb, 0)
cos_alpha = 1 - (D**2)/(Orb**2)/2
alpha = math.acos(cos_alpha)
sin_alpha = math.sin(alpha)
Linal_1_cor = (-cos_alpha*Orb, sin_alpha*Orb)

centre = ((Linal_1_cor[0] + MBKS_cor[0])/2, (Linal_1_cor[1] + MBKS_cor[1])/2)
if abs(centre[0]) < Rad and abs(centre[1]) < Rad:
    print("Trouble")
else:
    print("Escape")


