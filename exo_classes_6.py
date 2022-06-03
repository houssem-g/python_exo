class StackCalc:
    def __init__(self):
        self.stack = []
        self.err = ""


    def run(self, instructions):
        listInstruction = []
        if instructions == '':
            self.stack.append(0)
            return self.stack
        elif instructions[0].isdigit() == False and instructions[0] != '':
            self.err = 'Invalid instruction: ' + str(instructions[0])
            return self.err

        for val in instructions.split():
            if val.isdigit():
                self.stack.append(int(val))
                continue
            else:
                listInstruction = instructions[instructions.index(val):].split()
                break

        if len(listInstruction) == 0:
            return self.stack
        
        for i in listInstruction:
            # print(i, self.stack)
            if i == "DUP":
                self.stack.append(self.stack[-1])
                continue
            elif i == "POP":
                self.stack = self.stack[:-1] if len(self.stack)>1 else [0]
                continue
            elif i.isdigit():
                self.stack.append(int(i))
                continue
            elif i.isalpha():
                self.err = 'Invalid instruction: ' + i
                return self.err
            elif eval(str(self.stack[-1]) + i + str(self.stack[-2])) == 0:
                del self.stack[-1]
                continue
            else:
                self.stack[-1] = int(eval(str(self.stack[-1]) + i + str(self.stack[-2])))
                del self.stack[-2] 
        return self.stack
    def getValue(self):
        toreturn = self.err if len(self.err)> 0 else self.stack[-1]
        return toreturn

tests = [
  {'arg': '12', 'ans': 12},
  {'arg': '5 6 +', 'ans': 11},
  {'arg': '3 6 -', 'ans': 3},
  {'arg': '3 DUP +', 'ans': 6},
  {'arg': '2 5 - 5 + DUP +', 'ans': 16},
  {'arg': '9 14 DUP + - 3 POP', 'ans': 19},
  {'arg': '1 2 3 4 5 POP POP POP', 'ans': 2},
  {'arg': '13 DUP 4 POP 5 DUP + DUP + -', 'ans': 7},
  {'arg': '6 5 5 7 * - /', 'ans': 5},
  {'arg': '4 2 4 * 3 + 5 + / 5 -', 'ans': 1},
  {'arg': '5 8 + 4 5 1 + POP 13 +', 'ans': 17},
  {'arg': 'x', 'ans': 'Invalid instruction: x'},
  {'arg': '4 6 + x', 'ans': 'Invalid instruction: x'},
  {'arg': 'y x *', 'ans': 'Invalid instruction: y'},
  {'arg': '', 'ans': 0},
  {'arg': '4 POP', 'ans': 0}
]
for dict in tests:
	arg = dict['arg']
	ans = dict['ans']
	machine = StackCalc()
	machine.run(arg)
	print(machine.getValue(), 'the result is : ', ans)

