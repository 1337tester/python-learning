import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    new_rabbit = 0
    
    for rabbit in range(CURRENTRABBITPOP):
        rabbit_repro = 1.0 - CURRENTRABBITPOP/MAXRABBITPOP
        if random.random() <= rabbit_repro and (new_rabbit + CURRENTRABBITPOP < MAXRABBITPOP):
            new_rabbit += 1
    CURRENTRABBITPOP += new_rabbit
    
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    born_fox = 0
    fox_died = 0
    
    for fox in range(CURRENTFOXPOP):
        prob_fox_eats = CURRENTRABBITPOP/MAXRABBITPOP
        if CURRENTRABBITPOP > 10 and random.random() <= prob_fox_eats:
            CURRENTRABBITPOP -= 1            
            if random.random() <= 1/3:
                born_fox += 1
        else:
            if random.random() <= 1/10 and (CURRENTFOXPOP + born_fox - fox_died > 10):
                fox_died += 1
    CURRENTFOXPOP -= fox_died
    CURRENTFOXPOP += born_fox
    
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit = []
    fox = []
    for n in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit.append(CURRENTRABBITPOP)
        fox.append(CURRENTFOXPOP)
    return (rabbit, fox)
    
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30
numSteps = 200
result = runSimulation(numSteps)


#set plot size
pylab.rcParams['figure.figsize'] = 20, 20
#set line width
pylab.rcParams['lines.linewidth'] = 4
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
#set size of markers
pylab.rcParams['lines.markersize'] = 10
#set number of examples shown in legends
pylab.rcParams['legend.numpoints'] = 10



pylab.plot(range(numSteps),result[0], label='rabbit')
pylab.plot(range(numSteps),result[1], label='fox')
pylab.legend()
pylab.show()
#
coeff = polyfit(range(len(result[0])), result[0], 2)
coeff1 = polyfit(range(len(result[1])), result[1], 2)


#print(result[0], result[1])
#print(coeff, coeff1)


#plot(pylab.polyval([2.68719786, 3.70917874],[2010, 2011, 2013, 2015]), range(len(result[0])))
#plot(polyval(coeff, range(len(result[0]))))
#plot(polyval(coeff1, range(len(result[1]))))

