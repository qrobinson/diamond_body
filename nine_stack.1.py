# namu
# class nineStack

#   (a): root is the origin of the Arithmetic Progression given by Astapada, defaults to 0
#   (b): bundle is subject of the table, the constant addend to consecutive AP values beginning at root
#   (c): sequence is a pair of lists which order the 8x8
#   (d): planets give a set of 3x3 matrices, each alternatively presented as 5-cell

root = int()
graha = int()
stack = list()

# HeTu River-map projected onto Nava-graha
Surya =   {'north': (1, 6),  'south': (7, 2),   'east': (3, 8),   'west': (9, 4),   'central': (5, 10)}
Chandra = {'north': (7, 2),  'south': (3, 8),   'east': (9, 4),   'west': (5, 10),  'central': (11, 6)}
Mangal =  {'north': (3, 8),  'south': (9, 4),   'east': (5, 10),  'west': (11, 6),  'central': (7, 12)}
Budha =   {'north': (9, 4),  'south': (5, 10),  'east': (11, 6),  'west': (7, 12),  'central': (13, 8)}
Guru =    {'north': (5, 10), 'south': (11, 6),  'east': (7, 12),  'west': (13, 8),  'central': (9, 14)}
Shukra =  {'north': (11, 6), 'south': (7, 12),  'east': (13, 8),  'west': (9, 14),  'central': (15, 10)}
Shani =   {'north': (7, 12), 'south': (13, 8),  'east': (9, 14),  'west': (15, 10), 'central': (11, 16)}
Rahu =    {'north': (13, 8), 'south': (9, 14),  'east': (15, 10), 'west': (11, 16), 'central': (17, 12)}
Ketu =    {'north': (9, 14), 'south': (15, 10), 'east': (11, 16), 'west': (17, 12), 'central': (13, 18)}

# Nava-graha: nine_planets
planets = [Surya, Chandra, Mangal, Budha, Guru, Shukra, Shani, Rahu, Ketu]


def get_sequence():
    # sequence is a pair of orderings of the 8 gua over the rows and columns of the 8x8
    sequence = []
    ready = 0
    while not ready:
        choice = raw_input('Enter trigram sequence (default = Family x Family) Sequence #' + str(len(sequence)) + ': ')
        seq = list(str(choice))
        if not seq:
            sequence = list(str(12345678)), list(str(12345678))
            print "Sequence is:", sequence
            return sequence
        if len(seq) != 8:
            continue
        else:
            for i in list(str(12345678)):
                if i in seq:
                    continue
                elif i not in seq:
                    break
            else:
                sequence.append(seq)
                if len(sequence) > 1:
                    ready += 1
    print "Sequence is:", sequence
    return sequence
#    print "Lower sequence: ",sequence[0], "Upper sequence: ", sequence[1]


def get_bundle():
    # bundle scales the superposed lower & upper gua, ascending order
    bundle = []
    ready = 0
    while not ready:
        choice = raw_input('Enter three counting numbers (default = 123) Bundle #' + str(len(bundle)) + ': ')
        fiber = list(str(choice))
        # print "Fiber is: ", fiber
        if not fiber:
            bundle = [list(str(123)), list(str(123))]
            print "Bundle is:", bundle
            return bundle
        if len(fiber) != 3:
            continue
        else:
            for i in fiber:
                if i in list(str(123456789)):
                    continue
                elif i not in list(str(123456789)):
                    break
            else:
                bundle.append(fiber)
                if len(bundle) > 1:
                    ready += 1
    print "Bundle is", bundle
    return bundle


# generates fibers (half-bundles), all 729 in 111 to 999
def get_fiber():
    fiber = []
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                fiber.append(list(str(i) + str(j) + str(k)))
    return fiber


