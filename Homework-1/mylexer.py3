#Homework #1
#Ryan Andrews : CS 3500 Section A
#
# My First Lexical Analyzer
# To have it read a file, type on the command line "python hw1.py3 input.txt"
####################################
import sys

def ishex(str):
    if (str == "A" or str == "B" or str == "C" or str == "D" or str == "E" or str == "F" or str.isdigit()):
        return True
    else:
        return False
####################################
# recognize: Takes an input string and returns true if the string
#            is in the grammar that is coded, False otherwise
####################################
def recognize(line):
    k = 0 # The current position in 'line'
    state = 1 # The current state in the automota
    Type = "INVALID!"
    while k < len(line):
        #print("\t", state, "---", line[k])
        if (state == 1):
            if (line[k] == "+" or line[k] == "-"): state = 2
            elif (line[k] == "("): state = 23
            elif (line[k].isdigit()): state = 3
            elif (line[k] == "w"): state = 36
            elif (line[k] == "e"): state = 41
            elif (line[k] == "p"): state = 47
            elif (line[k].isalpha()): state = 52
            else: return Type
        elif (state == 2):
            if (line[k].isdigit()): state = 6
            else: return Type
        elif (state == 3):
            if (line[k] == "."): state = 22
            elif(line[k].isdigit()): state = 4
            elif (ishex(line[k])): state = 17
            else: return Type
        elif (state == 4):
            if (line[k].isdigit()): state = 5
            elif (line[k] == "."): state = 22
            elif (ishex(line[k])): state = 17
            else: return Type
        elif (state == 5):
            if (line[k].isdigit()): state = 6
            elif (line[k] == "."): state = 8
            elif (line[k] == "-"): state = 27
            elif (ishex(line[k])): state = 17
            else: return Type
        elif (state == 6):
            if (line[k].isdigit()): state = 6
            elif (ishex(line[k])): state = 17
            elif (line[k] == "."): state = 22
            elif (line[k] == "H"): state = 21
            else: return Type
        elif (state == 7):
            if (line[k].isdigit()): state = 7
            elif (line[k] == "E"): state = 18
            else: return Type
        elif (state == 8):
            if (line[k].isdigit()): state = 9
            else: return Type
        elif (state == 9):
            if (line[k] == "E"): state = 18
            elif (line[k].isdigit()): state = 10
            else: return Type
        elif (state == 10):
            if (line[k] == "E"): state = 18
            elif (line[k].isdigit()): state = 11
            else: return Type
        elif (state == 11):
            if (line[k] == "E"): state = 18
            elif (line[k] == "."): state = 12
            elif (line[k].isdigit()): state = 7
            else: return Type
        elif (state == 12):
            if (line[k].isdigit()): state = 13
            else: return Type
        elif (state == 13):
            if (line[k].isdigit()): state = 14
            else: return Type
        elif (state == 14):
            if (line[k].isdigit()): state = 15
            else: return Type
        elif (state == 15):
            if (line[k].isdigit()): state = 16
            else: return Type
        elif (state == 16):
            return Type
        elif (state == 17):
            if (ishex(line[k])): state = 17
            elif (line[k] == "H"): state = 53
            else: return False
        elif (state == 18):
            if (line[k] == "-"): state = 20
            elif (line[k].isdigit()): state = 19
            else: return Type
        elif (state == 19):
            if (line[k].isdigit()): state = 19
            else: return Type
        elif (state == 20):
            if (line[k].isdigit()): state = 19
            else: return Type
        elif (state == 21):
            return Type
        elif (state == 22):
            if (line[k].isdigit()): state = 7
            else: return Type
        elif (state == 23):
            if (line[k].isdigit()): state = 24
            else: return Type
        elif (state == 24):
            if (line[k].isdigit()): state = 25
            else: return Type
        elif (state == 25):
            if (line[k].isdigit()): state = 26
            else: return Type
        elif (state == 26):
            if (line[k] == ")"): state = 27
            else: return Type
        elif (state == 27):
            if (line[k].isdigit()): state = 28
            else: return Type
        elif (state == 28):
            if (line[k].isdigit()): state = 29
            else: return Type
        elif (state == 29):
            if (line[k].isdigit()): state = 30
            else: return Type
        elif (state == 30):
            if (line[k] == "-"): state = 12
            else: return Type
        elif (state == 36):
            if (line[k] == "h"): state = 37
            elif (not ishex(line[k])): state = 54
            elif (line[k].isalnum() or line[k] == "_"): state = 52
            else: return Type
        elif (state == 37):
            if (line[k] == "i"): state = 38
            elif (not ishex(line[k])): state = 54
            elif (line[k].isalnum() or line[k] == "_"): state = 52
            else: return Type
        elif (state == 38):
            if (line[k] == "l"): state = 39
            elif (not ishex(line[k])): state = 54
            elif (line[k].isalnum() or line[k] == "_"): state = 52
            else: return Type
        elif (state == 39):
            if (line[k] == "e"): state = 40
            elif (not ishex(line[k])): state = 54
            elif (line[k].isalnum() or line[k] == "_"): state = 52
            else: return Type
        elif (state == 40):
            if (not ishex(line[k])): state = 54
            elif (line[k].isalnum() or line[k] == "_"): state = 52
            else: return Type
        elif (state == 41):
            if (line[k] == "l"): state = 42
            elif (line[k] == "n"): state = 45
            elif (not ishex(line[k])): state = 54
            elif (line[k].isalnum() or line[k] == "_"): state = 52
            else: return Type
        elif (state == 42):
            if (line[k] == "s"): state = 43
            elif (not ishex(line[k])): state = 54
            elif (line[k].isalnum() or line[k] == "_"): state = 52
            else: return Type
        elif (state == 43):
            if (line[k] == "e"): state = 44
            elif (not ishex(line[k])): state = 54
            elif (line[k].isalnum() or line[k] == "_"): state = 52
            else: return Type
        elif (state == 44):
            if (not ishex(line[k])): state = 54
            elif (line[k].isalnum() or line[k] == "_"): state = 52
            else: return Type
        elif (state == 45):
            if (line[k] == "d"): state = 46
            elif (not ishex(line[k])): state = 54
            elif (line[k].isalnum() or line[k] == "_"): state = 52
            else: return Type
        elif (state == 46):
            if (not ishex(line[k])): state = 54
            elif (line[k].isalnum() or line[k] == "_"): state = 52
            else: return Type
        elif (state == 47):
            if (line[k] == "r"): state = 48
            elif (not ishex(line[k])): state = 54
            elif (line[k].isalnum() or line[k] == "_"): state = 52
            else: return Type
        elif (state == 48):
            if (line[k] == "i"): state = 49
            elif (not ishex(line[k])): state = 54
            elif (line[k].isalnum() or line[k] == "_"): state = 52
            else: return Type
        elif (state == 49):
            if (line[k] == "n"): state = 50
            elif (not ishex(line[k])): state = 54
            elif (line[k].isalnum() or line[k] == "_"): state = 52
            else: return Type
        elif (state == 50):
            if (line[k] == "t"): state = 51
            elif (not ishex(line[k])): state = 54
            elif (line[k].isalnum() or line[k] == "_"): state = 52
            else: return Type
        elif (state == 51):
            if (not ishex(line[k])): state = 54
            elif (line[k].isalnum() or line[k] == "_"): state = 52
            else: return Type
        elif (state == 52):
            if (line[k] == "H"): state = 53
            elif (not ishex(line[k])): state = 54
            elif (line[k].isalnum() or line[k] == "_"): state = 52
            else: return Type
        elif (state == 53):
            return Type
        elif (state == 54):
            if (line[k].isalnum() or line[k] == "_"): state = 54
            else: return Type
        else:
            return Type
        k = k+1
    if (state == 3 or state == 4 or state == 5 or state == 17 or state == 6):
        Type = "Integer."
    elif (state == 53):
        Type = "Hexadecimal."
    elif (state == 9 or state == 10 or state == 11 or state == 7 or state == 21):
        Type = "Decimal."
    elif (state == 19):
        Type = "Scientific."
    elif (state == 16):
        Type = "Phone."
    elif (state == 44 or state == 46 or state == 40 or state == 51):
        Type = "Keyword."
    elif (state == 52 or state == 54):
        Type = "Identifier."
    else:
        Type = "INVALID!"

    return Type



def main():
    i = 0
    for line in sys.stdin:
        print(i, ": ", recognize(line.strip()))
        i = i+1
    return



main()
