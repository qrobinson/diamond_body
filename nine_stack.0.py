#   (a): root is the origin of the Arithmetic Progression given by astapada
#   (b): bundle is subject of the table, the constant addend to consecutive AP values beginning at root

import copy

# class nineStack
root = 0

Cn5 = {'north': (1, 6), 'south': (7, 2), 'east': (3, 8), 'west': (9, 4)}
Cn6 = {'north': (7, 2), 'south': (3, 8), 'east': (9, 4), 'west': (10, 5)}
Cn7 = {'north': (3, 8), 'south': (9, 4), 'east': (5, 10), 'west': (11, 6)}
Cn8 = {'north': (9, 4), 'south': (5, 10), 'east': (11, 6), 'west': (7, 12)}
Cn9 = {'north': (5, 10), 'south': (11, 6), 'east': (7, 12), 'west': (13, 8)}
Cn10 = {'north': (11, 6), 'south': (7, 12), 'east': (13, 8), 'west': (9, 14)}
Cn11 = {'north': (7, 12), 'south': (13, 8), 'east': (9, 14), 'west': (15, 10)}
Cn12 = {'north': (13, 8), 'south': (9, 14), 'east': (15, 10), 'west': (11, 16)}
Cn13 = {'north': (9, 14), 'south': (15, 10), 'east': (11, 16), 'west': (17, 12)}


def get_sequence():
    # sequence is the ordering of the 8 gua on the rows and columns of the Astapada 8x8
    sequence = []
    ready = 0
    while not ready:
        choice = raw_input('Enter trigram sequence (default = Family x Family) Sequence #' + str(len(sequence)) + ': ')
        seq = list(str(choice))
        if not seq:
            return [list(str(12345678)), list(str(12345678))]
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


def get_bundle():
    # the bundle is a scalar applied to the lines of the upper and lower gua, in ascending line order
    bundle = []
    ready = 0
    while not ready:
        choice = raw_input('Enter three counting numbers (default = 123) Bundle #' + str(len(bundle)) + ': ')
        fiber = list(str(choice))
        # print "Fiber is: ", fiber
        if not fiber:
            return [list(str(123)), list(str(123))]
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


#    print "Inner sequence: ",Sequence[0], "Outer sequence: ", Sequence[1]

class Astapada:
    # Astapada is an 8x8 matrix of trigram-sums
    bundle = get_bundle()
    sequence = get_sequence()

    def __init__(self, phase):

        # hexagram
        def pair_gua(_inner, _outer):
            inner_gua = 0
            outer_gua = 0
            # Bundle the Gua
            for position in range(len(Astapada.bundle[0])):
                inner_gua += bagua[_inner][position] * int(Astapada.bundle[0][position])
                outer_gua += bagua[_outer][position] * int(Astapada.bundle[1][position])
            # print innerGua, outerGua
            return sum([inner_gua, outer_gua])  # hexagram construction

        self.phase = phase
        self.matrix = []
        dark = Cn5[self.phase][0]
        light = Cn5[self.phase][1]

        # trigram definitions
        earth = [dark, dark, dark]
        thunder = [light, dark, dark]
        water = [dark, light, dark]
        mountain = [dark, dark, light]
        lake = [light, light, dark]
        fire = [light, dark, light]
        wind = [dark, light, light]
        heaven = [light, light, light]
        bagua = [None, earth, thunder, water, mountain, lake, fire, wind, heaven]

        self.sequence = copy.deepcopy(Astapada.sequence)  # copy the class object
        if self.phase in ['metal', 'fire']:
            self.sequence[0].reverse()
            self.sequence[1].reverse()
        for inner in self.sequence[0]:
            rank = []
            for outer in self.sequence[1]:
                #                print "Inner order: ", Sequence[0], '\t'+"Outer order: ", Sequence[1]
                #                print "inn:",inn,'\t',"out:",out
                #                print "inn:",int(inn),'\t',"out:",int(out)
                rank.append(pair_gua(int(inner), int(outer)))
            self.matrix.append(rank)

# Dict: Q = dict(zip(HeTu.keys(),[Astapada(phase) for phase in HeTu.keys() if phase]))
# List of 2-tuples: Q = zip(HeTu.keys(),[Astapada(phase) for phase in HeTu.keys() if phase])
# [Q.append(dict(zip(HeTu.keys(),[Astapada(phase, level) for phase in HeTu.keys() if phase]))) for level in range(8)]

