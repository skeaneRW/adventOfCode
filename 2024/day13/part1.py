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
            machine['Prize'] = (eval(line[0]), eval(line[1]))
        if line == '':
            machines.append(machine)
            machine = {}
    machines.append(machine)
    return machines

machines = getClawMachines(chosenPath)

def slope(btn):
    x, y = btn
    if x == 0:
        return 0
    return y/x

def pressBtn(machine, btnLetter, pushes):
    btn_modifier = machine[f'btn{btnLetter}']
    x, y = btn_modifier
    endPoint = pushes * x, pushes * y
    return endPoint

def pressBtns(machine, btnA_pushes, btnB_pushes):
    btnA = pressBtn(machine, 'A', btnA_pushes)
    btnB = pressBtn(machine, 'B', btnB_pushes)
    return (btnA[0] + btnB[0], btnA[1] + btnB[1])

def maxPushes(machine, btnLetter):
    prize = machine['Prize']
    prize_x, prize_y = prize
    counter = 0
    result = pressBtn(machine, btnLetter, counter)
    while result[0] < prize_x or result[1] < prize_y:
        counter += 1
        result = pressBtn(machine, btnLetter, counter)
    return counter

def getCombinations(machine):
    maxPushesA = maxPushes(machine, 'A')
    maxPushesB = maxPushes(machine, 'B')
    max = maxPushesA if maxPushesA > maxPushesB else maxPushesB
    print(max)
    combos = [list(x) for x in itertools.product(range(max+1), repeat=2)]
    return combos

combinations = getCombinations(machines[0])

def getValidCombinations(machine, combinations):
    validCombos = []
    for combo in combinations:
        btnA_pushes, btnB_pushes = combo
        endPoint = pressBtns(machine, btnA_pushes, btnB_pushes)
        if endPoint == machine['Prize']:
            validCombos.append(combo)
    return validCombos

def getLowestCost(machines, combinations):
    results = []
    for machine in machines:
        validCombos = getValidCombinations(machine, combinations)
        btnCost = None
        btnPushes = None
        if(len(validCombos) == 0):
            continue
        for combo in validCombos:
            result = {}
            btnACost = combo[0]*3
            btnBCost = combo[1]*1
            if btnCost == None or btnCost > btnACost + btnBCost:
                btnCost = btnACost + btnBCost
                btnPushes = combo
            result['pushes'] = btnPushes
            result['cost'] = btnCost
        results.append(result)
    return sum(list(result['cost'] for result in results))
                


print(getLowestCost(machines, combinations))

