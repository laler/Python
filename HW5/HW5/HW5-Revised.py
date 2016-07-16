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
    print "1. Read file", fname, "successfully."
    f.close()
    
    #count numbers of nodes and probabilities in each line
    length = len(contents)
    nodes, prob = [0] * length, [0] * length
    table = []  #save all probabilities for each node                   
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
    print "2. The joint distribution using this network is:"
    nodelist = []
    for line in contents:
        nodelist.append(line[0])
    print "P(", printElement(nodelist), ") = "
    for num in range(0, length):
        line = contents[num]
        if  nodes[num] == 1:
            print "P(", line[0], ")", 
        else: 
            print "P(", line[0], '|', printElement(line[1:nodes[num]]),\
             ")", 
        if num == length - 1:
            print ' '
        else: 
            print ' * ', 
 
    #print out the full joint distribution table 
###This is the revised version using recursive calls and###
###print out the cpt table to a .txt file###
    #further revision includes deleting depth by pop() table, contents and nodes
    #also, I can extract the parents in the previous step, then contents will not be used here
    fo=open(fname+'.zz.txt','w')
    result = 1.0
    depth = 0
    global additions, multiplications
    additions, multiplications = 0, 0
    fullCPT(nodelist, [], result, depth, fo, contents, table, nodes)
    fo.close()

    #print out result of step 3    
    print "3. Additions and multiplications needed to calculate",\
        "the joint distribution is:", additions, "and", multiplications
    print "The number of nodes in the network is: ", length

    #print out reselt of step 4
    spaceFull = int(math.pow(2,length)) - 1
    spaceBN = sum(prob)
    print "4. Space this network saved is (Compactness): ", spaceBN, "/", \
        spaceFull, "=", float(spaceBN) / float(spaceFull), '\n'
    return

def fullCPT(nodelist, rowname, result, depth, fo, contents, table, nodes):
    """recursivedly divide the problem by poping item out of nodelist"""
    if len(nodelist) == 0:
        if (not fo==0):
            fo.write("P(" + printElement(rowname) + ") = " + str(result) + "\n")
        return
    
    global additions, multiplications
    counter = counterCompute(contents[depth], nodes[depth], rowname)
    curprob = table[depth][int(counter)]
    newdepth = depth + 1
    newnodelist = list(nodelist)
    cur = newnodelist.pop(0)

    #recursive calls for all nodes, one call for one node
    newrowname1 = list(rowname)
    newrowname1.append(cur)
    result1 = result * curprob #positive case for cur
    multiplications += 1
    fullCPT(newnodelist, newrowname1, result1, newdepth, fo, contents, table, nodes)

    newrowname0 = list(rowname)
    newrowname0.append("Not " + cur)
    result0 = result * (1 - curprob) #negative case for cur
    multiplications += 1
    additions += 1
    fullCPT(newnodelist, newrowname0, result0, newdepth, fo, contents, table, nodes)
    return

def counterCompute(line, nodes, rowname):
    """compute the index for prob based on parents"""
    counter = 0
    if  nodes != 1:     #node has parents    
        parent = line[1: nodes]            
        for par in parent:
            if ("Not " + par) in rowname: #one parent is "Not par"
                counter = counter + math.pow(2, nodes - 2 - parent.index(par))
    return counter

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
