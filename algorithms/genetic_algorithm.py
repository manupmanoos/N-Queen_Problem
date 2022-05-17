import random
from itertools import permutations
#Based on Darwin's Survival of The Fittest 
#Here Fitness is taken as the Pair of Non Attacking Queens arrangement
def random_space(num_queen):
    new_list = []
    for n in range(num_queen):
        new_list.append(random.randint(1, num_queen))
    return new_list

def random_solution(setOfAllSolutions, probabilities):
    total_prob = 0
    for solution, probability in zip(setOfAllSolutions, probabilities):
        total_prob += probability
    random_prob = random.uniform(0, total_prob)
    end = 0
    for solution, probability in zip(setOfAllSolutions, probabilities):
        if end + probability >= random_prob:
            return solution
        end += probability




def pairOfNonAttackingQueens(arrangement,maxPairOfNonAttackingQueens): #Find the fittest arrangement
    row_attacks = 0
    for position in arrangement:
        row_attacks += arrangement.count(position)-1
    row_attacks /= 2    
    arrangement_len = len(arrangement)
    left_diag = [0] * 2 * arrangement_len
    right_diag = [0] * 2 * arrangement_len
    i=0
    while i<=arrangement_len-1:
        left_diag[i + arrangement[i] - 1] += 1
        right_diag[len(arrangement) - i + arrangement[i] - 2] += 1
        i=i+1

    diagonal_attacks = 0
    i=0
    while i<=((2*arrangement_len-1) -1):
        count = 0
        if left_diag[i] >= 2:
            count += left_diag[i]-1
        if right_diag[i] >= 2:
            count += right_diag[i]-1
        diagonal_attacks += count / (arrangement_len-abs(i-arrangement_len+1))
        i=i+1
    
    nonAttackingPositions = int(maxPairOfNonAttackingQueens - (row_attacks + diagonal_attacks))
    return  nonAttackingPositions


def alter(child): 
    random_index = random.randint(0, len(child) - 1)
    random_value = random.randint(1, len(child))
    child[random_index] = random_value
    return child
        
def crossover(x, y): #Re-arrange the position in the matrix
    slice_index = random.randint(0, len(x) - 1)
    return x[0:slice_index] + y[slice_index:len(x)]


def generate_solutionSet(setOfAllSolutions, pairOfNonAttackingQueens,maxPairOfNonAttackingQueens,alter_probability= 0.1): #Populate or generate the list of solutions
    new_SetOfSolutions = []
    return_sol =[]
    probability_vals = []
    for solution in setOfAllSolutions:
        probability_vals.append(pairOfNonAttackingQueens(solution,maxPairOfNonAttackingQueens) / maxPairOfNonAttackingQueens)
    
    i=0
    while i<=len(setOfAllSolutions) - 1:
        parent_1 = random_solution(setOfAllSolutions, probability_vals) 
        parent_2 = random_solution(setOfAllSolutions, probability_vals) 
        child = crossover(parent_1, parent_2) 
        if alter_probability >= random.random() :
            child = alter(child)
        
        new_SetOfSolutions.append(child)
        if pairOfNonAttackingQueens(child,maxPairOfNonAttackingQueens) == maxPairOfNonAttackingQueens:
            return_sol.append(child)
            break
        i=i+1
    return new_SetOfSolutions, return_sol

def print_arrangement(pos,maxPairOfNonAttackingQueens): #For every position in each fitness (Pair of non-attacking queens), show
    print("Position = {},  Fitness Score = {}"
        .format(str(pos), pairOfNonAttackingQueens(pos,maxPairOfNonAttackingQueens)))
    matrix = [] 
    for i in range(len(pos)):          # A for loop for row entries 
        a =[] 
        for j in range(len(pos)):      # A for loop for column entries 
            if j+1 == pos[i]:
                entry=1
                a.append(entry)
            else:
                entry=0
                a.append(entry)
        matrix.append(a) 
    #print(matrix)
    print('Position of Queens on board')
    for element in matrix:        
        print(''.join(str(element)))
    

#if __name__ == "__main__":
def main(num_queen):
    
    if num_queen <= 3:
        print("Solution does not exist")
    else: 
        setOfAllSolutions = []
        for i in range(100):
            setOfAllSolutions.append(random_space(num_queen))

        maxPairOfNonAttackingQueens = (num_queen*(num_queen-1))/2 
        generation_count =1
        return_solution =[]
        while [pairOfNonAttackingQueens(pos,maxPairOfNonAttackingQueens) for pos in setOfAllSolutions].count(maxPairOfNonAttackingQueens) <1:

            setOfAllSolutions, return_sol = generate_solutionSet(setOfAllSolutions, pairOfNonAttackingQueens,maxPairOfNonAttackingQueens)
            generation_count +=1

        if generation_count == 1:
            for item in setOfAllSolutions:
                if pairOfNonAttackingQueens(item,maxPairOfNonAttackingQueens) == maxPairOfNonAttackingQueens:
                    print("")
                    print("Solution found in {}th generation is: ".format(generation_count))
                    return_solution.append(item)
                    print_arrangement(item,maxPairOfNonAttackingQueens)
        else:
            print("")
            print("Solution found in {}th generation is: ".format(generation_count))
            return_solution.append(return_sol[0])
            print_arrangement(return_sol[0],maxPairOfNonAttackingQueens)
        #for pos in setOfAllSolutions:
            #if pairOfNonAttackingQueens(pos,maxPairOfNonAttackingQueens) == maxPairOfNonAttackingQueens:
                #print("")
                #new_list =[list(p) for p in permutations(pos)]
                #i=1
                #for item in new_list:
                    #if pairOfNonAttackingQueens(item,maxPairOfNonAttackingQueens) == maxPairOfNonAttackingQueens:
                #return_solution.append(pos)
                #print("Solution  is: ")
                #print_arrangement(pos,maxPairOfNonAttackingQueens)
                        #i+=1
    return return_solution
if __name__ == '__main__':
    main()
