###############
#Interpelator
#
#
############

#get three values that are from known middle
        #earlyKnown
        #middleKnown
        #lateKnown
while(True):
        earlyKnown = input("earlyKnown: ")
        middleKnown = input("middleKnown: ")
        lateKnown = input("lateKnown: ")
        #get two values that the third is between
                #ealyMyst
                #unknown
                #lateNMyst
        earlyMyst = input("earlyMyst: ")
        lateMyst = input("lateMyst: ")
        #unknown

        #math
        percentageKnown = float(middleKnown-earlyKnown)/(lateKnown-earlyKnown)
       
        unknown = percentageKnown*(lateMyst-earlyMyst)+earlyMyst

        print unknown
        
