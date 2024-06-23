h1 = float(input("Input the height of the 1st ball: "))
m1 = float(input("Input the mass of the 1st ball: "))
m2 = float(input("Input the mass of the 2nd ball: "))

u1 = m1*9.8*h1
Vs = (2*u1/m1)**0.5	

V2 = 2*m1/(m1+m2)*Vs

print("The velocity of the 1st ball after slidez: ",Vs)
print("The velocity of the 2st ball after collision: ",V2)