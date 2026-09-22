class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result = 0
        for operation in operations:
            if operation == "+":
                result += (stack[-1] + stack[-2])
                stack.append(stack[-1] + stack[-2])
            elif operation == "D":
                result += (2*stack[-1])
                stack.append(2*stack[-1])
            elif operation == "C":
                result -= stack.pop()
            else:
                result += int(operation)
                stack.append(int(operation))
        return result