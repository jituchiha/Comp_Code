class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Brute force
        # Create a single string with lowercase alphanumeric values and then check if they are equal if they are reversed. 
        # n 
        # n
        # ac

        # cleaned_str = ''.join(char.lower() for char in s if char.isalnum())

        # return cleaned_str == cleaned_str[::-1]

        # Optimized
        # Use two pointer one from the beginning and one from the end and keep checking for the values and if in case it's different then return False and if we reach the end then we return True
        # n
        # 1
        # ac
        n = len(s)
        left,right = 0,n-1

        while(left<=right):
           

            # Here we can remove all of the chars except alphanumeric and then run the algo or simply check if it's alphanumeric and if it's not then move to the next char and start you check.

            while left<right and not s[left].isalnum():
                left+=1

            while left<right and  not s[right].isalnum():
                right-=1

            if s[left].lower() !=s[right].lower():
                return False


            left+=1
            right-=1


        return True 