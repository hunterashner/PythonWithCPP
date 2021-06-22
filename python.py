import re
import string


def printsomething():
    print("Hello from python!")

def PrintMe(v):
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    return v * v

    #multiplies user entered values for each number in the for range
def MultiplicationTable(v):
    for i in range(1, 10):
        print((v-48), " * ", i, "= ", (v-48)*i)

    #doubles the user entered value
def DoubleValue(v):
    print((v-48) * (v-48))