#CISC6525 AI HW5 
#Zhen Guo
#Bayesian Network
#4/26/2016

import math
def evaljointbayes(fname):
    """Print out the answers for all questions"""
    #read file and save lines to contents
    contents = []
    f = open(fname)
    for line in f:
        randomVar = line.rstrip().split()
        if randomVar[0] != 'END':
            contents.append(randomVar)
    print("1. Read file", fname, "successfully.")
    f.close()
    
    #count numbers of nodes and probabilities in each line
    length = len(contents)
    nodes, prob = [0] * length, [0] * length
    table = []                     
    for num in range(0, length):
        tableline = []
        for i in contents[num]:
            try:
                j = float(i)
                prob[num] += 1
                tableline.append(j) 
            except ValueError:
                if i != 'NONE':
                    nodes[num] += 1 
        table.append(tableline)      
    
    #print out the joint distribution formular
    print("2. The joint distribution using this network is:")
    nodelist = []
    for line in contents:
        nodelist.append(line[0])
    print("P(", printElement(nodelist), ") = ")
    for num in range(0, length):
        line = contents[num]
        if  nodes[num] == 1:
            print("P(", line[0], ")", end = "")
        else: 
            print("P(", line[0], '|', printElement(line[1:nodes[num]]),\
             ")", end = "")
        if num == length - 1:
            print(' ')
        else: 
            print(' * ', end = "")

    #print out the full joint distribution table 
    for n in range(int(math.pow(2, length)) - 1, -1, -1): #all possible elements in table
        input = bin(n).lstrip("0b") #generate the T/F list
        if len(input) < length: #make the input list 5 digit string
            input = "0" * (length - len(input)) + input
        #calculate the probability result for one input
        result = 1
        for num in range(0, length):
            if  nodes[num] == 1: #node has no parents
                result = multiply(result, input[num], table[num], 0)     
            else: #node has parents
                counter = 0
                parent = contents[num][1: nodes[num]]            
                for i in range(0, nodes[num] - 1):
                    if input[nodelist.index(parent[i])] == '0': #one parent is false
                        counter = counter + math.pow(2, nodes[num] - 2 - i)
                result = multiply(result, input[num], table[num], int(counter))
        #print out the probability result for one input
        newnodelist = []
        for i in range (0, length):
            if input[i] == '1':
                newnodelist.append(nodelist[i])
            else:
                newnodelist.append("Not "+nodelist[i])
        print("P(", printElement(newnodelist),") = ", result)

    #print out result of step 3    
    additions = int(math.pow(2,length)) - 1
    multiplications = length - 1
    print("3. Additions and multiplications needed to calculate",\
        "the joint distribution is: ", additions, "*", multiplications, \
        "=", additions * multiplications)
    print("The number of nodes in the network is: ", length)

    #print out reselt of step 4
    spaceFull = int(math.pow(2,length)) - 1
    spaceBN = sum(prob)
    print("4. Space this network saved is: ", spaceFull, "-", \
        spaceBN, "=", spaceFull - spaceBN, '\n')
    return

def multiply(result, flag, matrix, counter):
    """for one multiplication step, depending on T or F"""
    if flag == '1':     #node is T
        result = result * matrix[counter]
    else:   #node is F
        result = result * (1 - matrix[counter])
    return result

def printElement(line):
    """print all elements in list line"""
    message = ""
    for i in range(0, len(line)):
        if i == len(line) - 1:
            message = message + line[i]
        else:
            message = message + line[i] + ", "
    return message

evaljointbayes('bayesburglar.txt')
evaljointbayes('bayesnets1.txt')
evaljointbayes('bayesnets2.txt')
