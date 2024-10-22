#Tinh chu vi va dien tich hinh tron

import math

#Nhap ban kinh hinh tron
r=float (input("Ban kinh hinh tron la r ="))

#Dieu kien xac dinh cua r>0
if r>0:
    #Chu vi hinh tron
    C=2*math.pi*r
    #Dien tich hinh tron
    S=2*math.pi*r*r
    #in ket qua ra man hinh
    print("Chu vi hinh tron la ", C)
    print("Dien tich hinh tron la", S)
else:
    print("r khong thoa man dieu kien lon hon 0")
    

