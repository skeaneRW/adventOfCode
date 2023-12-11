inputPath = "2023/day6/input.txt"
testPath = "2023/day6/testInput1.txt"

def parseInput(path):
    file = open(path, 'r')
    times = []
    distances = []
    result = []
    for index, line in enumerate(file.readlines()):
        line = line.replace('\n', '').replace(' ','').split(':')
        line = list(filter(lambda x: x != '', line))[1::]
        line = list(map(lambda x: int(x), line))
        if index == 0:
            times = line
        if index == 1:
            distances = line
    for index,time in enumerate(times):
        result.append({'time': times[index], 'distance': distances[index]})
    return(result)

def evaluateRaces(winningRaces):
    def calcDistance(holdDuration, bestDist):
        speed = holdDuration
        travelDistance = (timeAllotted - holdDuration) * speed
        # print(f'holding button for {holdDuration}ms')
        # print(f'speed is {speed} mm per ms')
        # print(f'{timeAllotted - holdDuration}ms remain')
        if (travelDistance > bestDist):
            #print(f'if you hold the button for {holdDuration}ms, the boat will travel {travelDistance}mm')
            return True
        else:
            return False
    
    result = []
    factorials = []
    for race in winningRaces:
        print(f'lets evaluate race {race}')
        timeAllotted = race['time']
        print(f'how far can you go in {race["time"]}ms?')
        
        for holdDuration in range(race['time']):
            #print(f'will holding for {holdDuration}ms beat {race["distance"]}mm?')
            if (calcDistance(holdDuration, race["distance"])):
                result.append(True)
        factorials.append(len(result))
        result = []
    print(factorials)
    sum = 1
    for num in factorials:
        sum = num * sum
    print(sum) 

        

winningRaces = parseInput(inputPath)
print(winningRaces)
evaluateRaces(winningRaces)