import os

class VarMap(object):
    '''Translates between two naming schemes for a list of variables'''

    def __init__(self, tuples):
        '''tuples can be either a list of tuples:

        vm = VarMap([
            ('a', 'b'),
            ('b', 'a'),
        ])   

        or the path to a file containing:

        a		b		some documentation here
        c		d
        b		a		inverting a and b
        #  d             e              comments are allowed, like empty lines:

        f               g

        The list of variables in the first column is denoted as a, 
        and the list in the second column is denoted as b. 
        
        '''
        if isinstance(tuples, basestring):
            tuples = self._load(tuples)
        self.toa = dict()
        self.tob = dict()
        for a,b in tuples:
            if a in self.tob:
                raise ValueError(a + ' appears twice in list b')
            if b in self.toa:
                raise ValueError(b + ' appears twice in list a')
            self.tob[a] = b
            self.toa[b] = a

    def _load(self, fname):
        '''loads variable map from fname'''
        with open(fname) as ifile:
            tuples = []
            for line in ifile:
                line = line.strip()
                if len(line)==0 or line.startswith('#'):
                    continue
                variable_pair = line.split()[:2]
                tuples.append(variable_pair)
            return tuples

    

    
