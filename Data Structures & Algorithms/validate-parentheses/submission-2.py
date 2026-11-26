class Solution:
    def isValid(self, s: str) -> bool:

        # Keep a running stack of open parenthesis seen so far
        # For every closed paren we see, check that the 
        # One we expect it to close is at the top of the stack
        # if not, return False
        # if yes, we can pop that open one off the stack since it's been
        # properly accounted for/closed 
        # By the end, after we've seen all characters, 
        # the stack should be empty. 

        stack = []
        mappings = { 
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for char in s:
            if char in mappings:
                if len(stack) > 0 and stack[-1] == mappings[char]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(char)

        print(stack)
        return len(stack) == 0
           
                    

        