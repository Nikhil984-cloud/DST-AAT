def isBalanced(s):
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return "NO"
        else:
            return "NO"  # Invalid character (shouldn't happen with valid input)
    
    return "YES" if not stack else "NO"

try:
    t = int(input("Enter the number of test cases: ").strip())
    for _ in range(t):
        s = input("Enter the sequence of bracket: ").strip()
        print(isBalanced(s))
except ValueError:
    print("Invalid input, Please enter an integer for number of test cases.")