class Astapada:
    # Astapada: 8x8 matrix of ordered trigram-pairs given as values
    # bundle and sequence are global parameters for ordering the 8x8 and shaping its values
    bundle = get_bundle()
    sequence = get_sequence()

    def __init__(self, _graha, _direction):
        # building the 8x8 means ordering the field, pairing and bundling the gua
        # graha: integer; index to planets
        # direction: string; key to planet's light-dark values

        self.bundle = Astapada.bundle
        self.sequence = Astapada.sequence
        self.graha = _graha
        self.direction = _direction
        self.matrix = []

        # build hexagram as gua-pair(_lower,_upper) --> sum, product, ...
        def bind_gua(_lower, _upper):
            lower_gua = 0
            upper_gua = 0

            # scale the gua by the bundle
            for position in range(len(Astapada.bundle[0])):
                lower_gua += bagua[_lower][position] * int(Astapada.bundle[0][position])
                upper_gua += bagua[_upper][position] * int(Astapada.bundle[1][position])

            # DEBUG: print lower_gua, upper_gua
            # hexagram gets sum of trigram values
            return sum([lower_gua, upper_gua])

        # index the planet to get its light-dark values
        light = planets[self.graha][self.direction][0]
        dark =  planets[self.graha][self.direction][1]

        # abstract trigram/gua definitions
        earth    = [dark, dark, dark]
        thunder  = [light, dark, dark]
        water    = [dark, light, dark]
        mountain = [dark, dark, light]
        lake     = [light, light, dark]
        fire     = [light, dark, light]
        wind     = [dark, light, light]
        heaven   = [light, light, light]

        bagua = [None, earth, thunder, water, mountain, lake, fire, wind, heaven]

        # reverse upper & lower trigram sequences in the south and west directions to preserve reflexive symmetry
        if self.direction in ['west', 'south']:
            self.sequence[0].reverse()
            self.sequence[1].reverse()

        '''
        call bind_gua to build Astapada
        # 1. iterate rank-wise over sequence (lower x upper)
        # 2. assign values to a rank of trigram pairs
        # 3. append rank of evaluated trigram-pairs to self.matrix
        '''
        for lower in self.sequence[0]:
            rank = []
            for upper in self.sequence[1]:
                # DEBUG: print "Inner order: ", Sequence[0], '\t'+"Outer order: ", Sequence[1]
                # DEBUG: print "lower:",lower,'\t',"upper:",upper
                # DEBUG: print "lower:",int(lower),'\t',"upper:",int(upper)
                rank.append(bind_gua(int(lower), int(upper)))
            self.matrix.append(rank)


# Bundler's constructor receives list[3] as argument
class Bundler(Astapada):
    def __init__(self, _fiber):
        # default to Surya in the north
        self.graha = 0
        self.direction = 'north'
        self.bundle = _fiber
        self.sequence = Astapada.sequence[0]
        self.rank = []

        # _image is index to bagua
        def bind_gua(_image):
            gua = 0
            # scale the gua by the fiber/bundle
            for position in range(len(self.bundle)):
                gua += bagua[_image][position] * int(self.bundle[position])
            return gua

        # index the planet to get its light-dark values
        light = planets[self.graha][self.direction][0]
        dark =  planets[self.graha][self.direction][1]

        # abstract trigram/gua definitions
        earth    = [dark, dark, dark]
        thunder  = [light, dark, dark]
        water    = [dark, light, dark]
        mountain = [dark, dark, light]
        lake     = [light, light, dark]
        fire     = [light, dark, light]
        wind     = [dark, light, light]
        heaven   = [light, light, light]

        bagua = [None, heaven, wind, fire, lake, mountain, water, thunder, earth]
        # bagua = [None, earth, thunder, water, mountain, lake, fire, wind, heaven]

        # iterate over the gua in sequence;
        for image in self.sequence:
            self.rank.append(bind_gua(int(image)))

'''
get_fiber() returns an exhaustive list of 729 half-bundles
Bundler's constructor accepts a list of three integers

for fiber in get_fiber():    Bundler(list(fiber))

bun = []; for fiber in get_fiber(): bun.append( (fiber,Bundler(list(fiber))) )                  
for i in range(len(bun)): print bun[i][0]; print bun[i][1].rank

Construct (via comprehension) the nine-stack:
Stack is a list of dictionaries, generated per each planet, by zipping directions with instances of 8x8

[stack.append(dict(zip(planets[graha].keys(),
                   [Astapada(graha, direction) for direction in planets[graha].keys()]
                   ))) for graha in range(len(planets))]


Support for matplotlib                   
    ipython --matplotlib
        import numpy as np
        import matplotlib
        #matplotlib.use('Agg')
        import matplotlib.pylab as plt
from nine_stack import *
set=[]; bun=[]
for fiber in get_fiber(): bun.append( (fiber,Bundler(list(fiber))) )
for l in range(0,len(bun)): set.append(len((np.unique(bun[l][1].rank))))
plt.hist(set, bins=8, density=1)
plt.show()

## investigating 111 to 999
#empty list to hold the values
m=[]
# iterate over all 729 half bundles
for i in range(len(bun)):
    # bundle, evaluated images, unique values on the images
    a = bun[i][0]; c = np.unique(bun[i][1].rank); b = bun[i][1].rank
    # in the case of only 7 discrete values out of 8
    if len(c) == 7:
        k=0
        # get the sum of the bundle
        for j in a:
            k+=int(j)
        # print the bundle and its sum
        #print a, k
        # collect the sum, bundle, and unique values
        m.append((k, a, b))
# sort for reading
m.sort()
'''
# hung phat
