#Homework #3
#Ryan Andrews : CS 3500 Section A
#
# Recursive Descent Parser
####################################
import sys

keywords = ["is", "=", "+", "-", "*", "/", "or", "and", "~", "(", ")", "<", ">", "!", "forward", "rotate", "if", "endif", "else", "while", "endw", "prog", "blip", "blorp"]
token = ""
symbols = []
list_pos = 0
num_symbols = 0
def getToken():
    global token
    global symbols
    global list_pos
    if (list_pos < num_symbols):
        token = symbols[list_pos]
        list_pos += 1
    else:
        return False
    #print ("Got Token ", token);

def isKeyword():
    #print("\t\t   isKeyword")
    if (token in keywords):
        return True
    else:
        return False

def isIdentifier():
    #print("\t\t   isIdentifier")
    if (not isKeyword()):
        l = len(token)
        if (token[0].isalpha()):
            for i in range(1, l):
                if (not token[i].isalnum()):
                    #print("\tIdentifier: ", token, " contains non alpha-numeric character ", token[i], "!")
                    return False
                    break
        else:
            #print("\tIdentifier: ", token, " doesn't start with character!");
            return False
    else:
        #print("\tIdentifier: ", token, " is a keyword!")
        return False
    return True

def isInteger():
    #print("\t\t   isInteger")
    newT = token
    if (newT[0] == "+"):
        newT = newT.replace("+", "")
    elif (newT[0] == "-"):
        newT = newT.replace("-", "")
    if (newT.find(".") > -1):
        return False
    return (newT.isnumeric())

def isDecimal():
    #print("\t\t   isDecimal")
    newT = token
    if (newT.find(".") == -1):
        return False
    else:
        pos = newT.find(".")
        return (isInteger(newT[0:pos]) and isInteger(newT[pos+1:]))

# START SYMBOL
def RoutineSequence():
    #print("\t\t RoutineSequence")
    if (RoutineDeclaration()):
        getToken()
        while (RoutineDeclaration()):
            getToken()
    else:
        #print("\tRoutineSequence: Expected RoutineDeclaration! ", token)
        return False
    return True

def RoutineDeclaration():
    #print("\t\t  RoutineDeclaration")
    if (token == "prog"):
        getToken()
        if (isIdentifier()):
            getToken()
            if (token == "blip"):
                getToken()
                StatementSequence()
                if (token == "blorp"):
                    return True
                else:
                    #print("\tRoutineDeclaration: Expected blorp! ", token)
                    return False
            else:
                #print("\tRoutineDeclaration: Expected blip! ", token)
                return False
        else:
            #print("\tRoutineDeclaration: Expected identifier! ", token)
            return False
    else:
        #print("\tRoutineDeclaration: Expected prog! ", token)
        return False

def StatementSequence():
    #print("\t\t StatementSequence")
    if (Statement()):
        getToken()
        while (Statement()):
            getToken()
        return True
    else:
        return False

def Statement():
    #print("\t\t Statement")
    if (Assignment() or IfStatement() or LoopStatement() or FwdStatement() or RotStatement()):
        return True
    else:
        #print("Statement: Expected Assignment, IfStatement, LoopStatement, FwdStatement, or RotStatement! ", token)
        return False

def Assignment():
    #print("\t\t Assignment")
    if (isIdentifier()):
        getToken()
        if (token == "is"):
            getToken()
            if (Expression()):
                #getToken()
                if (token == "!"):
                    return True
                else:
                    #print("\tAssignment: Expected !! ", token)
                    return False
            else:
                #print("\tAssignment: Expected Expression! ", token)
                return False
        else:
            #print("\tAssignment: Expected is! ", token)
            return False
    else:
        #print("\tAssignment: Expected identifier! ", token)
        return False

def IfStatement():
    #print("\t\t IfStatement")
    if (token == "if"):
        getToken()
        if (token == "("):
            getToken()
            if (Expression()):
                #getToken()
                if (token == ")"):
                    getToken()
                    if (StatementSequence()):
                        pass
                    if (token == "else"):
                        getToken()
                        if (StatementSequence()):
                            pass
                    if (token == "endif"):
                        return True
                    else:
                        #print("\tIfStatement: Expected endif! ", token)
                        return False
                else:
                    #print("\tIfStatement: Expected )! ", token)
                    return False
            else:
                #print("\tIfStatement: Expected Expression! ", token)
                return False
        else:
            #print("\tIfStatement: Expected (! ", token)
            return False
    else:
        #print("\tIfStatement: Expected if! ", token)
        return False

