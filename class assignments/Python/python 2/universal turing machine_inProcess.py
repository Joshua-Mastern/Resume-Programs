from __future__ import print_function
import json
import sys

def run_utm(
        state = 'q0',
        blank = ' ',
        rules = [],
        tape = [],
        halt = 'qdone',
        pos = 0):
    st = state
    if not tape: tape = [blank]
    if pos < 0: pos += len(tape)
    if pos >= len(tape) or pos < 0: raise Error( "bad init position")
    while True:
        if st == halt:
            print("HALTED:\n", end="")
            print("The inputted string is accepted\n" ,end="")
            break
        print(st, '\t', end=" ")
        for i, v in enumerate(tape):
            if i == pos: print("[%s]" % (v,), end=" ")
            else: print(v, end=" ")
        print()

        #if (st, tape[pos]) not in rules: break

        #assign values according to rules
        try:
            v1 = rules[st][tape[pos]]["write"]
        except:
            print ("HALTED:\nThe inputted string is not accepted\n", end="")
            break
        dr = rules[st][tape[pos]]["move"]
        s1 = rules[st][tape[pos]]["nextState"]
        tape[pos] = v1 #write new value
        if dr == 'left':
            if pos > 0: pos -= 1
            else: tape.insert(0, blank)
        if dr == 'right':
            pos += 1
            if pos >= len(tape): tape.append(blank) 
        st = s1
    

# EXAMPLES
nameOfTm = sys.argv[1]
with open(nameOfTm) as f:
   descr = json.load(f)

while(True):
    inputTape = input("\nEnter the tape contents for the turing machine. ")
    tape = list(inputTape)
    run_utm( tape = tape, rules = descr)
