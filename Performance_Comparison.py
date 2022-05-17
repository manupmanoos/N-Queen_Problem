from  algorithms import backtracking, hillclimbing, genetic_algorithm,baseline
import numpy as np
from matplotlib import pyplot as plt

queen_range=11
N_queen=[]
Hill_time=[]
Genetic_time=[]
backtracking_time=[]
baseline_time=[]

for i in range(4,queen_range):
    N_queen=np.append(N_queen,i)
    Hill_time= np.append(Hill_time,hillclimbing.main(i))
    Genetic_time= np.append(Genetic_time,genetic_algorithm.main(i))
    backtracking_time= np.append(backtracking_time,backtracking.main(i))
    baseline_time = np.append(baseline_time,baseline.main(i))



plt.xticks(np.arange(min(N_queen), max(N_queen)+1, 1))
plt.plot(N_queen,baseline_time,label="Baseline")
plt.plot(N_queen,Hill_time,label="Hill Climbing")
plt.plot(N_queen,backtracking_time,label="Backtracking")
plt.plot(N_queen,Genetic_time,label="Genetic algorithm")
plt.xlabel('Number of Queens')
plt.ylabel('Time in milliseconds')
plt.legend(loc='upper left')
plt.title('Algorithm performance')
plt.show()