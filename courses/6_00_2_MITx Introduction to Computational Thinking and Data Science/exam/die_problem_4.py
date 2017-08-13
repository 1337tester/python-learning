import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    if title != None: pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.hist(values, bins = numBins)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longests = []
    suma = 0
    for i in range(numTrials):
        last = None
        longest = 0
        longest_temp = 0
        for j in range(numRolls):
            roll = die.roll()
            if roll == last:
                longest_temp += 1
            elif roll != last:                
                if longest_temp > longest:
                    longest = longest_temp
                longest_temp = 1
            last = roll
            if longest_temp > longest:
                longest = longest_temp
        longests.append(longest)
#    print(longests)        
    makeHistogram(longests, 10, 'numbers', 'length of run', 'Longest runs')
    return getMeanAndStd(longests)[0]
        
                
        
            
    
    
    
    
# One test case
random.seed(0)
#print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
print(getAverage (Die([1,2,3,4,5,6]), 50, 1000))
#print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 50, 1000))
