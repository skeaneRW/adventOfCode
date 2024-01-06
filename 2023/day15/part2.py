import re
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

def getBoxContents(str):
    boxes = {}
    for i in range(256):
        boxes[f'box{i}'] = []

    for step in str.split(','):
        pattern = re.compile(r'[^a-zA-Z0-9]')
        operationChar = pattern.search(step).group()
        label, focalLen = step.split(operationChar)
        boxNo = useHashAlgo(label)
        thisBox = boxes[f'box{boxNo}']
        hasLabel = lambda val: any([x.__contains__(val) for x in thisBox])

        def editBox(action, label):
            labelIndex = [i for i, x in enumerate(thisBox) if x.__contains__(label)][0]
            if action == 'del':
                del thisBox[labelIndex]
            else:
                thisBox[labelIndex] = (f'{label} {focalLen}')
        
        if operationChar == '-' and hasLabel(label):
            editBox('del', label)
        elif operationChar == '-' and not hasLabel(label):
            pass
        elif hasLabel(label):
            editBox('replace', label)
        else:
            thisBox.append(f'{label} {focalLen}')
    return boxes

def scoreBoxes(boxes):
    focusingPowers = []
    for boxIndex, box in enumerate(boxes):
        lenses = boxes[box]
        if lenses != []:
            print(lenses)
            for lensOrder, lens in enumerate(lenses):
                focalLen = int(lens.split(' ')[1])
                score = (boxIndex + 1) * (lensOrder + 1) * focalLen
                focusingPowers.append(score)
    print(sum(focusingPowers))


input = parseInput(chosenPath)
boxes = getBoxContents(input)
scoreBoxes(boxes)

