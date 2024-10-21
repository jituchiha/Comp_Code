class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Optimized sol 
        # Backtracking approach with stack. we are only going to add open paranthesis if open < n and only adding a closed parathesis if closed < open and finally a combination is only valid if open == closed == n 
        # 2^n 
        # 2^n
        # ac 

        res = [] 

        def backtrack(open,closed,path):
            if open == closed == n:
                res.append(path)
                return 

            if open < n:
                backtrack(open + 1, closed, path+"(")

            if closed<open:
                backtrack(open, closed +1 , path+")")

        backtrack(0,0,"")
        return res 
        