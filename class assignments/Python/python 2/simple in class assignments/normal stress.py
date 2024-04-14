########
#Engr220 Normal Stress calculator

force = 0.0
area = 0.0
stress = 0.0
while(True):
        mode = input("1 for force change, 2 for area change")
        if(mode ==1):
                force = input("tpye force ")
        elif (mode ==2):
                area = input("type area ")

        if(area!=0):
                stress = force/area

        print "Stress is {}, force is {}, area is {}".format(round(stress, 3), force, area)
