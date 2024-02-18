from scipy.spatial import distance


import PyPluMA
import PyIO

class MahalanobisPlugin:
    def input(self, inputfile):
        self.parameters = PyIO.readParameters(inputfile)
        ivfile = open(PyPluMA.prefix()+"/"+self.parameters["inputvector"], 'r')
        self.iv = []
        for line in ivfile:
            line = line.strip()
            row = line.split(',')
            for i in range(len(row)):
                row[i] = float(row[i])
            self.iv.append(row)
        v1file = open(PyPluMA.prefix()+"/"+self.parameters["vector1"], 'r')
        self.v1 = []
        for line in v1file:
            self.v1.append(float(line.strip()))
        v2file = open(PyPluMA.prefix()+"/"+self.parameters["vector2"], 'r')
        self.v2 = []
        for line in v2file:
            self.v2.append(float(line.strip()))


    def run(self):
        self.result = distance.mahalanobis(self.v1, self.v2, self.iv)

    def output(self, outputfile):
        print(self.result)
#iv = [[1, 0.5, 0.5], [0.5, 1, 0.5], [0.5, 0.5, 1]]
#result = distance.mahalanobis([1, 0, 0], [0, 1, 0], iv)
#print(result)
