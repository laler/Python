#CISC6525 AI HW5 
#Zhen Guo
#Bayesian Network

import math
import random

#####################################
#Q3(a)
#Counting pairs of attacking queens in 8-queens problem
def pairqueens(board):
    """Compute the pairs of attacking queens given a board state"""
    size = len(board)
    pair = 0
    for i in range(size):   #calculate pairs in rows
        for j in range(i + 1, size):
            if board[i] == board[j]:
                pair += 1;
        
    for i in range (1, 2 * (size - 1)):  #calculate pairs in diagonal lines 
        n = 0;
        for j in range(size):
            if j + int(board[j]) == i:
                n += 1
        if n > 1:
            pair += pairinline(n)

    board2 = board[::-1]    #calculate pairs in the other direction
    for i in range (1, 2 *(size - 1)):
        n = 0;
        for j in range(size):
            if j + int(board2[j]) == i:
                n += 1
        if n > 1:
            pair += pairinline(n)
        
    return int(pair)

def pairinline(n):
    """How many pairs of queens in each diagonal lines"""
    return math.factorial(n) / math.factorial(2) / math.factorial(n - 2)

########################################
#Q3(b)
#local beam search
def localbeamsearch(k, board):
    """Perform the k local beam search from one board state"""
    size = len(board)
    pair = pairqueens(board)
    currentstate = [(board, pair)]  #the initial state
  
    while 1:
        neighbors = []  
        for i in currentstate:  #generate all successors from current state
            currentsuccessors = successor(i[0])
            for s in currentsuccessors:
                neighbors.append(s)

        minneighbors = neighborrank(neighbors)[:k]  #find the k minimum successors
                
        if goaltest(minneighbors) != 0: #goal test
            print ("Test board = ", board, ", k = ", k)
            print ("Cost = 0 reached, state is ", goaltest(neighbors))
            return 1
        elif minneighbors[0][1] >= currentstate[0][1]: 
            print ("Test board = ", board, ", k = ", k)
            print ("Local cost minimum reached, minimum cost = ",\
                   currentstate[0][1], ", state is ", currentstate[0][0])
            return 0    
        else:
            currentstate = minneighbors     #save the k minimum successors to currentstate

def successor(state):
    """"""
    size = len(state)
    currentsuccessors = []
    for i in range(size):
        for j in range(size):
            if j != state[i]:
                neighborstate = state[:i] + str(j) + state[i + 1:]
                pair = pairqueens(neighborstate)
                neighbor = (neighborstate, pair)
                currentsuccessors.append(neighbor)        
    return currentsuccessors

def neighborrank(neighbors):
    """"""
    neighborsize = len(neighbors)
    for i in range(neighborsize):
        for j in range(i + 1, neighborsize):
            if neighbors[i][1] > neighbors[j][1]:
                temp = neighbors[i]
                neighbors[i] = neighbors[j]
                neighbors[j] = temp
    return neighbors

def goaltest(neighbors):
    """"""
    for state in neighbors:
        if state[1] == 0:
            return state[0]
    return 0

#########################################
#Command to call routines
#(a)
board = "31046715"
print ("Q3(a)")
print ("Test board = 31046715, pair of queens is:", end =" ")
print (pairqueens(board))

board = input("Please type in a test sequence to compute pairs of queens:")
print ("Test board = ", board, ", pair of queens is:", pairqueens(board))

#(b)
board = "45634565"
#board = "31046715"
print ("Q3(b):")
localbeamsearch(2, board)

board = input("Please type in a test sequence for local beam search:")
k = input("Please type in a k value for local beam search:")
localbeamsearch(int(k), board)

###(c)
##size = 100
##board = ""
##for i in range(size):
##    s = random.randint(0, size - 1)
##    board += str(s)
##print (board)
##for k in [1, 10, 50]:
##    localbeamsearch(k, board)

#(c)
size = 8
for k in [1, 10, 50]:
    accuracy = 0
    for i in range(100):
        board = ""
        for m in range(size):
            row = random.randint(0, size - 1)
            board += str(row)
        accuracy += localbeamsearch(k, board)
    accuracy = accuracy * 1.0 / 100
    print ("The accuracy for k= ", k, "is: ", accuracy)

