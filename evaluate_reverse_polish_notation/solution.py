class Solution:
    # Time: O(?)
    # Space: O(?)
    def eval_rpn(self, tokens: list[str]) -> int:
        operators = "+-*/"
        stack = []

        for t in tokens:
            if t in operators:
                op2 = stack.pop()
                op1 = stack.pop()

                res = self.operate(op1, op2, t)
                print(op1, op2, t, res)

                stack.append(res)
            else:
                stack.append(int(t))

        return stack[-1]

    def operate(self, op1, op2, operator):
        match operator:
            case "+":
                return op1 + op2
            case "-":
                return op1 - op2
            case "*":
                return op1 * op2
            case "/":
                return int(op1 / op2)
