#! /usr/bin/python

class Grille:
    def __init__(self, sequence):
        self.data = list(sequence)
        
    def __str__(self):
        for ligne in range(0, 8):
            for col in range(0, 8):
                print(self.data[ligne * 9 + col], end='')
            print "\n"
        
    @staticmethod
    def createFromFile(filename):
        inputfile = open(filename, 'r')
        print ("encoding:" + str(inputfile.encoding))
        s = inputfile.read()
        return Grille(s.split())

