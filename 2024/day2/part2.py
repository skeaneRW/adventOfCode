testPath = "./testInput.txt"
inputPath = "./input.txt"
chosenPath = inputPath

def parseInput(path):
    file = open(path, "r")
    result = []
    for line in file.readlines():
        row = line.replace('\n', '').split(' ')
        result.append(list(map(int, row)))
    return result

reports = parseInput(chosenPath)

def reviewReportLines(reports):
    safeReports = []
    for report in reports:
        # based on the report figure out the difference between each level.
        def getLevels(report):
            result = []
            for i in range(len(report)):
                if i != len(report) - 1:
                    result.append(report[i] - report[i + 1])
            return result
        # check to see if a report is safe (all levels are either all negative or all positive)
        # and no level is greater than +3 or less than -3
        def checkSafety(report):
            levels = getLevels(report)
            isSafe = lambda levels: all(i > 0 and i <= 3 for i in levels) or all(i < 0 and i >= -3 for i in levels)
            if isSafe(levels):
                safeReports.append(report)
            # if the report is not safe, loop through the report, remove one level at a time and check 
            # if the report is safe. If it is, add it to the safeReports array.    
            if not isSafe(levels):
                for i in range(len(report)):
                    newReport = report.copy()
                    newReport.pop(i)
                    newLevels = getLevels(newReport)
                    if isSafe(newLevels):
                        safeReports.append(newReport)
                        break
        checkSafety(report)
    return safeReports

safeReports = reviewReportLines(reports)

print(len(safeReports))





        
