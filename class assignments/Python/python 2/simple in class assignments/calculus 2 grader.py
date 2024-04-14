############################################
#CALCULUS 2 grade experimenter             #
#                                          #
############################################

def calculate (letterGrade):
        grades = {"a":90, "b":80, "c": 70, "d":60, "f":0}
        soFar = test1*0.2 + hw*0.1
        need = grades[letterGrade] - soFar
        avg = need/0.7
        print "I need {} more points to get an {}".format(need, letterGrade)
        print "I need to average {} on all my remaining tests, to get a(n) {} in the course.".format(avg, letterGrade)
        
test1 = 68.4615385
test2 = None
test3 = None
test4 = None

hw = 100

while(True):
        answer = raw_input("What grade do you want to get?")

        if(answer == "a" or answer == "b" or answer == "c"):
                calculate(answer)
        elif (answer == "exit"):
                break
        else:
                print "I don't deal with stuff like that."
