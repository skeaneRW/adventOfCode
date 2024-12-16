import itertools
testPath = 'adventofcode/2024/day13/testInput.txt'
inputPath = 'adventofcode/2024/day13/input.txt'
chosenPath = inputPath

def getClawMachines(input):
    file = open(input, 'r')
    lines = [line.replace('\n','') for line in file.readlines()]
    machines = []
    machine = {}
    for line in lines:
        if line.__contains__('Button A:'):
            line = line.replace('Button A: ','')
            line = line.replace('X','0')
            line = line.replace('Y','0')
            line = line.split(', ')
            machine['btnA'] = (eval(line[0]), eval(line[1]))
        elif line.__contains__('Button B:'):
            line = line.replace('Button B: ','')
            line = line.replace('X','0')
            line = line.replace('Y','0')
            line = line.split(', ')
            machine['btnB'] = (eval(line[0]), eval(line[1]))
        elif line.__contains__('Prize:'):
            line = line.replace('Prize: ','')
            line = line.replace('X=','')
            line = line.replace('Y=','')
            line = line.split(', ')
            machine['Prize'] = (eval(line[0]) + 10000000000000, eval(line[1]) + 10000000000000)
        if line == '':
            machines.append(machine)
            machine = {}
    machines.append(machine)
    return machines

machines = getClawMachines(chosenPath)

'''
part 1 solution took too long to solve part 2;
needed to hit reddit and brush up on some math to solve this one
'''

def getMinimum(machine):
    btnA_X, btnA_Y = machine['btnA']
    btnB_X, btnB_Y = machine['btnB']
    total_X, total_Y = machine['Prize']
    b = (total_X * btnA_Y - total_Y * btnA_X)//(btnA_Y * btnB_X-btnB_Y * btnA_X)
    a = (total_X * btnB_Y - total_Y * btnB_X)//(btnB_Y * btnA_X-btnB_X * btnA_Y)
    totalX_Match = btnA_X * a + btnB_X * b == total_X
    totalY_Match = btnA_Y * a + btnB_Y * b == total_Y
    if totalX_Match and totalY_Match:
        a = 3 * a
        return a + b
    else:
        return 0

cost = 0
for machine in machines:
    cost += getMinimum(machine)

print(cost)

