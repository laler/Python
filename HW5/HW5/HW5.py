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
    #print(contents)
    #count numbers of nodes and probabilities in each line
    length = len(contents)
    nodes = [0] * length  
    prob = [0] * length
    for num in range(0, length):
        for i in contents[num]:
            try:
                j = float(i)
                prob[num] += 1
            except ValueError:
                if i != 'NONE':
                    nodes[num] += 1       

    #print out the joint distribution function
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
    #for num in range(0,length):
    #    line=contents[num]
    #    if nodes[num]==1:
    #        print('P(',line[0].lower(),') =',line[-counter[num]])
    #    else:
    #        print('P(',line[0].lower(),'|',printElement(line[1:nodes[num]]),\
    #        ') = <',printElement(line[-counter[num]::]),'>')

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
