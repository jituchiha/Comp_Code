class Solution:
    def isValid(self, s: str) -> bool:
        # Optimized 
        # Stack based approach, here we are going to store the opening braces into the stack and the moment we encounter any of the closing parentheses we are going to pop the top element from the stack and check if it's equal and we are going to continue this and to match the valid braces we are going to use a hashmap 
        # n 
        # n 
        # ac 

        bracket_map = {')':'(', '}':'{', ']':'['}

        stack = []

        for char in s:
            if char in bracket_map:
                top = stack.pop() if stack else -1

                if bracket_map[char] != top:
                    return False 

            else:
                stack.append(char) 

        return not stack
        