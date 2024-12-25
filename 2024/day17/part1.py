test = 'adventofcode/2024/day17/testInput.txt'
actual = 'adventofcode/2024/day17/input.txt'

class Computer():
    def __init__ (self, input):
        self.input = input
        self.register, self.program = self.parse_input()
        self.opcodes = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }
        self.solution = self.execute_program()

    def parse_input(self):
        register = {}
        program = []
        with open(self.input, 'r') as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            lines[i] = line.strip()
            if 'Register' in lines[i]:
                lines[i] = lines[i].split(': ')
                register[lines[i][0].split(' ')[1]] = int(lines[i][1])
            if 'Program' in lines[i]:
                lines[i] = lines[i].split(': ')
                nums = [int(num) for num in lines[i][1].split(',')]
                for i in range(0, len(nums), 2):
                    program.append((nums[i], nums[i+1]))
        return register, program
    
    def execute_program(self):
        print(f'executing program...{self.program}')
        for instr, literal_op in self.program:
            print(f'instr: {instr}, literal: {literal_op}')
            self.opcodes[instr](literal_op)
            print()

    def get_combo_op(self, literal_op):
        if literal_op <= 3:
            return literal_op
        elif literal_op == 4:
            return self.register['A']
        elif literal_op == 5:
            return self.register['B']
        elif literal_op == 6:
            return self.register['C']
        else:
            return 'error'
        
    def adv(self, operand): #opcode 0
        combo_op = self.get_combo_op(operand)
        numerator = self.register['A']
        denominator = 2 ** combo_op
        print(f'adv: Register A is now {numerator // denominator}')
        self.register['A'] = numerator // denominator
        return
    def bxl(self, operand): #opcode 1
        print('bxl')
        #instruction (opcode 1) performs bitwise XOR.
        return operand
    def bst(self, operand): #opcode 2
        combo_op = self.get_combo_op(operand)
        print('bst', operand)
        #instruction (opcode 2) performs calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits),
        return operand
    def jnz(self, operand): #opcode 3
        if self.register['A'] == 0:
            print('jnz: Register A is 0; doing nothing')
            return
        else:
            print(f'jnz: Register A is not 0; jumping to opcode {operand}')
            self.opcodes[operand](operand)
        return operand
    def bxc(self, operand): #opcode 4
        combo_op = self.get_combo_op(operand)
        print('bxc')
        #instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B.
        return operand
    def out(self, operand): #opcode 5
        combo_op = self.get_combo_op(operand)
        print(f'out: modulo 8 of {combo_op} is {combo_op % 8}')
        return combo_op % 8
    def bdv(self, operand): #opcode 6
        print('bdv')
        #instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register.
        return operand
    def cdv(self, operand): #opcode 7
        combo_op = self.get_combo_op(operand)
        print('cdv')
        #instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. 
        return operand

chosen_input = test
computer = Computer(chosen_input)
print(computer.solution)