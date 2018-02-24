import numpy


class PhysicalParameter:
    ''' A base class that represents a 'physical parameter' such as
    health or shields.  It should not be instantiated on its'own.
    '''

    def __init__(self, basephysicalparameter=None, baselevel=None,
                 currentlevel=None, species=None):

        if not basephysicalparameter:
            self.current_pp = 0
            self.array = numpy.zeros(13)
            self.species = None
            return None

        self.basephysicalparameter = basephysicalparameter
        self.baselevel = baselevel
        self.currentlevel = currentlevel
        self.species = species
        self.array = numpy.array(self.type_dict[self.species])
        self.current_pp = self.pp_max_calc()

        # Check to see if species is in type dictionary as it
        # can be an easy mistype
        if self.species not in self.type_dict.keys():
            raise NameError('%s is not a valid type of %s'
                            % (self.species, type(self).__name__))

        self.array = numpy.array(self.type_dict[species])

    def pp_max_calc(self):
        if self.species:
            return(self.basephysicalparameter *
                   (1 + self.constant1 * (self.currentlevel - self.baselevel)
                    ** self.constant2))
        else:
            return(0)

    def __iadd__(self, other):
        self.current_pp += other
        return(self)

    def __isub__(self, other):
        self.current_pp -= other
        return(self)

    def __gt__(self, other):
        return(self.current_pp > other)

    def __ge__(self, other):
        return(self.current_pp >= other)

    def __lt__(self, other):
        return(self.current_pp < other)

    def __le__(self, other):
        return (self.current_pp <= other)

    def __add__(self, other):
        return(self.current_pp + other)

    def __sub__(self, other):
        return(self.current_pp - other)

    def __mul__(self, other):
        return(self.current_pp * other)

    def __truediv__(self, other):
        return(self.current_pp / other)


''' ***************** NOTE ***************
 All type dictionaries are currently of the indexing
 [Impact,Puncture,Slash]
 Damage modifiers with respect to the class
 the dictionary definition is present in. '''


class Health(PhysicalParameter):
    constant1 = 0.015
    constant2 = 2
    type_dict = ({
        'cloned flesh': [-0.25, 0, 0.25, 0, 0, 0.25, 0, 0,
                         0, -0.5, 0, 0, 0.75],
        'machinery': [0.25, 0, 0, 0, 0.5, 0, -0.25, 0.75, 0,
                      0, 0, 0, -0.25],
        'flesh': [-0.25, 0, 0.25, 0, 0, 0, 0.5, 0, 0, -0.25,
                  0, 0, 0.5],
        'robotic': [0, 0.25, -0.25, 0, 0.5, 0, -0.25, 0, 0,
                    0, 0, 0.25, 0],
        'infested': [0, 0, 0.25, 0, 0, 0.25, 0, 0, 0, 0.75,
                     0, -0.5, -0.5],
        'infested flesh': [0, 0, 0.5, -0.5, 0, 0.5, 0, 0, 0,
                           0.5, 0, 0, 0],
        'fossilized': [0, 0, 0.15, -0.25, 0, 0, -0.5, 0.5,
                       0.75, 0, 0, -0.75, 0],
        'infested sinew': [0, 0.25, 0, 0.25, 0, 0, 0, -0.5,
                           0, 0, 0, 0.5, 0]})


class Shield(PhysicalParameter):
    ''' The shield class for an enemy.  Blocks damage before the enemies
    health is affected.
    '''

    constant1 = 0.0075
    constant2 = 2
    type_dict = (
        {'shield': [0.5, -0.2, 0, 0.5, 0, 0, 0, 0,
                    0, 0, 0.75, -0.25, 0],
         'proto shield': [0.15, -0.5, 0, 0, 0, -0.5, 0.25,
                          0, -0.5, 0, 0.75, 0, 0]})


class Armor(PhysicalParameter):
    ''' The Armor class for an enemy.  Provides additional resistances
    for an enemies health to resist damage.
    '''

    constant1 = 0.005
    constant2 = 1.75
    type_dict = (
        {'ferrite': ([0, 0.5, -0.15, 0, 0, 0,
                      0.25, -0.25, 0.75, 0, 0, 0, 0]),
         'alloy': [0, 0.15, -0.5, 0.25, -0.5,
                   0, 0, 0, 0, 0, -0.5, 0.75, 0]})