def LoopStatement():
    #print("\t\t LoopStatement")
    if (token == "while"):
        getToken()
        if (token == "("):
            getToken()
            if (Expression()):
                #getToken()
                if (token == ")"):
                    getToken()
                    if (StatementSequence()):
                        #getToken()
                        if (token == "endw"):
                            return True
                        else:
                            #print("\tLoopStatement: Expected endw! ", token)
                            return False
                    else:
                        #print("\tLoopStatement: Expected StatementSequence! ", token)
                        return False
                else:
                    #print("\tLoopStatement: Expected )! ", token)
                    return False
            else:
                #print("\tLoopStatement: Expected Expression! ", token)
                return False
        else:
            #print("\tLoopStatement: Expected (! ", token)
            return False
    else:
        #print("\tLoopStatement: Expected while! ", token)
        return False

def FwdStatement():
    #print("\t\t FwdStatement")
    if (token == "forward"):
        getToken()
        if (token == "("):
            getToken()
            if (Expression()):
                #getToken()
                if (token == ")"):
                    getToken()
                    if (token == "!"):
                        return True
                    else:
                        #print("\tFwdStatement: Expected !! ", token)
                        return False
                else:
                    #print("\tFwdStatement: Expected )! ", token)
                    return False
            else:
                #print("\tFwdStatement: Expected Expression! ", token)
                return False
        else:
            #print("\tFwdStatement: Expected (! ", token)
            return False
    else:
        #print("\tFwdStatement: Expected forward! ", token)
        return False

def RotStatement():
    #print("\t\t RotStatement")
    if (token == "rotate"):
        getToken()
        if (token == "("):
            getToken()
            if (Expression()):
                #getToken()
                if (token == ")"):
                    getToken()
                    if (token == "!"):
                        return True
                    else:
                        #print("\tRotStatement: Expected !! ", token)
                        return False
                else:
                    #print("\tRotStatement: Expected )! ", token)
                    return False
            else:
                #print("\tRotStatement: Expected Expression! ", token)
                return False
        else:
            #print("\tRotStatement: Expected (! ", token)
            return False
    else:
        #print("\tRotStatement: Expected rotate! ", token)
        return False

def Expression():
    #print("\t\t Expression")
    if (SimpleExpression()):
        if (Relation()): #Optional
            getToken()
            if (SimpleExpression()): #Optional
                pass
            else:
                #print("\tExpression: Expected Relation->SimpleExpression! ", token)
                return False
    else:
        #print("\tExpression: Expected SimpleExpression! ", token)
        return False
    return True

def SimpleExpression():
    #print("\t\t SimpleExpression")
    if (Term()):
        while (AddOperator()):
            getToken()
            if (Term()):
                pass
            else:
                #print("\tSimpleExpression: Expected AddOperator->Term! ", token)
                return False
        return True
    else:
        #print("\tSimpleExpression: Expected Term! ", token)
        return False
    #return True

def Term():
    #print("\t\t Term")
    if (Factor()):
        getToken()
        while (MulOperator()):
            getToken()
            if (Factor()):
                getToken()
            else:
                #print("\tTerm: Expected MulOperator->Factor! ", token)
                return False
    else:
        #print("\tTerm: Expected Factor! ", token)
        return False
    return True

def Factor():
    #print("\t\t Factor")
    if (isInteger() or isDecimal() or isIdentifier()):
        return True
    elif (token == "("):
        getToken()
        if (Expression()):
            #getToken()
            if (token == ")"):
                return True
            else:
                #print("\tFactor: Expected )! ", token)
                return False
        else:
            #print("\tFactor: Expected Expression! ", token)
            return False
    elif (token == "~"):
        getToken()
        if (Factor()):
            return True
        else:
            #print("\tFactor: Expected Factor! ", token)
            return False
    else:
        #print("\tFactor: Expected Integer, Decimal, Identifier, ( Expression ), or ~ Factor! ", token)
        return False

def Relation():
    #print("\t\t Relation")
    if (token == "<" or token == ">" or token == "=" or token == "#"):
        return True
    else:
        #print("\tRelation: Expected <, >, =, or #! ", token)
        return False

def AddOperator():
    #print("\t\t AddOperator")
    if (token == "+" or token == "-" or token == "or"):
        return True
    else:
        #print("\tAddOperator: Expected +, -, or or! ", token)
        return False

def MulOperator():
    #print("\t\t MulOperator")
    if (token == "*" or token == "/" or token == "and"):
        return True
    else:
        #print("\tMulOperator: Expected *, /, or and! ", token)
        return False

def main():
    global symbols
    global num_symbols
    s = ""

    for line in sys.stdin:
        s += line.strip()
        s += " "

    symbols = s.split(" ")
    num_symbols = len(symbols)
    #print(symbols)

    getToken()
    if (RoutineSequence()):
        print("CORRECT")
    else:
        print("INVALID!")


main()