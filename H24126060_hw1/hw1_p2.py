F = float(input("Input the force:"))          #F是將input的字串化為浮點數
m1 = float(input("Input the mass of m1:"))    #m1是將input的字串化為浮點數	
r = float(input("Input the distance:"))		  #r是將input的字串化為浮點數

m2 = F/(6.67*(10**-11))*(r**2)/m1			  #求m2即為把F，m1，r的數值套入universal gravitation的公式中

E2 = m2*(299792458**2)						  #求E2即為m2乘以C的平方	

print("The mass of m2 =",m2)				  #打出m2的值
print("The energy of m2 =",E2)				  #打出E2的值

