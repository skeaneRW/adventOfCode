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
        self.solution = self.execute_program
        self.get_bitwise_xor = self.get_bitwise_xor

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
                print(nums)
                for num in nums:
                    program.append(num)
        return register, program
    
    def execute_program(self, pointer, existing_outputs=[]):
        print(f'pointer: {self.program}')
        print()
        outputs = existing_outputs
        if pointer < len(self.program)-1:
            instr = self.program[pointer]
            literal_op = self.program[pointer + 1]
            print(f'instr: {instr}, literal: {literal_op}')
            jump_step, output = self.opcodes[instr](literal_op)
            if output != None:
                outputs.append(output)
            if jump_step != None:
                pointer = jump_step
                self.execute_program(pointer, outputs)
            else:
                pointer += 2
                self.execute_program(pointer, outputs)

        return ','.join([str(output) for output in outputs]), self.register

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
        
    def adv(self, operand): #opcode 0; updates register A - complete
        combo_op = self.get_combo_op(operand)
        numerator = self.register['A']
        denominator = 2 ** combo_op
        print(f'adv: Register A is now {numerator // denominator}')
        self.register['A'] = numerator // denominator
        return None, None
    def bxl(self, operand): #opcode 1; updates register B - test
        b = self.register.get('B')
        op = operand
        bitwise_xor = b ^ op
        self.register['B'] = bitwise_xor
        print(f'bxl: Register B is now {bitwise_xor}')
        return None, None
    def bst(self, operand): #opcode 2; updates register B - test
        combo_op = self.get_combo_op(operand)
        mod_combo_op = combo_op % 8
        print(f'bst: Register B is now {mod_combo_op}')
        self.register['B'] = mod_combo_op
        return None, None
    def jnz(self, operand): #opcode 3; updates instruction pointer - complete
        if self.register['A'] == 0:
            print('jnz: Register A == 0; nothing happens')
            return None, None
        else:
            print(f'jnz: Register A !== 0; opcode == {operand}')
            jump_step = operand
        return jump_step, None
    def bxc(self, operand): #opcode 4; updates register B - test
        b = self.register.get('B')
        c = self.register.get('C')
        bitwise_xor = b ^ c
        self.register['B'] = bitwise_xor
        print(f'bxc: Register B is now {bitwise_xor}')
        return None, operand
    def out(self, operand): #opcode 5; outputs a value - complete
        combo_op = self.get_combo_op(operand)
        print(f'out: modulo 8 of {combo_op} is {combo_op % 8}')
        return None, combo_op % 8
    def bdv(self, operand): #opcode 6; updates register B - complete
        combo_op = self.get_combo_op(operand)
        numerator = self.register['A']
        denominator = 2 ** combo_op
        print(f'adv: Register B is now {numerator // denominator}')
        self.register['B'] = numerator // denominator
        return None, None
    def cdv(self, operand): #opcode 7; updates register C - complete
        combo_op = self.get_combo_op(operand)
        numerator = self.register['A']
        denominator = 2 ** combo_op
        print(f'adv: Register C is now {numerator // denominator}')
        self.register['C'] = numerator // denominator
        return None, None

    def get_bitwise_xor(self, a, b):
        bin_a = bin(a)[2:].zfill(3)  # Convert to binary and remove '0b' prefix
        bin_b = bin(b)[2:].zfill(3)  # Convert to binary and remove '0b' prefix
        result = ''
        for i in range(3):
            result += str(int(bin_a[i]) ^ int(bin_b[i]))
        return int(result, 2)

chosen_input = test
computer = Computer(chosen_input)
solution, final_register = computer.solution(0)
print(f'Solution: {solution}')
print(f'Final Register: {final_register}')