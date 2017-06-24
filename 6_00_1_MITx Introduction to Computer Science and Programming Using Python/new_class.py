# -*- coding: utf-8 -*-


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_diff_sqr = (self.x - other.x) ** 2
        y_diff_sqr = (self.y - other.y) ** 2
        return (x_diff_sqr + y_diff_sqr) ** 0.5
    def __str__(self):
        return '<' + str(self.x) + '.' + str(self.y) + '>'
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    
c = Coordinate(3, 4)
alfa = Coordinate(20, 8)
origin = Coordinate(0, 0)

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        	time = '6:30'
        	print(self.time)


#TEST
#clock = Clock('5:30')
#clock.print_time()

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()        
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other):
        '''returns a new intSet containing elements that appear in both sets'''
        result = intSet()
        for e in self.vals:
            if other.member(e): result.insert(e)
        return result
        
    def __len__(self):
        '''hokus pokus fidibus'''
        return len(self.vals)
        

#TEST
c = intSet()
d = intSet()
c.insert(2)
c.insert(5)
c.insert(8)
c.insert(2)
c.insert(245)
c.insert(2)
d.insert(13)
d.insert(131)
d.insert(2)

print(c)
print('length of c is ' + str(len(c)))

print(c.intersect(d))
        


        