from AdjacencyList import AdjacencyList
from ArrayList import ArrayList
import random
import time
import matplotlib.pyplot as plt

class Simulation:
    class Node():
        def __init__(self, i):
            self.state = None
            self.recover = None
            self.index = i
            self.adj = None

    def __init__(self, interactions, n1, alpha, recovery_days, transmission_rate, fatality_rate, initial_setting):
        '''
        Initialize parameters and objects for COVID-19 simulation
        '''
        # Constants
        self.n = n1
        self.ALPHA = alpha
        self.RECOVERY_DAYS = recovery_days
        self.TRANSMISSION_RATE = transmission_rate
        self.FATALITY_RATE = fatality_rate
        self.INITIAL_SETTING = initial_setting
        self.INTERACTION = interactions

        # States
        self.CLEAN = 0
        self.INFECTED = 1
        self.DEAD = 2
        self.RECOVERED = 3

        # Initialize list
        self.Nodes = ArrayList()

        for i in range(self.n):
            self.Nodes.append(self.Node(i))

        # Set random indexes to infected
        for v in self.Nodes:
            if random.uniform(0,1) <= self.INITIAL_SETTING: # Probability of being infected
                v.state = self.INFECTED
                v.recover = self.RECOVERY_DAYS
            else: # Probability of not being infected
                v.state = self.CLEAN

        # Initialize graph
        self.Graph = self.getInteractionGraph()

    def getInteractionGraph(self):
        '''
        Creates an AdjacencyList of size self.n to monitor node interactions
        '''

        start_time = time.time()
        g = AdjacencyList(self.n) # Declare adjacency list
        for repeat in range(self.INTERACTION): # Repeat interaction times
            for j in range(0,self.n): # Repeat for all nodes
                i = self.Nodes.get(random.randint(0,j)) # Get a random node
                if random.uniform(0,1) < self.ALPHA: # Alpha chance
                    g.add_edge(j, i)
                else:
                    ngh = g.out_edges(i.index) # Find neighbors of i
                    if ngh.size() > 0: # Validate that there are neighbors
                        k = random.choice(ngh)
                        g.add_edge(j, k)

        for v in self.Nodes:
            v.adj = g.out_edges(v.index)

        elapsed_time = time.time() - start_time
        print(f"Created interaction graph of size {self.n*self.INTERACTION} in", elapsed_time, "seconds")
        return g

    def run(self, days : int):
        '''
        Runs the simulation for "days" amount of times
        '''

        start_time = time.time()

        # Initialize plot lists
        day = []
        clean = []
        infected = []
        dead = []
        recovered = []

        # Header
        print("=== === === === === === === === === === === === === === ===")

        # Day repeat
        for repeat in range(1,days+1):

            # Initialize node count
            infected_nodes = 0
            dead_nodes = 0
            clean_nodes = 0
            recovered_nodes = 0

            # Print statistics
            for i in self.Nodes:
                if i.state==self.CLEAN: clean_nodes += 1
                if i.state==self.INFECTED: infected_nodes += 1
                elif i.state==self.DEAD: dead_nodes += 1
                elif i.state==self.RECOVERED: recovered_nodes += 1
            print("DAY:", repeat, "CLEAN:", clean_nodes, "INFECTED:", infected_nodes, "DEAD:", dead_nodes, "RECOVERED:", recovered_nodes)

            # Plot lists
            day.append(repeat)
            clean.append(clean_nodes)
            infected.append(infected_nodes)
            dead.append(dead_nodes)
            recovered.append(recovered_nodes)

            # Run simulation
            for v in self.Nodes: # Run through all nodes
                if v.state==self.INFECTED: # Check for infection
                    for w in v.adj: # Find interaction neighbors self.Graph.covid_out_edges(v.index)
                        if w.state == self.CLEAN: # If infected interacts with clean
                            if random.uniform(0,1) <= self.TRANSMISSION_RATE: # Transmission chance
                                self.Nodes.get(w.index).state = self.INFECTED # Clean is now infected
                                self.Nodes.get(w.index).recover = self.RECOVERY_DAYS # Set recovery days to RECOVERY_DAYS
                    v.recover -= 1 # Subtract recovery day
                    if v.recover == 0: # If recovery is over
                        if random.uniform(0,1) <= self.FATALITY_RATE: # Fatality chance
                            v.state = self.DEAD # Node is dead
                        else:
                            v.state = self.RECOVERED # Node recovered

        # Create plot
        #plt.plot(day, clean, 'b')
        plt.plot(day, infected, 'r')
        plt.plot(day, dead, 'k')
        plt.plot(day, recovered, 'g')
        plt.legend(['Infected', 'Dead', 'Recovered'], loc='upper right')

        elapsed_time = time.time() - start_time

        # Footer
        print("=== === === === === === === === === === === === === === ===")
        print(f"Simulation for {days} days completed in {elapsed_time} seconds")

        # View plot
        opt=""
        while opt!="Y" and opt!="N":
            opt=input("Would you like to view the graph? (Y/N): ")
            if opt=="Y":
                plt.show()
                input("Press enter to continue...")
        plt.clf()
        plt.close()







