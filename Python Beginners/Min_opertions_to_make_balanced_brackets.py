# Problem statement
# For a given expression in the form of a string, find the minimum number of brackets that can be reversed in order to make the expression balanced. The expression will only contain curly brackets.

# If the expression can't be balanced, return -1.

# Example:
# Expression: {{{{
# If we reverse the second and the fourth opening brackets, the whole expression will get balanced. Since we have to reverse two brackets to make the expression balanced, the expected output will be 2.

# Expression: {{{
# In this example, even if we reverse the last opening bracket, we would be left with the first opening bracket and hence will not be able to make the expression balanced and the output will be -1.

def countBracketReversals(input_string):
    n = len(input_string)
    
    if n % 2 != 0:
        return -1
    
    stack = []
    
    for char in input_string:
        if char == '{':
            stack.append(char)
        else:
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(char)
    
    open_count = 0
    close_count = 0
    
    while stack:
        if stack.pop() == '{':
            open_count += 1
        else:
            close_count += 1
    
    return (open_count + 1) // 2 + (close_count + 1) // 2

#Example 1
input_string = "}{{}}{"
print(countBracketReversals(input_string)) #Output 1
