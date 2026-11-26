class Solution:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        #print(a, b)
        return a * b

    def div(self, a, b):
        return math.ceil(a / b) if (a/b) < 0 else math.floor(a/b)

    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        operators = {'+': self.add, '-': self.sub, '*': self.mul, '/': self.div}

        for i in range (len(tokens)):
            token = tokens[i]
            if token in operators:
                # print(stack)
                # print(i)
                b = stack.pop()
                a = stack.pop()
                #print(token, a, b)
                res = operators[token](a, b)
                stack.append(res)
                # print(stack)
            else:
                stack.append(int(token))
        
        

        return stack[0]

        