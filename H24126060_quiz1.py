richter = float(input("Please imput a Richter scale value: ")) #輸入芮氏值

energy = 10**(1.5*richter+4.8)   #焦耳換算

TNT = energy/(4.184*(10**9))    #換算炸彈的量
lunches = energy/2930200        #換算營養午餐的量

print("Richter scale value: ",richter)   #此四行輸出答案
print("Equivalence in Joules: ",energy)
print("Equivalence in tons of TNT ",TNT)
print("Equivalence in the number of nutritious lunches: ",lunches)