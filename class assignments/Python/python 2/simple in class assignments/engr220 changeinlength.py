########
#Engr220 Elongation calculator

force = 0.0
area = 0.0
length = 0.0
elasticity = 10600
lengthChng = 0.0
while(True):
        mode = input("1 for force change, 2 for area change, 3 for length change ")
        if(mode ==1):
                force = input("tpye force ")
        elif (mode ==2):
                area = input("type area ")
        elif (mode ==3):
                length = input("type length ")

        if(elasticity*area!=0):
                lengthChng = force*length/(elasticity*area)

        print "Change in length is {}, force is {}, area is {}, length is {}, elasticity is {} ".format(round(lengthChng, 3), force, area, length, elasticity)
