class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Optimized 
        # Take a stack and start pushing into it if there's a number and whenever you encounter any operand then pop the last two elements from your stack and then push that into your stack again after everything return the top element in the stack
        # n
        # n 
        # ac
        
        operand_set = {'+','-','*','/'}

        stack = []
        for token in tokens:
            if token in operand_set: 
                if len(stack) >= 2:
                    num_1 = stack.pop()
                    num_2 = stack.pop()

                    if token == "+":
                        stack.append(num_2 + num_1)
                    elif token == '*':
                        stack.append(num_2 * num_1)
                    elif token == '/':
                        stack.append(int(num_2/num_1))
                    elif token == '-':
                        stack.append(num_2 - num_1) 

                    else:
                        print("wrong operator")

                    
                else:
                    print("You shouldn't have reached here :( ")
            else:
                print(token)
                stack.append(int(token))

        return stack[-1]    

        