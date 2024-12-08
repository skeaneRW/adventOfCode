testPath = './testInput.txt'
inputPath = './input.txt'
chosenPath = inputPath

import itertools
import re

def getValidEquations(path):
    validEquations = []
    def isValid(result, terms):
        operators = ['+', '*']
        numCombinations = (len(terms)-1) * len(operators)
        def getOperatorCombinations(operators, numCombinations):
            operatorCombinations = []
            for combination in itertools.product(operators, repeat=len(terms)-1):
                operatorCombinations.append(combination)
            return operatorCombinations
        
        def makeExpression (terms, operatorCombinations):
            expressions = []
            for i in range(len(operatorCombinations)):
                expression = []
                for j in range(len(terms)):
                    expression.append(str(terms[j]))
                    if j < len(operatorCombinations[i]):
                        expression.append(str(operatorCombinations[i][j]))
                expressions.append(expression)
            return expressions
        
        allExpressions = makeExpression(terms, getOperatorCombinations(operators, numCombinations))

        def evaluateExpression(expression):
            # Split the expression into tokens (numbers and operators)
            tokens = re.findall(r'\d+|[+*]', expression)
            
            # Initialize the result with the first number
            result = int(tokens[0])
            
            # Iterate through the tokens two at a time (operator followed by number)
            i = 1
            while i < len(tokens):
                operator = tokens[i]
                num = int(tokens[i + 1])
                
                if operator == '+':
                    result += num
                elif operator == '*':
                    result *= num
                i += 2  # Move to the next operator-number pair
            
            return result

        for expression in allExpressions:
            string = ''.join(expression)
            if evaluateExpression(string) == int(result):
                validEquations.append(evaluateExpression(string))
                break

        return validEquations
    with open(path, 'r') as file:    
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            result, terms = line.split(': ')
            terms = terms.split(' ')
            terms = list(map(int, terms))
            total = (isValid(result, terms))
    return (sum(total))

print(getValidEquations(chosenPath))


