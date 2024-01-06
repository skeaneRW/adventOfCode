inputPath = '2023/day15/input.txt'
testPath = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
chosenPath = inputPath

def parseInput(path):
    file = open(path, 'r')
    for line in file:
        line = line.replace('\n','')
    return line
   
def useHashAlgo(str, val=0):
    for char in str:
        val += (ord(char))
        val *= 17
        val = val % 256
    return val

def getResults(string, tot = 0):

    for str in string.split(','):
        tot += useHashAlgo(str)
    return tot

input = parseInput(chosenPath)
print(getResults(input))