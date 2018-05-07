class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        mysorted = sorted(self.__elements)
        self.maximumDifference = mysorted[len(mysorted) - 1] - mysorted[0]

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)