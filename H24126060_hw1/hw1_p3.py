p = float(input("Input velocity "))/299792458  #p是input後字串的浮點數除以光速 也等於對於光速的百分比
r = 1/((1-p**2)**0.5)					       #r是套p進Einstein's equation後得出的值

td_alpha = 4.309		
td_barnard = 6.0
td_betelgeuse = 309
td_andromeda = 2000000

tp_alpha = td_alpha/r 						 #此四行為Einstein's equation下人在船中旅行的時間
tp_barnard = td_barnard/r
tp_betelgeuse = td_betelgeuse/r
tp_andromeda = td_andromeda/r

print("Percentage of light speed =",p)
print("Travel time to Alpha Centauri =",tp_alpha)
print("Travel time to Barnard's Star =",tp_barnard)
print("Travel time to Betelgeuse (in the Milky Way) =",tp_betelgeuse)
print("Travel time to Andromeda Galaxy (closest galaxy) =",tp_andromeda)